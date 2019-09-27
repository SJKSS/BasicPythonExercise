#สร้างฟังก์ชัน hello
def hello(name):
    print('Hello %s'% name)

#เริ่มฟังก์ชัน
hello('kiki')

#สร้างฟังก์ชันที่มีการ return ค่า Area
def Area(width=5,height=6):
    c=width*height
    return c
#เรียกใช้ฟังก์ชัน Area
print(Area())