usage = float(input("Enter data usage in GB: "))
budget = float(input("Enter your budget: "))

basic = 249 + max(0, usage - 8) * 20
smart = 399 + max(0, usage - 15) * 15
premium = 499 + max(0, usage - 25) * 10

print("Basic Plan: Rs.", basic)
print("Smart Plan: Rs.", smart)
print("Premium Plan: Rs.", premium)

plans = [("Basic", basic), ("Smart", smart),
         ("Premium", premium)]

eligible = [p for p in plans if p[1] <= budget]

if eligible:
    print("Best plan:", min(eligible, key=lambda p: p[1]))
else:
    print("No plan within budget")