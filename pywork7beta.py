import MySQLdb
from dbConf import DBDesc

def main_menu():
    print("********** Main Menu **********")
    print("1. สินค้าที่มีราคาขายตั้งแต่ 20-80 บาท")
    print("2. Trains and Motorcycles")
    print("3. ข้อมูลสินค้าที่ไม่ปรากฎในใบสั่งซื้อ ")
    print("4. ยอดขายสินค้าแยกตามใบสั่งซื้อ ")
    print("5. รายการสั่งซื้อตามหมายเลขใบสั่งซื้อที่ระบุ")
    print("6. ออกจากโปรแกรม")

def menu_1():
    strsql = "SELECT productCode, productName, productLine, productVendor, buyPrice FROM products WHERE buyPrice BETWEEN 20 AND 80"
    myCursor.execute(strsql)
    myResult = myCursor.fetchall()
    print("********** สินค้าที่มีราคาขายตั้งแต่ 20-80 บาท ***********")
    for data in myResult:
        print("{0:<10s} {1:45s} {2:20s} {3:40s} {4:10f}".format(data[0], data[1], data[2], data[3], data[4]))

def menu_2():
    strsql = "SELECT productCode, productName, productLine, quantityInStock, buyPrice FROM products WHERE productLine IN ('Trains', 'Motorcycles')"
    myCursor.execute(strsql)
    myResult = myCursor.fetchall()
    print("********** Trains and Motorcycles ***********")
    for data in myResult:
        print("{0:<10s} {1:40s} {2:20s} {3:10d} {4:20f}".format(data[0], data[1], data[2], data[3], data[4]))

def menu_3():
    strsql = "SELECT p.productCode, p.productName, p.productLine, p.buyPrice "\
             "FROM products p "\
             "LEFT JOIN orderdetails o ON p.productCode = o.productCode "\
             "WHERE o.orderNumber IS NULL"
    myCursor.execute(strsql)
    myResult = myCursor.fetchall()
    print("********** ข้อมูลสินค้าที่ไม่ปรากฎในใบสั่งซื้อ ***********")
    for data in myResult:
        print("{0:<10s} {1:40s} {2:20s} {3:20s} {4:20f}".format(data[0], data[1], data[2], "N/A", data[3]))

def menu_4():
    strsql = "SELECT orderdetails.orderNumber, orders.orderDate, SUM(orderdetails.priceEach * orderdetails.quantityOrdered) as total "\
             "FROM orders "\
             "JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber "\
             "GROUP BY orderdetails.orderNumber, orders.orderDate"
    myCursor.execute(strsql)
    myResult = myCursor.fetchall()
    print("********** ยอดขายสินค้าแยกตามใบสั่งซื้อ ***********")
    for data in myResult:
        print("{0:<10d} {1} {2:20f}".format(data[0], data[1], data[2]))

def menu_5():
    order_number_input = input("ใส่หมายเลขใบสั่งซื้อ: ")
    try:
        myDb = DBDesc()
        myConn = MySQLdb.connect(host=myDb.getHost(), user=myDb.getUser(), password=myDb.getPassword(), database=myDb.getDatabase())
        myCursor = myConn.cursor()

        strsql = "SELECT o.orderNumber, o.orderDate, c.customerName, od.productCode, p.productName, od.priceEach, od.quantityOrdered, (od.priceEach * od.quantityOrdered) AS total "
        strsql += "FROM orders o "
        strsql += "JOIN customers c ON o.customerNumber = c.customerNumber "
        strsql += "JOIN orderdetails od ON o.orderNumber = od.orderNumber "
        strsql += "JOIN products p ON od.productCode = p.productCode "
        strsql += "WHERE o.orderNumber = %s"

        myCursor.execute(strsql, (order_number_input,))
        order_info = myCursor.fetchall()

        if order_info:
            order_number, order_date, customer_info = order_info[0][0], order_info[0][1], order_info[0][2]
            order_items = [(item[3], item[4], item[5], item[6], item[7]) for item in order_info]

            total_items = sum(item[3] for item in order_items)
            total_amount = sum(item[4] for item in order_items)

            print("********** ใบเสร็จรับเงิน **********")
            print("หมายเลขใบสั่งซื้อ: {}".format(order_number))
            print("วันที่สั่งซื้อ: {}".format(order_date))
            print("ข้อมูลลูกค้า: {}".format(customer_info))

            print("\n{:<20} {:<45} {:<20} {:<15} {:<15}".format("รหัสสินค้า", "ชื่อสินค้า", "ราคาต่อหน่วย", "จำนวน", "เป็นเงิน"))
            for item in order_items:
                print("{:<17} {:<41} {:<18} {:<15} {:<15}".format(item[0], item[1], item[2], item[3], item[4]))

            print("\nจำนวนรายการที่สั่งซื้อ: {}".format(total_items))
            print("รวมเป็นเงินทั้งสิ้น: {:.2f}".format(total_amount))
        else:
            print("ไม่พบข้อมูลใบสั่งซื้อที่ระบุ")

    except Exception as e:
        print("เกิดข้อผิดพลาด: {}".format(e))
    finally:
        myConn.close()


try:
    myDb = DBDesc()
    with MySQLdb.connect(host=myDb.getHost(), user=myDb.getUser(), password=myDb.getPassword(), database=myDb.getDatabase()) as myConn:
        myCursor = myConn.cursor()

        while True:
            main_menu()
            choice = input("ตัวเลือกของคุณคือ: ")

            if choice == '1':
                menu_1()
            elif choice == '2':
                menu_2()
            elif choice == '3':
                menu_3()
            elif choice == '4':
                menu_4()
            elif choice == '5':
                menu_5()
            elif choice == '6':
                print("**********ออกจากโปรแกรม**********")
                break  
            else:
                print("เลือกไม่ถูกต้อง กรอกตัวเลขระหว่าง 1 ถึง 6.")

except Exception as e:
    print("เกิดข้อผิดพลาด: {}".format(e))

