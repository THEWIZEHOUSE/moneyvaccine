import re

with open('index.html', 'r') as f:
    html = f.read()

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

# Use regex to find the end of the #free-classes section
html = re.sub(r'(<!-- Video / Course Cards Grid -->[\s\S]*?</div>\s*</div>\s*</div>\n\n\s*</div>)', r'\1' + cta_block, html)

with open('index.html', 'w') as f:
    f.write(html)
