import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


# print(random.choice(friends))

#option 2

random_choice = random.randint(0,4)
print(friends[random_choice])