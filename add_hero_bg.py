import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_hero = '''<section class="hero-section text-center position-relative" style="background-image: url('assets/images/hero-bg.png'); background-size: cover; background-position: center;">
            <div class="position-absolute top-0 start-0 w-100 h-100 bg-dark opacity-75"></div>
            <div class="container position-relative z-1">'''
            
    pattern = r'<section class=\"hero-section text-center\">\s*<div class=\"container\">'
    content = re.sub(pattern, new_hero, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Done!')
