distance = float(input("Enter distance in km: "))
age = int(input("Enter passenger age: "))
travel_class = input("Enter class (Sleeper/AC): ")

if distance <= 0 or age < 0:
    print("Invalid details")
else:
    if travel_class.lower() == "sleeper":
        fare = distance * 1
    elif travel_class.lower() == "ac":
        fare = distance * 2.5
    else:
        fare = 0
        print("Invalid travel class")

    if fare > 0:
        if age < 12:
            fare = fare * 0.5
        elif age >= 60:
            fare = fare * 0.8

        total = fare + 40
        print("Total railway fare: Rs.", total)