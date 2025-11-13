
'''
The errors or human errors sometimes in Inevitable
That's why we should have contingency plan to do when
errors happen.
'''

#FileNotFound
#with open("a_file.txt") as file:
#file.read()

#KeyError
#a_dictionary = {"key": "value"}
#value = a_dictionary["non_existent_key"]

#IndexError
#fruit_list = ["Apple", "Banana", "Pearl"]

#TypeError
#text = "abc"
#print(text + 5)
#---------------------------------------------------------------

#try - Something that might cause an exception
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdasd"])
#except - Do this if there was an exception
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
#else -do this if there were no exceptions
else:
    content = file.read()
    print("Fle was closed.")
#-finally - Do this no matter what happens
finally:
    file.close()
    print("File was closed.")

#Raising your own exception(you are in control of declaring an exception)

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters. you are not Godzilla haha!")

bmi = weight / height ** 2
print(bmi)