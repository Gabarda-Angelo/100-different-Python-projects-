import random
#Dictionary comprehension
#Syntax: new_dict = {new_key: new_value for item in list}

#new_dict = {new_key:new_value for (key,value) in dict.items()}

#Conditional Dictionary Comprehension
#Syntax: new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex","Beth","Dave","Elanor","Freddie"]
student_grades = {name : random.randint(1,100) for name in names}

passed_students = {key:value for (key, value) in student_grades.items() if value > 75}

print(passed_students)