import re

with open('index.html', 'r') as f:
    html = f.read()

old_btn = r'''                            <button onclick="openModal('Cashflow Club Thailand', '฿3,990')" class="w-full bg-white text-black hover:bg-gray-100 rounded-full py-3.5 font-semibold text-base transition-all duration-200 hover:shadow-lg">
                                ลงทะเบียนจองรอบถัดไป
                            </button>'''

new_link = r'''                            <a href="https://go.thewizehouse.com/register/95e2b713-1ec8-47f9-850b-869293e16a26?invitedby=moneyvaccine" target="_blank" class="w-full bg-white text-black hover:bg-gray-100 rounded-full py-3.5 font-semibold text-base transition-all duration-200 hover:shadow-lg flex justify-center">
                                ลงทะเบียนจองรอบถัดไป
                            </a>'''

html = html.replace(old_btn, new_link)

with open('index.html', 'w') as f:
    f.write(html)
