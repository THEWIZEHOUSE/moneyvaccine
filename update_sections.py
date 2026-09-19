import re

with open('index.html', 'r') as f:
    html = f.read()

# --- 1. Design Your Life Bullets ---
old_dyl_bullets = r'''                            <!-- Key Feature Bullets -->
                            <div class="space-y-3 mb-8 text-sm text-gray-600">
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>สร้างพิมพ์เขียวชีวิต (Life & Financial Blueprint) ของตนเอง</span>
                                </div>
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>จำลองสถานการณ์วิกฤตทางการเงิน และวิธีรับมืออย่างปลอดภัย</span>
                                </div>
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>ตกผลึกเป้าหมายการเงินและชีวิตที่สอดคล้องกัน 100%</span>
                                </div>
                            </div>'''

new_dyl_bullets = r'''                            <!-- Key Feature Bullets -->
                            <div class="space-y-3 mb-8 text-sm text-gray-600">
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>ตกตะกอนความคิดผ่านกระดานชีวิตของตนเอง</span>
                                </div>
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>กลับมาอยู่กับตัวเองที่ไม่ต้องแข่งขันกับใครในชีวิตจริง</span>
                                </div>
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>กลุ่มเล็กจำกัด 6-8 ท่าน เพื่อการดูแลและโค้ชชิ่งอย่างใกล้ชิด</span>
                                </div>
                            </div>'''

html = html.replace(old_dyl_bullets, new_dyl_bullets)


# --- 2. Cashflow Club Description & Bullets ---
old_cashflow_desc = r'''                            <p class="text-gray-400 text-sm sm:text-base mb-6 leading-relaxed">
                                ออกจากสนามแข่งหนู (Rat Race) และสร้างอิสรภาพทางการเงิน ผ่านเกมจำลองการเงินระดับโลก พร้อมการวิเคราะห์การลงทุนจริง
                            </p>'''

new_cashflow_desc = r'''                            <p class="text-gray-400 text-sm sm:text-base mb-6 leading-relaxed">
                                ความรู้ทางการเงินที่โรงเรียนไม่เคยสอน แต่ที่นี่สอน! เพราะอยากให้พวกเธอมีชีวิตการเงินที่ดีขึ้น<br>
                                ออกจากสนามแข่งหนู (Rat Race) ใช้แรงและเวลาแลกเงิน<br>
                                แต่สร้างอิสรภาพทางการเงิน ผ่านเกมจำลองการเงินระดับโลก
                            </p>'''

html = html.replace(old_cashflow_desc, new_cashflow_desc)

old_cashflow_bullets = r'''                            <!-- Key Feature Bullets -->
                            <div class="space-y-3 mb-8 text-sm text-gray-300">
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>ฝึกคิดและตัดสินใจแบบนักลงทุนอสังหาฯ และเจ้าของธุรกิจ</span>
                                </div>
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>สร้างกระแสเงินสดเชิงบวก (Passive Cashflow) สู่ Fast Track</span>
                                </div>
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>Networking กับกลุ่มเพื่อนที่มีเป้าหมายทางการเงินร่วมกัน</span>
                                </div>
                            </div>'''

new_cashflow_bullets = r'''                            <!-- Key Feature Bullets -->
                            <div class="space-y-3 mb-8 text-sm text-gray-300">
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>ฝึกคิดและตัดสินใจแบบนักลงทุนอสังหาฯ และเจ้าของธุรกิจ</span>
                                </div>
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>สร้างรายได้จากทรัพย์สินไปสู่ Fast Track</span>
                                </div>
                                <div class="flex items-start gap-2.5">
                                    <svg class="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                    <span>Networking กับคนที่มีเป้าหมายทางการเงินคล้ายกัน</span>
                                </div>
                            </div>'''

html = html.replace(old_cashflow_bullets, new_cashflow_bullets)


# --- 3. Cashflow Location & Time Box ---
old_cashflow_schedule = r'''                            <!-- Schedule & Location Box -->
                            <div class="text-left text-sm text-gray-300 bg-white/5 rounded-2xl p-5 mb-8 border border-white/10 space-y-2.5">
                                <div class="flex items-center gap-2.5">
                                    <span class="text-gray-400">📍</span>
                                    <span><strong>สถานที่:</strong> ใจกลางกรุงเทพฯ (แนวรถไฟฟ้า BTS/MRT)</span>
                                </div>
                                <div class="flex items-center gap-2.5">
                                    <span class="text-gray-400">⏰</span>
                                    <span><strong>รอบถัดไป:</strong> วันเสาร์-อาทิตย์ | 13:00 น. - 18:00 น. (เต็มวัน)</span>
                                </div>
                                <div class="flex items-center gap-2.5">
                                    <span class="text-gray-400">✨</span>
                                    <span><strong>สิทธิพิเศษ:</strong> สมาชิกคอมมูนิตี้แลกเปลี่ยนไอเดียรายเดือน</span>
                                </div>
                            </div>'''

new_cashflow_schedule = r'''                            <!-- Schedule & Location Box -->
                            <div class="text-left text-sm text-gray-300 bg-white/5 rounded-2xl p-5 mb-8 border border-white/10 space-y-2.5">
                                <div class="flex items-center gap-2.5">
                                    <span class="text-gray-400">📍</span>
                                    <span><strong>สถานที่:</strong> โรงแรม โนโวเทล แพลทตินัมประตูน้ำ (ถ้าเปลี่ยนแปลง จะอัพเดตอีกครั้ง)</span>
                                </div>
                                <div class="flex items-center gap-2.5">
                                    <span class="text-gray-400">⏰</span>
                                    <span><strong>เวลาเรียน:</strong> 09:00 น. - 18:00 น. (เต็มวัน)</span>
                                </div>
                                <div class="flex items-center gap-2.5">
                                    <span class="text-gray-400">✨</span>
                                    <span><strong>สิทธิพิเศษ:</strong> สมาชิกคอมมูนิตี้แลกเปลี่ยนไอเดียรายเดือน</span>
                                </div>
                            </div>'''

html = html.replace(old_cashflow_schedule, new_cashflow_schedule)


# --- 4. Remove badge from Cashflow price block ---
old_badge = r'''                                <span class="text-xs font-medium px-2.5 py-1 rounded bg-white/10 text-gray-300">
                                    กลุ่มเล็กจำกัด 6-8 ท่าน เพื่อการดูแลและโค้ชชิ่งอย่างใกล้ชิด
                                </span>'''

html = html.replace(old_badge, '')

# --- 5. Cashflow Button Text ---
html = html.replace('ลงทะเบียนจองรอบถัดไป', 'ลงทะเบียนเพื่อรับส่วนลด15%')


# --- 6. LINE Banner Text ---
old_line_banner_text = r'''                    <p class="text-gray-600 mb-8 text-base md:text-lg relative z-10">
                        แอดไลน์ OA ของวัคซีน แล้วพิมพ์คำว่า <span class="font-bold text-[#0071e3] bg-blue-100 px-2 py-1 rounded">FREE</span> <br class="hidden md:block">
                        ระบบจะส่งลิงก์เข้าเรียนฟรีให้ทันที!
                    </p>'''

new_line_banner_text = r'''                    <p class="text-gray-600 mb-8 text-base md:text-lg relative z-10">
                        แอดไลน์ OA ของวัค แล้วพิมพ์คำว่า <span class="font-bold text-[#0071e3] bg-blue-100 px-2 py-1 rounded">FREE</span> <br class="hidden md:block">
                        แล้ววัคจะรีบมาตอบด้วยตัวเองค่า
                    </p>'''

html = html.replace(old_line_banner_text, new_line_banner_text)


# --- 7. Remove "ภาพบรรยากาศและการเรียนรู้" block ---
html = re.sub(
    r'<!-- Media Gallery Highlights \(Replaces placeholders\) -->[\s\S]*?</div>\s*</div>\s*</div>',
    '',
    html
)


# --- 8. Real Experiences: Replace with ONLY ONE Reel clip (Db-mX1vS0fs) and remove text reviews ---
old_testimonials_section = r'''        <!-- Section: Testimonials -->
        <section id="testimonials" class="py-16 md:py-24 px-6 bg-white border-t border-black/5">
            <div class="max-w-6xl mx-auto">
                <div class="text-center max-w-2xl mx-auto mb-14">
                    <span class="text-xs font-semibold tracking-wider uppercase text-[#0071e3]">Real Experiences</span>
                    <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-gray-900 mt-2 mb-3">
                        เสียงตอบรับจากผู้เข้าร่วมเวิร์กช็อป
                    </h2>
                    <p class="text-gray-500 text-sm sm:text-base">
                        ความประทับใจจริงจากผู้ที่ได้เข้าร่วมปรับเปลี่ยนวิธีคิดทางการเงินกับเรา
                    </p>
                </div>

                <!-- Testimonial Cards Grid -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <!-- Review 1 -->
                    <div class="bg-[#fbfbfd] rounded-2xl p-6 border border-black/[0.04] shadow-sm flex flex-col justify-between">
                        <p class="text-gray-600 text-sm leading-relaxed mb-6">
                            "ตอนแรกคิดว่าเป็นแค่บอร์ดเกมธรรมดา แต่พอเล่นจบเหมือนได้เห็นอนาคตทางการเงินของตัวเองในอีก 10 ปีข้างหน้า รู้เลยว่าต้องปรับตรงไหน!"
                        </p>
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-blue-100 text-[#0071e3] font-bold flex items-center justify-center text-sm">
                                K
                            </div>
                            <div>
                                <h4 class="text-sm font-semibold text-gray-900">คุณกานต์</h4>
                                <p class="text-xs text-gray-400">พนักงานบริษัทเอกชน (Design Your Life รุ่น 42)</p>
                            </div>
                        </div>
                    </div>

                    <!-- Review 2 -->
                    <div class="bg-[#fbfbfd] rounded-2xl p-6 border border-black/[0.04] shadow-sm flex flex-col justify-between">
                        <p class="text-gray-600 text-sm leading-relaxed mb-6">
                            "ชอบตรงที่ได้ลองเสี่ยงและล้มเหลวในเกม ทำให้เรากล้าตัดสินใจในชีวิตจริงมากขึ้น บรรยากาศเป็นกันเอง โค้ชเชอร์ให้คำแนะนำดีมากครับ"
                        </p>
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-indigo-100 text-indigo-600 font-bold flex items-center justify-center text-sm">
                                P
                            </div>
                            <div>
                                <h4 class="text-sm font-semibold text-gray-900">คุณภัทร</h4>
                                <p class="text-xs text-gray-400">เจ้าของธุรกิจส่วนตัว (Cashflow Club Thailand)</p>
                            </div>
                        </div>
                    </div>

                    <!-- Review 3 -->
                    <div class="bg-[#fbfbfd] rounded-2xl p-6 border border-black/[0.04] shadow-sm flex flex-col justify-between">
                        <p class="text-gray-600 text-sm leading-relaxed mb-6">
                            "ได้เจอสังคมของคนที่มีเป้าหมายอยากพัฒนาตัวเองเหมือนกัน คุ้มค่ามากครับ ได้ทั้งความรู้คอนเนกชันและพลังกายใจกลับไปเต็มเปี่ยม"
                        </p>
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-600 font-bold flex items-center justify-center text-sm">
                                M
                            </div>
                            <div>
                                <h4 class="text-sm font-semibold text-gray-900">คุณเมย์</h4>
                                <p class="text-xs text-gray-400">Software Engineer (Design Your Life รุ่น 48)</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

new_testimonials_section = r'''        <!-- Section: Real Experiences -->
        <section id="testimonials" class="py-16 md:py-24 px-6 bg-white border-t border-black/5">
            <div class="max-w-4xl mx-auto">
                <div class="text-center max-w-2xl mx-auto mb-10">
                    <span class="text-xs font-semibold tracking-wider uppercase text-[#0071e3]">Real Experiences</span>
                    <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-gray-900 mt-2 mb-3">
                        บรรยากาศและเสียงตอบรับจริง
                    </h2>
                </div>

                <!-- Single Reel Video Embed -->
                <div class="max-w-[420px] mx-auto rounded-3xl overflow-hidden shadow-2xl border border-gray-100 bg-black aspect-[9/16] relative">
                    <iframe src="https://www.instagram.com/p/Db-mX1vS0fs/embed/" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full object-cover"></iframe>
                </div>
            </div>
        </section>'''

html = html.replace(old_testimonials_section, new_testimonials_section)


# --- 9. Behind the Mission: Keep ONLY ONE instance ---
# Find all occurrences of the About Founder section and keep only the first one
about_pattern = r'<!-- About Founder Section -->[\s\S]*?</section>'
about_matches = list(re.finditer(about_pattern, html))

if len(about_matches) > 1:
    # Remove second occurrence
    first_match = about_matches[0]
    second_match = about_matches[1]
    html = html[:second_match.start()] + html[second_match.end():]

with open('index.html', 'w') as f:
    f.write(html)
