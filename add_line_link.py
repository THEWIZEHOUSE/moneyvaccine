import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Replace the Free Classes LINE Banner CTA
old_line_cta = r'''                    <a href="#" class="inline-flex items-center justify-center bg-[#00B900] hover:bg-[#009900] text-white rounded-full px-8 py-4 font-semibold text-lg transition shadow-md relative z-10 w-full sm:w-auto">
                        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 24 24"><path d="M24 10.304c0-5.369-5.383-9.738-12-9.738-6.616 0-12 4.369-12 9.738 0 4.814 3.784 8.871 9.07 9.615.353.056.822.173 1.053.407.214.215.27.568.204.887l-.462 2.766c-.053.309.28.539.544.384 2.146-1.258 5.485-3.328 7.378-5.312 3.125-3.084 4.213-5.753 4.213-8.747z"/></svg>
                        แอดไลน์ @moneyvaccine
                    </a>
                    <p class="text-xs text-gray-400 mt-4 relative z-10">(เดี๋ยวทางเราจะมาอัปเดตลิงก์ Line OA ให้อีกที กดเตรียมไว้ก่อนได้เลย)</p>'''

new_line_cta = r'''                    <a href="https://page.line.me/278sxify" target="_blank" class="inline-flex items-center justify-center bg-[#00B900] hover:bg-[#009900] text-white rounded-full px-8 py-4 font-semibold text-lg transition shadow-lg relative z-10 w-full sm:w-auto transform hover:scale-105 duration-200">
                        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 24 24"><path d="M24 10.304c0-5.369-5.383-9.738-12-9.738-6.616 0-12 4.369-12 9.738 0 4.814 3.784 8.871 9.07 9.615.353.056.822.173 1.053.407.214.215.27.568.204.887l-.462 2.766c-.053.309.28.539.544.384 2.146-1.258 5.485-3.328 7.378-5.312 3.125-3.084 4.213-5.753 4.213-8.747z"/></svg>
                        แอดไลน์สอบถาม / รับคลาสฟรี
                    </a>'''

html = html.replace(old_line_cta, new_line_cta)

# 2. Add Floating LINE Button at the bottom right corner of the screen
floating_line_button = r'''
    <!-- Floating LINE OA Button -->
    <a href="https://page.line.me/278sxify" target="_blank" class="fixed bottom-6 right-6 z-50 bg-[#00B900] hover:bg-[#009900] text-white rounded-full p-3.5 shadow-2xl flex items-center justify-center group transition-all duration-300 hover:scale-110 border-2 border-white">
        <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24"><path d="M24 10.304c0-5.369-5.383-9.738-12-9.738-6.616 0-12 4.369-12 9.738 0 4.814 3.784 8.871 9.07 9.615.353.056.822.173 1.053.407.214.215.27.568.204.887l-.462 2.766c-.053.309.28.539.544.384 2.146-1.258 5.485-3.328 7.378-5.312 3.125-3.084 4.213-5.753 4.213-8.747z"/></svg>
        <span class="max-w-0 overflow-hidden whitespace-nowrap group-hover:max-w-xs transition-all duration-500 ease-in-out font-medium text-sm pl-0 group-hover:pl-2">
            สอบถามทาง LINE
        </span>
    </a>
</body>'''

html = html.replace('</body>', floating_line_button)

# 3. Add LINE link in footer
html = html.replace(
    '<a href="mailto:contact@moneyvaccine.co" class="hover:text-gray-900 transition">ติดต่อเรา</a>',
    '<a href="https://page.line.me/278sxify" target="_blank" class="hover:text-gray-900 transition text-[#00B900] font-semibold">LINE OA (@278sxify)</a>'
)

with open('index.html', 'w') as f:
    f.write(html)
