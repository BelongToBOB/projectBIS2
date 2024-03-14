con = "Y"
while con == "Y" or con == "y":
    watch = input("[T1=COROSPACE2],[T2=GarminForerunner45],[T3=GarminForerunner245],[T4=COROSAPEX],[T5=Sunto5]: ")
    color = input("[1=Black],[2=White],[3=Blackwhite],[4=Whitered]: ")
    sex = input("[1=Male],[2=Female]: ")
    con = input("ท่านต้องการป้อนข้อมูลคนถัดไปหรือไม่ [Y/N]? :")


con = False

while con == False:
    if watch == 'T1':
        model = "COROSPACE2"
        if sex == '1':
            gender = 'Male'
            price = 3000
        elif sex == '2':
            gender = 'Female'
            price = 2500
        con = True

    elif watch == 'T2':
        model = "GarminForerunner45"
        if sex == '1':
            gender = 'Male'
            price = 1000
        elif sex == '2':
            gender = 'Female'
            price = 1300
        con = True

    elif watch == 'T3':
        model = "GarminForerunner245"
        if sex == '1':
            gender = 'Male'
            price = 4500
        elif sex == '2':
            gender = 'Female'
            price = 5500
        con = True

    elif watch == 'T4':
        model = "COROSAPEX"
        if sex == '1':
            gender = 'Male'
            price = 6500
        elif sex == '2':
            gender = 'Female'
            price = 6000
        con = True

    elif watch == 'T5':
        model = "Sunto5"
        if sex == '1':
            gender = 'Male'
            price = 4000
        elif sex == '2':
            gender = 'Female'
            price = 3000
        con = True
        
    elif color == '1' or color == '2':
        if color == "1":
            discount = price*0.20
        elif color == "2":
            discount = price*0.20
        con = True
    elif color == '3' or color == '4':
        if color == "3":
            discount = price*0.10
        elif color == "4":
            discount = price*0.10
        con = True
    else:
        con == False 
        

print(watch)
print(gender)
print(price)
print("ส่วนลด".format(discount))
