credit = int(input("โปรดระบุหน่วยกิตสะสม: "))
gpa = float(input("โปรดระบุเกรดเฉลี่ยสะสม: "))
if credit < 30:
    status = "ปกติ"
elif credit < 60:
    if gpa < 1.50:
        status = "ตกออก"
    else:
        status = "ปกติ"
elif credit < 127:
    if gpa < 1.75:
        status = "ตกออก"
    else:
        status = "ปกติ"
elif credit >= 127:
    if gpa <= 1.90:
        status = "ตกออก"
    elif gpa >= 1.99:
        status = "รอพินิจ"
    else:
        status = "สำเร็จการศึกษา"
else:
    print("none")

print("หน่วยกิต: ",credit)
print("เกรดเฉลี่ยสะสม: ",gpa)
print("สถานะ: ",status)    