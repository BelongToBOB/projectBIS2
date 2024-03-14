def getAllowance(job_position):
    
    if job_position == "ceo":
        allowance = 20000
    elif job_position == "md":
        allowance = 10000
    elif job_position == "supervisor":
        allowance = 5000
    else:
        allowance = 0  
    return allowance

def getBonus(job_position,salary,work_age):

    if job_position in ["ceo","md","supervisor"]:
        if work_age < 5:
            bonus = salary*2
        elif work_age <= 10:
            bonus = salary*3
        else:
            bonus = salary*5
    else:
        if work_age < 3:
            bonus = salary*1
        elif work_age <= 5:
            bonus = salary*2
        elif work_age <= 10:
            bonus = salary*3
        else:
            bonus = salary*4
    return bonus
print("*****************ข้อมูลพนักงาน*********************")
employee_id = input("รหัสพนักงาน: ")
employee_name = input("ชื่อพนักงาน: ")
salary = float(input("เงินเดือน: "))
position = input("ตำแหน่ง: ")
work_age = int(input("อายุงาน: "))
print("*****************ข้อมูลพนักงาน*********************")
if employee_id == "ceo":
    emp = "CEO"
elif employee_id == "md":
    emp = "MB"
elif employee_id  == "supervisor":
    emp = "Supervisor"
else:
    emp = "employee"  
    
print("************************เงินเดือน**************************")
position_allowance = getAllowance(position)
print("เงินประจำตำแหน่ง", position_allowance)

bonus = getBonus(position, salary, work_age)
print("เงินโบนัส:", bonus)

total_salary = salary + position_allowance + bonus
print("เงินรวมที่จะได้รับ:", total_salary)
print("************************เงินเดือน**************************")