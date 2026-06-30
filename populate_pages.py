import glob
import os
import re

dir_path = "e:/OfficeDownloads_/MayJuneWebsite/Blockchain_Development_Web3_Consulting_Agency"
files = glob.glob(os.path.join(dir_path, "*.html"))

# Regex to find these empty placeholder sections: 
# e.g., <section class="py-5 text-center"><div class="container"><h2>Our Story</h2></div></section>
# Note: we need to handle variations in classes and newlines.
pattern = re.compile(r'<section class="([^"]*)">\s*<div class="container">\s*<h2>(.*?)</h2>\s*</div>\s*</section>', re.IGNORECASE | re.DOTALL)

specific_replacements = {
    "Our Story": """<div class="row g-4 align-items-center text-start">
                    <div class="col-lg-6">
                        <h2 class="text-center text-lg-start">Our Story</h2>
                        <p class="text-muted mt-4">NodeX was founded with a single mission: to provide enterprise-grade security and scalability to the NodeX ecosystem. From early days in Bitcoin and Ethereum communities, our founders recognized the need for professional, institutional-level development practices in the decentralized space.</p>
                        <p class="text-muted">Today, we are a global team of cryptographers, architects, and engineers dedicated to building robust decentralized applications that stand the test of time.</p>
                    </div>
                    <div class="col-lg-6">
                        <div class="glass-panel p-5 rounded d-flex align-items-center justify-content-center h-100" style="min-height: 300px;">
                            <h3 class="text-gradient mb-0 text-center">Building the Future Since 2018</h3>
                        </div>
                    </div>
                </div>""",
    "Mission & Vision": """<h2 class="mb-4 text-center">Mission & Vision</h2>
                <div class="row g-4 text-center">
                    <div class="col-md-6 d-flex">
                        <div class="p-4 bg-transparent border border-secondary rounded w-100 h-100">
                            <h4 class="text-primary mb-3">Our Mission</h4>
                            <p class="text-muted mb-0">To accelerate the global transition to decentralized infrastructure by providing top-tier, secure, and scalable blockchain engineering services.</p>
                        </div>
                    </div>
                    <div class="col-md-6 d-flex">
                        <div class="p-4 bg-transparent border border-secondary rounded w-100 h-100">
                            <h4 class="text-primary mb-3">Our Vision</h4>
                            <p class="text-muted mb-0">A future where trust is embedded in code, systems are transparent by default, and financial sovereignty is accessible to everyone.</p>
                        </div>
                    </div>
                </div>""",
    "Core Values": """<h2 class="mb-4 text-center">Core Values</h2>
                <div class="row g-4 text-center">
                    <div class="col-md-4 d-flex">
                        <div class="card bg-transparent border-secondary w-100 h-100 p-4">
                            <h4 class="text-primary">Integrity</h4>
                            <p class="text-muted mb-0">We build transparent and immutable systems, and we operate with the same transparency.</p>
                        </div>
                    </div>
                    <div class="col-md-4 d-flex">
                        <div class="card bg-transparent border-secondary w-100 h-100 p-4">
                            <h4 class="text-primary">Excellence</h4>
                            <p class="text-muted mb-0">We pursue technical perfection in every smart contract and protocol we deploy.</p>
                        </div>
                    </div>
                    <div class="col-md-4 d-flex">
                        <div class="card bg-transparent border-secondary w-100 h-100 p-4">
                            <h4 class="text-primary">Innovation</h4>
                            <p class="text-muted mb-0">We stay at the bleeding edge of cryptography and decentralized technologies.</p>
                        </div>
                    </div>
                </div>""",
    "Service Categories": """<h2 class="mb-4 text-center">Service Categories</h2>
                <div class="row g-4 text-center">
                    <div class="col-md-4 d-flex">
                        <div class="service-card text-center w-100 h-100 p-4 border border-secondary rounded">
                            <h4 class="text-primary">DeFi Protocols</h4>
                            <p class="text-muted mb-0">DEXs, lending platforms, and yield aggregators built for scale.</p>
                        </div>
                    </div>
                    <div class="col-md-4 d-flex">
                        <div class="service-card text-center w-100 h-100 p-4 border border-secondary rounded">
                            <h4 class="text-primary">NFT Ecosystems</h4>
                            <p class="text-muted mb-0">Marketplaces, dynamic NFTs, and robust fractionalization engines.</p>
                        </div>
                    </div>
                    <div class="col-md-4 d-flex">
                        <div class="service-card text-center w-100 h-100 p-4 border border-secondary rounded">
                            <h4 class="text-primary">DAOs & Governance</h4>
                            <p class="text-muted mb-0">Voting mechanisms, robust treasuries, and sustainable tokenomics.</p>
                        </div>
                    </div>
                </div>"""
}

def get_generic_replacement(title):
    lower_title = title.lower()
    return f"""<h2 class="mb-4 text-center">{title}</h2>
                <div class="row g-4 text-center">
                    <div class="col-md-6 d-flex">
                        <div class="p-4 bg-transparent border border-secondary rounded w-100 h-100">
                            <h4 class="text-primary mb-3">{title} Solutions</h4>
                            <p class="text-muted mb-0">We offer comprehensive solutions and deep expertise in {lower_title}, ensuring security, scalability, and robust performance for your decentralized applications.</p>
                        </div>
                    </div>
                    <div class="col-md-6 d-flex">
                        <div class="p-4 bg-transparent border border-secondary rounded w-100 h-100">
                            <h4 class="text-primary mb-3">Enterprise Grade Approach</h4>
                            <p class="text-muted mb-0">Our approach to {lower_title} involves rigorous testing, multi-stage audits, and industry best practices to deliver production-ready infrastructure.</p>
                        </div>
                    </div>
                </div>"""

for file in files:
    # Skip index and home-2 to not break them
    if file.endswith("index.html") or file.endswith("home-2.html"):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replacer(match):
        section_class = match.group(1)
        # Ensure text-center is in section class to match alignment request
        if 'text-center' not in section_class:
            section_class += ' text-center'
            
        title = match.group(2).strip()
        
        inner_content = specific_replacements.get(title, get_generic_replacement(title))
        
        return f'<section class="{section_class}">\n            <div class="container">\n                {inner_content}\n            </div>\n        </section>'
        
    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated placeholders in {os.path.basename(file)}")
