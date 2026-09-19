import re

with open('index.html', 'r') as f:
    html = f.read()

hero_regex = r'<!-- Hero Section -->[\s\S]*?</section>'

new_hero = r'''<!-- Hero Section -->
        <section class="relative pt-40 pb-32 md:pt-52 md:pb-44 px-6 text-center w-full min-h-[75vh] md:min-h-[85vh] flex flex-col justify-center items-center overflow-hidden bg-black mt-[-44px]">
            
            <!-- Background Image -->
            <div class="absolute inset-0 z-0">
                <img src="./hero-bg.png" alt="Money Vaccine Background" class="w-full h-full object-cover object-[center_30%]">
                <div class="absolute inset-0 bg-gradient-to-b from-black/80 via-black/40 to-[#f5f5f7]"></div>
            </div>
            
            <div class="relative z-10 w-full max-w-7xl mx-auto -mt-10">
                <h1 class="text-6xl sm:text-8xl md:text-9xl lg:text-[8rem] xl:text-[10rem] whitespace-nowrap font-extrabold tracking-tighter text-white mb-6 leading-none drop-shadow-2xl">
                    Money Vaccine.
                </h1>
                
                <p class="text-xl sm:text-2xl text-gray-200 font-medium max-w-2xl mx-auto leading-relaxed mb-12 drop-shadow-lg">
                    ยกระดับทักษะการเงิน และออกแบบชีวิตในแบบที่คุณต้องการ<br class="hidden sm:inline">
                    ผ่านการจำลองประสบการณ์จริง สู่ผลลัพธ์ที่จับต้องได้
                </p>

                <!-- Action Buttons -->
                <div class="flex flex-col sm:flex-row items-center justify-center gap-4 max-w-md mx-auto">
                    <a href="#workshops" class="bg-white text-black hover:bg-gray-100 rounded-full px-8 py-3.5 font-semibold text-base transition w-full sm:w-auto shadow-2xl hover:scale-105 transform duration-300">
                        สำรวจเวิร์กช็อป
                    </a>
                    <a href="#free-classes" class="bg-black/30 backdrop-blur-md text-white border border-white/20 hover:bg-black/50 rounded-full px-8 py-3.5 font-semibold text-base transition w-full sm:w-auto shadow-2xl hover:scale-105 transform duration-300">
                        เข้าเรียนคลาสฟรี
                    </a>
                </div>
            </div>
        </section>'''

html = re.sub(hero_regex, new_hero, html, count=1)

with open('index.html', 'w') as f:
    f.write(html)
