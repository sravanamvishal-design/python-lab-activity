name = input("Enter student name: ")
marks = float(input("Enter aggregate marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

if marks >= 75 and attendance >= 75 and income <= 250000:
    print(name, "is eligible for scholarship")
else:
    print(name, "is not eligible for scholarship")