import csv
import MySQLdb
from dbConf import DBDesc
import pandas as pd


filename = "tbopendata.csv"
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    data = list(reader)

myDb = DBDesc()
myConn = MySQLdb.connect(host=myDb.getHost(), user=myDb.getUser(), password=myDb.getPassword(), database=myDb.getDatabase())
mycursor = myConn.cursor()


def save_to_db(data):
    try:
        myConn = MySQLdb.connect(
            host="localhost",
            user="dbtstaff692",
            password="1234",
            database="classicmodels"
        )
        mycursor = myConn.cursor()

        colindex = [0, 1, 2, 3, 4]  
        df = pd.read_csv("tbopendata.csv", usecols=colindex)

        for (_, datarow) in df.iterrows():
            id, EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL = datarow.iloc[0], datarow.iloc[1], datarow.iloc[2], datarow.iloc[3], datarow.iloc[4]
            values = tuple(None if pd.isna(val) else val for val in (id, EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL))
            strsql = "INSERT INTO tbopendata(id, EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(strsql, values)

        myConn.commit()
        print("Data inserted successfully...")
    except Exception as e:
        print("Error:", e)
    finally:
        myConn.close()

save_to_db("tbopendata.csv")
def show_data():
    strsql = "SELECT * FROM tbopendata"
    mycursor.execute(strsql)
    myResult = mycursor.fetchall()

    for row in myResult:
        print(row)

def clear_data():
    strsql = "DELETE FROM tbopendata"
    mycursor.execute(strsql)

    myConn.commit()


while True:
    print("""
    L: โหลดข้อมูลจากไฟล์ CSV
    D: แสดงข้อมูล
    C: ลบข้อมูล
    E: ออกจากโปรแกรม
    """)

    choice = input("เลือกเมนู (L/D/C/E): ")

    if choice not in ("L", "D", "C", "E"):
        print("* ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่ *")
        continue

    if choice == "L":
        save_to_db(data)
        print("บันทึกข้อมูลเรียบร้อย")

    elif choice == "D":
        show_data()

    elif choice == "C":
        clear_data()
        print("ลบข้อมูลเรียบร้อย")

    elif choice == "E":
        print("จบการทำงาน...")
        break

myConn.close()