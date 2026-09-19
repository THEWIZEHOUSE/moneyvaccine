import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Fix line 152-154 which became <a ...> ... </button>
content = re.sub(
    r'<a href="https://forms\.gle/VyZ4vh8iGvGcAWLR7" target="_blank" class="bg-white/15([^>]+)>\n\s*ลงทะเบียนเวิร์กช็อป\n\s*</button>',
    r'<a href="https://forms.gle/VyZ4vh8iGvGcAWLR7" target="_blank" class="bg-white/15\1>\n                        ลงทะเบียนเวิร์กช็อป\n                    </a>',
    content
)

# 2. Fix Mobile Navbar CTA
content = re.sub(
    r'<button onclick="openModal\(\'Design Your Life Workshop\'\); toggleMobileMenu\(\)" class="apple-btn w-full text-center">\n\s*ลงทะเบียนตอนนี้\n\s*</button>',
    r'<a href="https://forms.gle/VyZ4vh8iGvGcAWLR7" target="_blank" class="apple-btn w-full text-center block" onclick="toggleMobileMenu()">\n                        ลงทะเบียนตอนนี้\n                    </a>',
    content
)

# 3. Fix Design Your Life Card CTA (Line 317)
content = re.sub(
    r'<button onclick="openModal\(\'Design Your Life Workshop\', \'฿600\'\)" class="apple-btn w-full py-3\.5 text-base font-medium">\n\s*ลงทะเบียนทันที\n\s*</button>',
    r'<a href="https://forms.gle/VyZ4vh8iGvGcAWLR7" target="_blank" class="apple-btn w-full py-3.5 text-base font-medium flex justify-center">\n                                ลงทะเบียนทันที\n                            </a>',
    content
)

# 4. Fix Footer CTA (Line 699)
content = re.sub(
    r'<a href="https://forms\.gle/VyZ4vh8iGvGcAWLR7" target="_blank" class="bg-white text-black hover:bg-gray-100 rounded-full px-8 py-3\.5 font-semibold text-base transition">\n\s*ลงทะเบียนเวิร์กช็อปทันที\n\s*</button>',
    r'<a href="https://forms.gle/VyZ4vh8iGvGcAWLR7" target="_blank" class="bg-white text-black hover:bg-gray-100 rounded-full px-8 py-3.5 font-semibold text-base transition inline-block">\n                        ลงทะเบียนเวิร์กช็อปทันที\n                    </a>',
    content
)

with open('index.html', 'w') as f:
    f.write(content)
