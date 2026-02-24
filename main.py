import core

print("=== 💧 เติมน้ำให้ร่างกาย: เครื่องคำนวณปริมาณน้ำดื่ม 💧 ===")
print(f"Engine Version: {core.get_version()}")
print("-" * 55)

# รับค่าจากผู้ใช้ (ใช้ float และ int เพื่อแปลงข้อความเป็นตัวเลข)
print("กรุณากรอกข้อมูลของคุณเพื่อให้ระบบคำนวณ...")
try:
    user_weight = float(input("น้ำหนักตัวของคุณ (กิโลกรัม) : "))
    user_exercise = int(input("วันนี้คุณออกกำลังกายกี่นาที? (ถ้าไม่ออกให้ใส่ 0) : "))
    
    # ส่งตัวเลขไปให้ Engine ประมวลผล
    result = core.calculate_water(user_weight, user_exercise)
    
    # แสดงผลลัพธ์
    print("\n✨ --- ผลการวิเคราะห์ --- ✨")
    print(result)
    print("----------------------------")
    print("อย่าลืมจิบน้ำเรื่อยๆ ตลอดทั้งวันนะครับ! 😊")

except ValueError:
    # ดักจับ error กรณีผู้ใช้พิมพ์ตัวหนังสือแทนที่จะเป็นตัวเลข
    print("\n❌ Error: กรุณาพิมพ์เป็นตัวเลขเท่านั้นนะครับ!")