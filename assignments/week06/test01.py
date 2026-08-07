#เขียน fuunction ชื่อ calculate_sphere(radius)
#คำนวณหา ปริมาตร ของทรงกลม volumn = 4.0 / 3* pi * radius ** 3
#จากนั้นแสดงผลลัพธ์ที่เหมาะสมออกทางหน้าจอ
#ไม่ลืมที่จะเขียนโปรแกรมในส่วนของการทดสอบการใช้งาน


def calculate_sphere(radius):
    pi = 3.14159  
    volume = 4.0 / 3 * pi * radius ** 3
    print(f"Sphere with radius {radius}")
    print(f"Volume = {volume}")
    print()

calculate_sphere(5)
calculate_sphere(10)