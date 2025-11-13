print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 or 15?"))
people = int(input("How many people to split the bill? "))

percentage_conversion= (tip / 100) * bill
print(f"each person should pay: {round((bill + percentage_conversion)/people,2)}")

