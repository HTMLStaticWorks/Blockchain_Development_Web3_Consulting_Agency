import os, glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # accordion buttons
    content = content.replace('accordion-button collapsed bg-transparent text-white', 'accordion-button collapsed bg-transparent')
    
    # footer input
    content = content.replace('class="form-control bg-transparent border-secondary text-white"', 'class="form-control bg-transparent border-secondary"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
