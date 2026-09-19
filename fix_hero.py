import re

with open('index.html', 'r') as f:
    html = f.read()

hero_img = r'''            </div>

            <!-- Hero Image -->
            <div class="mt-16 w-full max-w-5xl mx-auto rounded-[2rem] overflow-hidden relative shadow-2xl border border-gray-100 group">
                <img src="./hero-bg.png" alt="Money Vaccine Seminar" class="w-full h-auto object-cover max-h-[60vh] object-top group-hover:scale-105 transition duration-700 ease-out">
            </div>

            <!-- Stats / Social Proof Strip -->'''

html = html.replace('            </div>\n\n            <!-- Stats / Social Proof Strip -->', hero_img)

with open('index.html', 'w') as f:
    f.write(html)
