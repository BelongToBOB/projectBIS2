studyList = []
gradeDic = {}
con = "Y"

while con == "Y" or con == "y":
    subcode = int(input("รหัสวิชา: "))
    subname = input("ชื่อวิชา: ")
    gradecre = float(input("หน่วยกิต: "))
    gradecar = input("เกรดตัวอักษร: ")

    subject_data = [subcode, subname, gradecre, gradecar]
    studyList.append(subject_data)
    con = input("มีวิชาเรียนวิชาอื่นอีกหรือไม่ (Y/N): ")

print("ผลการเรียน(Study List):")
for subject_data in studyList:
    print(subject_data)

for subject_data in studyList:
    subcode = subject_data[0]
    gradecar = subject_data[3]
    
    if gradecar == 'A':
        numGrade = 4
    elif gradecar == 'B+':
        numGrade = 3.5
    elif gradecar == 'B':
        numGrade = 3
    elif gradecar == 'C+':
        numGrade = 2.5
    elif gradecar == 'C':
        numGrade = 2
    elif gradecar == 'D+':
        numGrade = 1.5
    elif gradecar == 'D':
        numGrade = 1
    elif gradecar == 'F':
        numGrade = 0
    else:
        numGrade = None
    
    GP = gradecre * numGrade
    subject_data.extend([numGrade, GP])

    gradeDic[subcode] = gradecar

print("ผลการเรียนหลังประมวลผล(studyList):")
for subject_data in studyList:
    print(subject_data)

print("รหัสวิชาและเกรด(gradeDic):")
print(gradeDic)

CGX = 0
CCX = 0

 
for subject_data in studyList:
        credit = subject_data[2]
        GP = subject_data[5]

        CCX += credit
        CGX += GP

print("ผลคูณหน่วยกิตกับเกรดสะสม(CGX):", CGX)
print("หน่วยกิตสะสม(CCX):", CCX)

GPA = CGX / CCX
print("เกรดเฉลี่ยสะสม(GPA): ", GPA)
