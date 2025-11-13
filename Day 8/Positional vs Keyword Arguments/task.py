# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

#Function with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# greet_with("Angelo", "Philippines")
#
# greet_with("Elon Musk", "America")

#Key word argument , the position doesn't matter because we have keyword

greet_with(location = "Bicol", name = "Buboy")