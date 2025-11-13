from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(operations["*"](4,8))
# print(operations)


first_number = None
while True:

    if  first_number is None:
        print(logo)
        first_number = float(input("First number: "))
    for operator in operations:
        print(operator)
    operation_choose = input("Pick an operation: ")
    second_number = float(input("What is the next number?: "))

    result = operations[operation_choose](first_number, second_number)

    print(f"{first_number} {operation_choose} {second_number} = {result}")

    new_calculation_choice = input("Type 'y' to continue calculating with 12.0, or type "
                            "'n' to start a new calculation:")

    if new_calculation_choice == "n":
        first_number = None
        print("\n" * 20)
    elif new_calculation_choice == "y":
        first_number = result



