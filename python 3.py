consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))
age = int(input("Enter patient age: "))

total = consultation + diagnostic + treatment

if age >= 60:
    total = total - (consultation + treatment) * 0.10

print("Total hospital bill: Rs.", total)

if total <= 0:
    print("Invalid bill")
else:
    print("Patient billing processed")