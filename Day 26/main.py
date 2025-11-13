

#using list comprehension, syntax: new_list [new_item for item in list]
numbers = [1,2,3]


new_numbers = [n + 1 for n in numbers]

print(new_numbers)
#2, 3 ,4

#get each letter
name = "Angela"
new_name  = [letter for letter in name]

print(new_name)

#double the value from the range

double_value = [n*2 for n in range(1,5)]
print(double_value)

#conditional list comprehension, syntax: new_list = [new_item for item in list if test]
names = ["Alex","Beth","Dave","Elanor","Freddie"]

short_names = [name for name in names if len(name) < 5 ]

#Challenge: make all caps the name that has more than 5 letters

longer_names = [long_name.upper() for long_name in names if len(long_name) > 5]

print(longer_names)