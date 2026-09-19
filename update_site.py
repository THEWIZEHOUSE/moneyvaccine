import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update Hero Section to include the image
hero_original = r'''        <!-- Hero Section -->
        <section class="relative pt-32 pb-20 md:pt-48 md:pb-32 overflow-hidden">
            <div class="max-w-7xl mx-auto px-6 relative z-10 text-center">
                <h1 class="text-5xl md:text-7xl font-bold tracking-tight mb-6">
                    ออกแบบชีวิตที่ใช่<br/>
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-300">ด้วยความรู้การเงินที่ถูกต้อง</span>
                </h1>
                <p class="text-xl md:text-2xl text-gray-400 mb-10 max-w-2xl mx-auto font-light">
                    Money Vaccine เปลี่ยนเรื่องเงินให้เป็นเรื่องง่าย พาคุณก้าวสู่อิสรภาพทางการเงินผ่านเวิร์กช็อปและบอร์ดเกม
                </p>
                <div class="flex flex-col sm:flex-row justify-center items-center space-y-4 sm:space-y-0 sm:space-x-6">
                    <a href="#workshops" class="bg-white text-black hover:bg-gray-100 rounded-full px-8 py-3.5 font-semibold text-base transition w-full sm:w-auto">
                        สำรวจเวิร์กช็อป
                    </a>
                    <a href="#free-classes" class="text-white hover:text-blue-400 font-medium transition flex items-center">
                        เริ่มเรียนฟรี <span class="ml-2">→</span>
                    </a>
                </div>
            </div>
            <!-- Background element -->
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-blue-600/20 rounded-full blur-[120px] -z-10"></div>
        </section>'''

hero_new = r'''        <!-- Hero Section -->
        <section class="relative pt-32 pb-16 md:pt-40 md:pb-24 overflow-hidden">
            <div class="max-w-7xl mx-auto px-6 relative z-10">
                <div class="flex flex-col items-center text-center">
                    <h1 class="text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight mb-6 leading-tight">
                        ออกแบบชีวิตที่ใช่<br/>
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-300">ด้วยความรู้การเงิน</span>
                    </h1>
                    <p class="text-xl md:text-2xl text-gray-400 mb-10 max-w-2xl font-light">
                        Money Vaccine เปลี่ยนเรื่องเงินให้เป็นเรื่องง่าย พาคุณก้าวสู่อิสรภาพทางการเงินอย่างยั่งยืน
                    </p>
                    <div class="flex flex-col sm:flex-row justify-center items-center space-y-4 sm:space-y-0 sm:space-x-6 mb-16">
                        <a href="#workshops" class="bg-white text-black hover:bg-gray-100 rounded-full px-8 py-3.5 font-semibold text-base transition w-full sm:w-auto">
                            สำรวจเวิร์กช็อป
                        </a>
                        <a href="#free-classes" class="text-white hover:text-blue-400 font-medium transition flex items-center">
                            เริ่มเรียนฟรี <span class="ml-2">→</span>
                        </a>
                    </div>
                    
                    <!-- Hero Image -->
                    <div class="w-full max-w-5xl mx-auto rounded-[2rem] overflow-hidden relative shadow-2xl border border-white/10 group">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent z-10"></div>
                        <img src="./hero-bg.png" alt="Money Vaccine Seminar" class="w-full h-auto object-cover group-hover:scale-105 transition duration-700 ease-out">
                    </div>
                </div>
            </div>
            <!-- Background element -->
            <div class="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-blue-600/20 rounded-full blur-[120px] -z-10"></div>
        </section>'''

html = html.replace(hero_original, hero_new)

# 2. Fix the Video Aspect Ratios (Make them 9:16 for full Reels feel)
# Workshops
html = html.replace('aspect-[4/5] sm:aspect-[1/1]', 'aspect-[9/16] sm:aspect-[9/16] max-h-[70vh]')
# Free Classes
html = html.replace('aspect-[4/5] bg-black', 'aspect-[9/16] bg-black')

# 3. Add Free Classes CTA
free_classes_end = r'''                </div>
            </div>
        </section>'''

free_classes_cta = r'''                </div>
                
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
                </div>
            </div>
        </section>'''

html = html.replace(free_classes_end, free_classes_cta)

# 4. Add Profile/About Section
about_section = r'''
        <!-- About Founder Section -->
        <section class="py-20 bg-[#fbfbfd]">
            <div class="max-w-6xl mx-auto px-6">
                <div class="flex flex-col md:flex-row items-center gap-12 md:gap-20">
                    <div class="w-full md:w-5/12">
                        <div class="relative rounded-[2rem] overflow-hidden shadow-2xl">
                            <img src="./profile-vaccine.png" alt="Vaccine Profile" class="w-full h-auto object-cover aspect-[4/5]">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
                            <div class="absolute bottom-6 left-6 text-white">
                                <h3 class="text-2xl font-bold">Vaccine</h3>
                                <p class="text-sm font-medium text-white/80">Founder, Money Vaccine</p>
                            </div>
                        </div>
                    </div>
                    <div class="w-full md:w-7/12">
                        <span class="text-xs font-bold text-[#0071e3] tracking-widest uppercase mb-3 block">Behind the Mission</span>
                        <h2 class="text-3xl md:text-5xl font-bold text-gray-900 mb-6 tracking-tight">ทำไมต้อง "วัคซีนการเงิน" ?</h2>
                        <p class="text-lg text-gray-600 mb-6 leading-relaxed">
                            เพราะเราเชื่อว่า "ความรู้ทางการเงินที่ถูกต้อง" คือภูมิคุ้มกันที่ดีที่สุดในการเผชิญหน้ากับโลกยุคใหม่ 
                            เป้าหมายของเราคือการย่อยเรื่องเงินที่ซับซ้อน ให้กลายเป็นเรื่องที่สนุก เข้าใจง่าย และทุกคนสามารถนำไปออกแบบชีวิตของตัวเองได้ทันที
                        </p>
                        <p class="text-lg text-gray-600 leading-relaxed">
                            ไม่ว่าคุณจะอยู่ในวัยเริ่มต้นทำงาน หรือกำลังวางแผนเกษียณ เราพร้อมเป็นส่วนหนึ่งในการสร้าง 
                            "วัคซีน" ที่ช่วยปกป้องและต่อยอดความมั่งคั่งให้กับคุณ
                        </p>
                    </div>
                </div>
            </div>
        </section>
'''

html = html.replace('<!-- Final Call to Action -->', about_section + '\n        <!-- Final Call to Action -->')

with open('index.html', 'w') as f:
    f.write(html)
