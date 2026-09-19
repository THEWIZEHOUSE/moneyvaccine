import re

with open('index.html', 'r') as f:
    html = f.read()

# Remove 🎁 รวม: อุปกรณ์กิจกรรม...
html = re.sub(
    r'\s*<div class="flex items-center gap-2\.5">\s*<span class="text-gray-400">🎁</span>\s*<span><strong>รวม:</strong> อุปกรณ์กิจกรรม, เอกสารสรุป และเครื่องดื่ม</span>\s*</div>',
    '',
    html
)

# Remove ✨ สิทธิพิเศษ: สมาชิกคอมมูนิตี้...
html = re.sub(
    r'\s*<div class="flex items-center gap-2\.5">\s*<span class="text-gray-400">✨</span>\s*<span><strong>สิทธิพิเศษ:</strong> สมาชิกคอมมูนิตี้แลกเปลี่ยนไอเดียรายเดือน</span>\s*</div>',
    '',
    html
)

with open('index.html', 'w') as f:
    f.write(html)
