import re

with open('index.html', 'r') as f:
    html = f.read()

# The block to remove:
cta_block = r'''                
                <!-- Free Classes Line OA CTA -->
                <div class="mt-16 max-w-4xl mx-auto bg-gradient-to-br from-blue-50 to-indigo-50 rounded-3xl p-8 md:p-12 text-center border border-blue-100 shadow-sm relative overflow-hidden">
                    <div class="absolute top-0 right-0 -mt-10 -mr-10 w-40 h-40 bg-blue-600/10 rounded-full blur-2xl"></div>
                    <div class="absolute bottom-0 left-0 -mb-10 -ml-10 w-40 h-40 bg-indigo-600/10 rounded-full blur-2xl"></div>
                    
                    <h3 class="text-2xl md:text-3xl font-bold text-gray-900 mb-4 relative z-10">อยากเรียนคลาสการเงินฟรีแบบเต็มๆ?</h3>
                    <p class="text-gray-600 mb-8 text-base md:text-lg relative z-10">
                        แอดไลน์ OA ของวัคซีน แล้วพิมพ์คำว่า <span class="font-bold text-[#0071e3] bg-blue-100 px-2 py-1 rounded">FREE</span> <br class="hidden md:block">
                        ระบบจะส่งลิงก์เข้าเรียนฟรีให้ทันที!
                    </p>
                    <a href="#" class="inline-flex items-center justify-center bg-[#00B900] hover:bg-[#009900] text-white rounded-full px-8 py-4 font-semibold text-lg transition shadow-md relative z-10 w-full sm:w-auto">
                        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 24 24"><path d="M24 10.304c0-5.369-5.383-9.738-12-9.738-6.616 0-12 4.369-12 9.738 0 4.814 3.784 8.871 9.07 9.615.353.056.822.173 1.053.407.214.215.27.568.204.887l-.462 2.766c-.053.309.28.539.544.384 2.146-1.258 5.485-3.328 7.378-5.312 3.125-3.084 4.213-5.753 4.213-8.747z"/></svg>
                        แอดไลน์ @moneyvaccine
                    </a>
                    <p class="text-xs text-gray-400 mt-4 relative z-10">(เดี๋ยวทางเราจะมาอัปเดตลิงก์ Line OA ให้อีกที กดเตรียมไว้ก่อนได้เลย)</p>
                </div>'''

# Remove ALL CTA blocks
html = html.replace(cta_block, "")

# Find the end of Free Classes section and insert ONE CTA block
free_classes_end = r'''                    <!-- Lesson 3 -->
                    <div class="group bg-[#fbfbfd] rounded-2xl overflow-hidden border border-black/[0.06] hover:shadow-appleCardHover transition-all duration-300 flex flex-col">
                        <!-- Instagram Reel Embed -->
                        <div class="relative w-full bg-black flex justify-center border-b border-black/[0.06] overflow-hidden aspect-[9/16]">
                            <iframe src="https://www.instagram.com/p/DaAeaWPwwGf/embed/" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full"></iframe>
                        </div>
                        <div class="p-6 flex-1 flex flex-col justify-between">
                            <div>
                                <span class="text-xs font-semibold text-[#0071e3] uppercase tracking-wide">บทที่ 3 • Financial Health</span>
                                <h3 class="text-lg font-bold text-gray-900 mt-2 mb-2 group-hover:text-[#0071e3] transition">
                                    อ่านงบการเงินชีวิตตนเองใน 1 แผ่นเพื่อวางแผนเกษียณ
                                </h3>
                                <p class="text-sm text-gray-500 line-clamp-2">
                                    วิเคราะห์สุขภาพทางการเงิน สินทรัพย์ หนี้สินดี-หนี้สินร้าย เพื่อเตรียมตัวสู่เป้าหมายระยะยาว
                                </p>
                            </div>
                            <div class="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between text-xs text-gray-400">
                                <span>เข้าชมฟรีบน IG</span>
                                <a href="https://www.instagram.com/reel/DaAeaWPwwGf/" target="_blank" class="text-[#0071e3] font-semibold hover:underline flex items-center gap-1">
                                    ดูบน Instagram <span aria-hidden="true">&rarr;</span>
                                </a>
                            </div>
                        </div>
                    </div>

                </div>'''

if free_classes_end in html:
    html = html.replace(free_classes_end, free_classes_end + cta_block)

with open('index.html', 'w') as f:
    f.write(html)
