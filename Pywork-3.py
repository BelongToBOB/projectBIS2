eid=input("กรอกหมายเลขผู้ใช้ไฟฟ้า: ")
eName=input("กรอกชื่อผู้ใช้ไฟฟ้า: ")
lastUnit=float(input("ข้อมูลเลขมิเตอร์ไฟฟ้าของเดือนที่แล้ว: "))
currentUnit=float(input("ข้อมูลเลขมิเตอร์ไฟฟ้าของเดือนปัจจุบัน: "))
usedUnit=currentUnit-lastUnit
print("********************************************************************")


if lastUnit < currentUnit:
    if usedUnit<50:
        basePrice=usedUnit*5
    elif usedUnit<150:
        basePrice=(usedUnit*10)-250
    elif usedUnit<300:
        basePrice=(usedUnit*15)-(1000)
    else:
        basePrice=(usedUnit*20)-(2250+1000+250)
else:
    print("*มีข้อผิดพลาด_จบโปรแกรม*")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

ftPrice=usedUnit*0.5
vat=(basePrice+ftPrice)*0.07
totalPaid=basePrice+ftPrice+vat
print("********************************************************************")
print("{0:<50s}{1:>12,.2f} หน่วย".format("จํานวนหน่วยไฟฟ้าที่ใช้ไป: ",usedUnit))
print("{0:<48s}{1:>10,.2f} บาท".format("ค่าไฟฟ้าฐาน: ",basePrice))
print("{0:<47s}{1:>12,.2f} บาท".format("ค่าไฟฟ้าผันแปร: ",ftPrice))
print("{0:<49s}{1:>12,.2f} บาท".format("ภาษีมูลค่าเพิ่ม: ",vat))
print("{0:<52s}{1:>10,.2f} บาท".format("ค่าไฟฟ้ารวมทั้งสิ้น: ",totalPaid))
print("********************************************************************")