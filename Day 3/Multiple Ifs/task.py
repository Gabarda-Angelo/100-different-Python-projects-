print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("ticket cost $5.")
    elif age <= 18:
        bill = 7
        print("ticket cost $7.")
    else:
        bill = 12
        print("ticket cost $12.")
    wants_photo = input("do you want to take a photo? type y for Yes or n for No")
    if wants_photo == "y":
        bill += 3

    print(f"Your total bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
