employee = "นายวชิรวิทย์ ศรีสูงเนิน"
status = "นักศึกษา"
department = "BIS2N1"
salary = float(input("เงินเดือน = "))
allowance = float(input("เงินเดือนประจำตำแหน่ง = "))
bonus = salary * 3
incomes = ((salary + allowance)*12)+bonus
tax = incomes * 0.05
print("------------------------------")
print("ชื่อ = ", employee)
print("ตำแหน่ง = ", status)
print("แผนก = ", department)
print("เงินเดือน = ", salary)
print("เงินเดือนประจำแหน่ง = ", allowance)
print("โบนัส = ", bonus)
print("ค่ารายได้ทั้งปี = ", incomes)
print("ภาษีที่ต้องชำระ = ", tax)
print("------------------------------")

