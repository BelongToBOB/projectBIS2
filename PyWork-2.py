name = 'Wachirawit'
id = '269-2'
price = float(input("ราคาสินค้าที่ซื้อ ="))
quantity = int(input("จำนวนที่ซื้อ ="))
total = price*quantity
discount = total*0.02
net = total-discount
myFavoritesRelax = ['Akari','Dancin','Heat waves','What you know bout love','Beautiful girls']
menus = {"กะเพราะ":"50","ไก่ย่าง":"100","ข้าวผัด":"45","ข้าวต้ม":"30","หมูทอด":"60","คะน้าหมูกรอบ":"65","ข้าวมันไก่":"45"}
print("*******************")
print("รหัสลูกค้า:", id)
print("ชื่อลูกค้า:", name)
print("ราคาสินค้าที่ซื้อ:",price)
print("จำนวนที่ซื้อ:",quantity)
print("ยอดซื้อก่อนหักส่วนลด:", total)
print("ส่วนลด 20%:", discount)
print("ยอดเงินที่ต้องชำระหลังหักส่วนลด:", net)
print(myFavoritesRelax)
print("เเสดงรายชื่่อ:", menus)
print("*******************")
print("แสดงรายการในตัวแปร List myFavoriteRelax ที่สร้างขึ้นใน 2.3 เฉพาะรายการที่ 3:", myFavoritesRelax[2])
print("แสดงรายการในตัวแปร Dictionary ที่สร้างขึ้นใน 2.4 เฉพาะรายการที่ 2 ถึง 5",list(menus.items())[2:5])
print("*******************")
myFavoritesRelax.append("Bound2")
menus["ตัวที่เพิ่มรายการ1ตัว :->หมูกระทะ"] = 189
print("*******************")
print("เพิ่มรายการเข้าไปใน List และ Dictionary อย่างละ 1 รายการ:", myFavoritesRelax)
print("แสดงผลข้อมูลตัวแปร List และ Dictionary หลังการเพิ่มรายการ:", menus)
print("*******************")
