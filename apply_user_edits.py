import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Remove dot from Money Vaccine. in Hero H1
html = html.replace('Money Vaccine.', 'Money Vaccine')

# 2. Add "Visual notes • Simple finance • Big impact" below subtitle in Hero
old_hero_p = r'''                <p class="text-xl sm:text-2xl text-gray-200 font-medium max-w-2xl mx-auto leading-relaxed mb-12 drop-shadow-lg">
                    ยกระดับทักษะการเงิน และออกแบบชีวิตในแบบที่คุณต้องการ<br class="hidden sm:inline">
                    ผ่านการจำลองประสบการณ์จริง สู่ผลลัพธ์ที่จับต้องได้
                </p>'''

new_hero_p = r'''                <p class="text-xl sm:text-2xl text-gray-200 font-medium max-w-2xl mx-auto leading-relaxed mb-6 drop-shadow-lg">
                    ยกระดับทักษะการเงิน และออกแบบชีวิตในแบบที่คุณต้องการ<br class="hidden sm:inline">
                    ผ่านการจำลองประสบการณ์จริง สู่ผลลัพธ์ที่จับต้องได้
                </p>

                <!-- Subtitle Tagline -->
                <div class="inline-flex items-center gap-2 sm:gap-3 text-xs sm:text-sm font-semibold text-blue-200 uppercase tracking-widest mb-12 bg-white/10 backdrop-blur-md px-5 py-2 rounded-full border border-white/20 shadow-lg">
                    <span>Visual notes</span>
                    <span class="text-blue-400">•</span>
                    <span>Simple finance</span>
                    <span class="text-blue-400">•</span>
                    <span>Big impact</span>
                </div>'''

html = html.replace(old_hero_p, new_hero_p)

# 3. Change "สำรวจเวิร์กช็อป" to "ค้นหาเวิร์กช็อป"
html = html.replace('สำรวจเวิร์กช็อป', 'ค้นหาเวิร์กช็อป')

# 4. Remove "Flagship Programs"
html = html.replace('<span class="text-xs font-semibold tracking-wider uppercase text-[#0071e3]">Flagship Programs</span>', '')

# 5. Remove "🌟 ยอดนิยมประจำเดือน" top tag
html = re.sub(
    r'<div class="absolute top-6 right-6">\s*<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-blue-50 text-\[#0071e3\] border border-blue-100">\s*🌟 ยอดนิยมประจำเดือน\s*</span>\s*</div>',
    '',
    html
)

# 6. Remove "⚡ Intensive Board Game" top tag
html = re.sub(
    r'<div class="absolute top-6 right-6">\s*<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-white/10 text-emerald-400 border border-white/10">\s*⚡ Intensive Board Game\s*</span>\s*</div>',
    '',
    html
)

# 7. Update Design Your Life description paragraph
old_dyl_desc = r'''                            <p class="text-gray-500 text-sm sm:text-base mb-6 leading-relaxed">
                                เรียนรู้การวางแผนการเงินและออกแบบเป้าหมายชีวิตผ่านประสบการณ์จำลอง ช่วยให้เห็นภาพรวมของรายได้ รายจ่าย และการตัดสินใจในอนาคตได้อย่างแม่นยำ
                            </p>'''

new_dyl_desc = r'''                            <p class="text-gray-600 text-sm sm:text-base mb-6 leading-relaxed">
                                อย่าปล่อยให้ชีวิตเป็นเรื่องบังเอิญค่ะ<br>
                                มาออกแบบชีวิต (Design Your Life)<br>
                                ให้มีความหมายในแบบที่ต้องการจริงๆ<br>
                                เพราะชีวิตจริงมีแค่รอบเดียว... ซ้อมให้ดี<br>
                                เพื่อที่จะได้ใช้ชีวิตที่ "สวยงามที่สุด"<br>
                                ในแบบของทุกคนเองนะคะ<br>
                                <span class="font-semibold text-[#0071e3] mt-2 block">เรียนรู้ผ่าน actual life board game</span>
                            </p>'''

html = html.replace(old_dyl_desc, new_dyl_desc)

# 8. Update group size text for Cashflow Club
html = html.replace('รับรอบละ 12 ท่าน', 'กลุ่มเล็กจำกัด 6-8 ท่าน เพื่อการดูแลและโค้ชชิ่งอย่างใกล้ชิด')

with open('index.html', 'w') as f:
    f.write(html)
