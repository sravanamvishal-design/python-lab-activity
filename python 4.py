basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentive = float(input("Enter incentive: "))

gross = basic + allowance + overtime + incentive

if gross <= 10000:
    deduction = 0
elif gross <= 20000:
    deduction = (gross - 10000) * 0.05
else:
    deduction = 500 + (gross - 20000) * 0.10

net = gross - deduction

print("Gross Salary: Rs.", gross)
print("Deduction: Rs.", deduction)
print("Net Salary: Rs.", net)