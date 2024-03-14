from Product import Product

com = Product("001", "Acer", "เครื่อง", "ใช้ประมวลผลข้อมูลในสำนักงาน", 35000.00, 10)
print("My Computer Info:", com.getInfo())
print("Total:", com.getTotal())
print("Discount:", com.getDiscount())
print("Net:", com.getNet())
print("Total:", com.getTotal())

car = Product("002", "Toyota", "คัน", "พาหนะในการเดินทางหรือขนส่ง", 980000.00, 1)
print("Car Info:", car.getInfo())
print("Total:", car.getTotal())
print("Discount:", car.getDiscount())
print("Net:", car.getNet())