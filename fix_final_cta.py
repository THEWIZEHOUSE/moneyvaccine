import re

with open('index.html', 'r') as f:
    html = f.read()

old_text = r'''                <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold tracking-tight mb-4">
                    เริ่มฉีดวัคซีนการเงินของคุณวันนี้
                </h2>
                <p class="text-gray-400 text-base sm:text-lg mb-8 max-w-xl mx-auto">
                    อย่ารอให้เกิดวิกฤตแล้วค่อยเริ่มเรียนรู้ สร้างความมั่นคงทางการเงินในแบบที่คุณเลือกได้
                </p>'''

new_text = r'''                <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold tracking-tight mb-4">
                    เพิ่มวัคซีนการเงินของคุณวันนี้
                </h2>
                <p class="text-gray-400 text-base sm:text-lg mb-8 max-w-xl mx-auto">
                    เพื่อสร้างความมั่นคงทางการเงินในแบบที่คุณเลือกได้
                </p>'''

html = html.replace(old_text, new_text)

with open('index.html', 'w') as f:
    f.write(html)
