import re

with open('index.html', 'r') as f:
    html = f.read()

testimonials_regex = r'<section id="testimonials"[\s\S]*?</section>'

new_testimonials = r'''<section id="testimonials" class="py-16 md:py-24 px-6 bg-white border-t border-black/5">
            <div class="max-w-4xl mx-auto">
                <div class="text-center max-w-2xl mx-auto mb-10">
                    <span class="text-xs font-semibold tracking-wider uppercase text-[#0071e3]">Real Experiences</span>
                    <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-gray-900 mt-2 mb-3">
                        เสียงตอบรับและบรรยากาศจริง
                    </h2>
                </div>

                <!-- Single Reel Video Embed -->
                <div class="max-w-[420px] mx-auto rounded-3xl overflow-hidden shadow-2xl border border-gray-100 bg-black aspect-[9/16] relative">
                    <iframe src="https://www.instagram.com/p/Db-mX1vS0fs/embed/" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full object-cover"></iframe>
                </div>
            </div>
        </section>'''

html = re.sub(testimonials_regex, new_testimonials, html, count=1)

with open('index.html', 'w') as f:
    f.write(html)
