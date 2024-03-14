print("Welcome to my practice looping program")
sales = {}
commissions = []
con = "Y"

while con == "Y" or con == "y":
    name = input("Enter sale name:")
    sale = float(input("Enter your sale: "))
    sales[name] = sale
    con = input("ท่านต้องการป้อนข้อมูลคนถัดไปหรือไม่ [Y/N]? :")

for key in sales:
    if sales[key] <= 10000:
        comm = sales[key] * 0.05
    elif sales[key] <= 30000:
        comm = sales[key] * 0.10
    else:
        comm = sales[key] * 0.15
    commissions.append(comm)

i = 0
print("********************* Output ********************")
print("{0:>20s} {1:>10s} {2:>10s}".format("Employee",
"Sale", "Commission"))
totalSale = 0.00
totalComm = 0.00
for empName in sales:
    print("{0:>20s} {1:>13,.2f}{2:>13,.2f}"
        .format(empName, sales[empName], commissions[i]))
    totalSale += sales[empName]
    totalComm += commissions[i]
    i += 1
print("*************************************************")
print("Total sale: {0:,.2f} ,Total commission: {1:,.2f}".format(totalSale, totalComm))