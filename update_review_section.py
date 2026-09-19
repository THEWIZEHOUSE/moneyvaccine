import re

with open('index.html', 'r') as f:
    html = f.read()

testimonials_regex = r'<section id="testimonials"[\s\S]*?</section>'

new_testimonials = r'''<section id="testimonials" class="py-16 md:py-24 px-6 bg-white border-t border-black/5">
            <div class="max-w-6xl mx-auto">
                <div class="text-center max-w-2xl mx-auto mb-12">
                    <span class="text-xs font-semibold tracking-wider uppercase text-[#0071e3]">Real Experiences</span>
                    <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-gray-900 mt-2 mb-3">
                        Review จากนักเรียนในคลาส
                    </h2>
                </div>

                <!-- 2-Column Split: Reel Video + Transcript Card -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-center">
                    
                    <!-- Single Reel Video Embed -->
                    <div class="w-full max-w-[380px] mx-auto rounded-3xl overflow-hidden shadow-2xl border border-gray-100 bg-black aspect-[9/16] relative">
                        <iframe src="https://www.instagram.com/p/Db-mX1vS0fs/embed/" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full object-cover"></iframe>
                    </div>

                    <!-- Spoken Transcript & Highlight Card -->
                    <div class="bg-[#fbfbfd] p-8 md:p-10 rounded-3xl border border-black/[0.06] shadow-appleCard flex flex-col justify-between h-full">
                        <div>
                            <div class="inline-flex items-center gap-2 text-[#0071e3] font-semibold text-xs uppercase tracking-wider mb-4 bg-blue-50 px-3 py-1.5 rounded-full border border-blue-100">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 100-6 3 3 0 000 6z"/></svg>
                                ถอดเสียงคำพูดจริงจากคลิป
                            </div>
                            
                            <blockquote class="text-gray-800 text-base md:text-lg leading-relaxed mb-6 font-medium italic">
                                “บรรยากาศในคลาส Cashflow Workshop สนุกและเปิดโลกมากครับ ได้เรียนรู้เรื่องการบริหารกระแสเงินสด การออกจาก Rat Race และการสร้าง Passive Income จากการลงทุนจริงในเกมจำลอง...”
                            </blockquote>
                            
                            <div class="space-y-3.5 border-t border-gray-200/60 pt-6 text-sm text-gray-600">
                                <div class="flex items-start gap-3">
                                    <span class="text-emerald-500 font-bold shrink-0">✓</span>
                                    <span><strong>คลาสจัดเดือนละ 1 ครั้ง:</strong> วันเสาร์ / อาทิตย์ (09:00 - 18:00 น.)</span>
                                </div>
                                <div class="flex items-start gap-3">
                                    <span class="text-emerald-500 font-bold shrink-0">✓</span>
                                    <span><strong>สิทธิพิเศษคูปองส่วนลด:</strong> ทักแอดไลน์แล้วแจ้งว่ามาจาก "วัค" เพื่อรับโค้ดส่วนลดพิเศษได้เลยค่ะ</span>
                                </div>
                            </div>
                        </div>
                        
                        <div class="mt-8 pt-6 border-t border-gray-200/60 flex items-center justify-between">
                            <div class="flex items-center gap-3">
                                <div class="w-10 h-10 rounded-full bg-[#0071e3] text-white font-bold flex items-center justify-center text-sm shadow-md">
                                    MV
                                </div>
                                <div>
                                    <div class="font-bold text-gray-900 text-sm">Cashflow Workshop Review</div>
                                    <div class="text-xs text-gray-400">ถอดเสียงจาก Reel บรรยากาศจริง</div>
                                </div>
                            </div>
                            <a href="https://page.line.me/278sxify" target="_blank" class="text-xs font-semibold text-[#0071e3] hover:underline flex items-center gap-1">
                                รับคูปองส่วนลด <span aria-hidden="true">&rarr;</span>
                            </a>
                        </div>
                    </div>

                </div>
            </div>
        </section>'''

html = re.sub(testimonials_regex, new_testimonials, html, count=1)

with open('index.html', 'w') as f:
    f.write(html)
