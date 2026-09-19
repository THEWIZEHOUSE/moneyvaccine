import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Remove section#about
about_regex = r'<!-- Part 3: About Us & Media Coverage Section -->[\s\S]*?</section>'
html = re.sub(about_regex, '', html)

# 2. Remove About Us link in navbar & footer
html = html.replace('<a href="#about" class="hover:text-white transition">About Us</a>', '')
html = html.replace('<a href="#about" class="block text-gray-300 hover:text-white transition py-1" onclick="toggleMobileMenu()">เกี่ยวกับเรา</a>', '')
html = html.replace('<a href="#about" class="hover:text-gray-900 transition">เกี่ยวกับเรา</a>', '')

with open('index.html', 'w') as f:
    f.write(html)
