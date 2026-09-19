import re

with open('index.html', 'r') as f:
    html = f.read()

beam_card = """
                <!-- Card 3: Beam Mentoring (Full Width Apple Style) -->
                <div class="mt-8 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-3xl p-8 sm:p-12 shadow-appleCard hover:shadow-appleCardHover transition-all duration-300 border border-blue-100 relative overflow-hidden group flex flex-col md:flex-row items-center gap-10">
                    
                    <div class="w-full md:w-5/12 aspect-square md:aspect-auto md:h-80 rounded-2xl overflow-hidden relative shadow-md border border-white/50 bg-white flex items-center justify-center">
                        <!-- Placeholder for Beam Mentoring Image -->
                        <div class="absolute inset-0 opacity-20 bg-[radial-gradient(#3b82f6_1px,transparent_1px)] [background-size:16px_16px]"></div>
                        <div class="text-center z-10 p-6">
                            <div class="w-20 h-20 mx-auto bg-blue-600 rounded-full flex items-center justify-center text-white mb-4 shadow-lg">
                                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                            </div>
                            <h4 class="text-xl font-bold text-gray-900">Beam Mentoring</h4>
                            <p class="text-sm text-gray-500 mt-2">พื้นที่สำหรับใส่รูป หรือคลิปของคุณบีม</p>
                        </div>
                    </div>

                    <div class="w-full md:w-7/12 flex flex-col justify-center">
                        <span class="text-xs font-bold text-[#0071e3] tracking-widest uppercase mb-3 block">Exclusive 1-on-1</span>
                        <h3 class="text-3xl sm:text-4xl font-bold tracking-tight text-gray-900 mb-4">
                            Beam Mentoring
                        </h3>
                        <p class="text-gray-600 text-base sm:text-lg mb-6 leading-relaxed">
                            ปลดล็อกศักยภาพและวางแผนการเงินแบบเจาะลึกเฉพาะบุคคล (1-on-1) กับคุณบีม 
                            ช่วยคุณออกแบบชีวิต จัดการความเสี่ยง และสร้างพอร์ตที่ตอบโจทย์เป้าหมายระยะยาวของคุณอย่างแท้จริง
                        </p>

                        <div class="grid grid-cols-2 gap-4 mb-8">
                            <div class="flex items-start gap-3">
                                <svg class="w-5 h-5 text-[#0071e3] mt-0.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                                <span class="text-sm text-gray-700">ที่ปรึกษาส่วนตัว</span>
                            </div>
                            <div class="flex items-start gap-3">
                                <svg class="w-5 h-5 text-[#0071e3] mt-0.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                                <span class="text-sm text-gray-700">วิเคราะห์เชิงลึก</span>
                            </div>
                            <div class="flex items-start gap-3">
                                <svg class="w-5 h-5 text-[#0071e3] mt-0.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                                <span class="text-sm text-gray-700">แผนการเงินเฉพาะคุณ</span>
                            </div>
                            <div class="flex items-start gap-3">
                                <svg class="w-5 h-5 text-[#0071e3] mt-0.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                                <span class="text-sm text-gray-700">ติดตามผลต่อเนื่อง</span>
                            </div>
                        </div>

                        <div class="flex flex-col sm:flex-row items-center gap-4">
                            <button onclick="openModal('Beam Mentoring')" class="apple-btn w-full sm:w-auto px-8 py-3.5 text-base font-medium">
                                สอบถามคิวว่าง
                            </button>
                            <span class="text-xs text-gray-400 font-medium">รับจำนวนจำกัดต่อเดือน</span>
                        </div>
                    </div>
                </div>
"""

# Insert right after the Workshops Grid closes
html = re.sub(
    r'(</button>\n\s*</div>\n\s*</div>\n\n\s*</div>)',
    r'\1\n' + beam_card,
    html
)

# Update Modal options to include Beam Mentoring
html = re.sub(
    r'<option value="Cashflow Club Thailand">Cashflow Club Thailand \(฿3,990\)</option>',
    r'<option value="Cashflow Club Thailand">Cashflow Club Thailand (฿3,990)</option>\n                        <option value="Beam Mentoring">Beam Mentoring (1-on-1)</option>',
    html
)

with open('index.html', 'w') as f:
    f.write(html)
