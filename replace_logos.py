import glob
import os

dir_path = "e:/OfficeDownloads_/MayJuneWebsite/Blockchain_Development_Web3_Consulting_Agency"
files = glob.glob(os.path.join(dir_path, "*.html"))

target_footer = '<h3 class="text-gradient mb-4">NodeX</h3>'
replace_footer = '<a <a class="navbar-brand d-flex align-items-center gap-2 fs-4 fw-bold" href="index.html" style="padding: 0;">\n                        <img src="assets/logo.svg" alt="NodeX Logo" width="32" height="32">\n                        NodeX\n                    </a>'

target_header = '<a class="navbar-brand text-gradient d-flex align-items-center gap-2" href="index.html">'
replace_header = '<a class="navbar-brand d-flex align-items-center gap-2 fs-4 fw-bold" href="index.html">'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(target_footer, replace_footer).replace(target_header, replace_header)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file)}")
