import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Remove "เปิดรับสมัครรอบประจำสัปดาห์นี้แล้ว" pill
pill_regex = r'<div class="inline-flex items-center gap-2 px-3\.5 py-1\.5 rounded-full bg-blue-50 border border-blue-100/80 text-\[#0071e3\] text-xs font-semibold mb-6 tracking-wide shadow-sm">\s*<span class="w-2 h-2 rounded-full bg-\[#0071e3\] animate-pulse"></span>\s*เปิดรับสมัครรอบประจำสัปดาห์นี้แล้ว\s*</div>'
html = re.sub(pill_regex, '', html)

# 2. Make Header Huge
old_header = r'<h1 class="text-5xl sm:text-6xl md:text-7xl font-bold tracking-tight text-gradient-dark mb-6 leading-tight">\s*Money Vaccine\.\s*</h1>'
new_header = r'''<h1 class="text-6xl sm:text-8xl md:text-9xl lg:text-[8rem] xl:text-[10rem] whitespace-nowrap font-extrabold tracking-tighter text-gradient-dark mb-6 leading-none -ml-4 sm:-ml-8 md:-ml-12">
                Money Vaccine.
            </h1>'''
html = re.sub(old_header, new_header, html)

# 3. Remove Stats Strip
stats_regex = r'<!-- Stats / Social Proof Strip -->[\s\S]*?(</section>)'
html = re.sub(stats_regex, r'\1', html)

# Wait, if the user wants it to be very wide, maybe making section container max-w-7xl instead of max-w-5xl
# Let's adjust the Hero Section container just in case it restricts the text width
html = re.sub(r'<section class="pt-32 pb-20 md:pt-40 md:pb-28 px-6 text-center max-w-5xl mx-auto">', r'<section class="pt-32 pb-20 md:pt-40 md:pb-28 px-6 text-center w-full max-w-7xl mx-auto overflow-hidden">', html)

with open('index.html', 'w') as f:
    f.write(html)
