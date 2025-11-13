
pizza_bill = 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    pizza_bill = 15
elif size == "M":
    pizza_bill = 20
elif size == "L":
    pizza_bill = 25
else:
    print("size you entered is invalid")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":

    if size == "S":
        pizza_bill += 2
    else:
        pizza_bill += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    pizza_bill += 1

print(f"Your final bill is: ${pizza_bill}.")





