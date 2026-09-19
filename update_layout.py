import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update Design Your Life iframe to be more responsive (Mobile/PC)
html = re.sub(
    r'<iframe src="https://www.instagram.com/p/DdNcXQtS_LL/embed/" width="100%" height="480" frameborder="0" scrolling="no" allowtransparency="true" class="max-w-\[400px\]"></iframe>',
    r'<iframe src="https://www.instagram.com/p/DdNcXQtS_LL/embed/" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full object-cover"></iframe>',
    html
)
# Wrap the DYL iframe in an aspect-ratio box
html = re.sub(
    r'<div class="w-full rounded-2xl mb-6 overflow-hidden relative group-hover:shadow-md transition duration-300 border border-gray-100 bg-white flex justify-center">',
    r'<div class="w-full aspect-[4/5] sm:aspect-[1/1] rounded-2xl mb-6 overflow-hidden relative group-hover:shadow-md transition duration-300 border border-gray-100 bg-black flex justify-center">',
    html
)

# 2. Update Cashflow iframe to be responsive
html = re.sub(
    r'<iframe src="https://www.instagram.com/p/DdA-hifSstI/embed/" width="100%" height="480" frameborder="0" scrolling="no" allowtransparency="true" class="max-w-\[400px\]"></iframe>',
    r'<iframe src="https://www.instagram.com/p/DdA-hifSstI/embed/" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full object-cover"></iframe>',
    html
)
html = re.sub(
    r'<div class="w-full rounded-2xl mb-6 overflow-hidden relative group-hover:shadow-md transition duration-300 border border-white/10 bg-black flex justify-center">',
    r'<div class="w-full aspect-[4/5] sm:aspect-[1/1] rounded-2xl mb-6 overflow-hidden relative group-hover:shadow-md transition duration-300 border border-white/10 bg-black flex justify-center">',
    html
)

# 3. Update Free Class iframes to be responsive (aspect-[9/16] or similar)
html = re.sub(
    r'<iframe src="https://www.instagram.com/p/DZ2ds38yu-d/embed/" width="100%" height="400" frameborder="0" scrolling="no" allowtransparency="true"></iframe>',
    r'<iframe src="https://www.instagram.com/p/DZ2ds38yu-d/embed/" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full"></iframe>',
    html
)
html = re.sub(
    r'<iframe src="https://www.instagram.com/p/DUm59aYkgdJ/embed/" width="100%" height="400" frameborder="0" scrolling="no" allowtransparency="true"></iframe>',
    r'<iframe src="https://www.instagram.com/p/DUm59aYkgdJ/embed/" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full"></iframe>',
    html
)
html = re.sub(
    r'<iframe src="https://www.instagram.com/p/DaAeaWPwwGf/embed/" width="100%" height="400" frameborder="0" scrolling="no" allowtransparency="true"></iframe>',
    r'<iframe src="https://www.instagram.com/p/DaAeaWPwwGf/embed/" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full"></iframe>',
    html
)
# Change the container for Free classes
html = re.sub(
    r'<div class="relative w-full bg-white flex justify-center border-b border-black/\[0\.06\]">',
    r'<div class="relative w-full aspect-[4/5] bg-black flex justify-center border-b border-black/[0.06] overflow-hidden">',
    html
)

with open('index.html', 'w') as f:
    f.write(html)
