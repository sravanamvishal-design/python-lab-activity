price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
category = input("Enter category (grocery/clothing/electronics): ")

subtotal = price * quantity

if subtotal >= 5000:
    discount = min(subtotal * 0.10, 1000)
else:
    discount = 0

amount = subtotal - discount

if category.lower() == "grocery":
    tax = amount * 0.05
elif category.lower() == "clothing":
    tax = amount * 0.12
else:
    tax = amount * 0.18

total = amount + tax

print("Subtotal: Rs.", subtotal)
print("Discount: Rs.", discount)
print("Tax: Rs.", tax)
print("Final Bill: Rs.", total)