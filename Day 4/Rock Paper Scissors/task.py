import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))



rps_shapes = [rock, paper, scissors]
rps_shape_in_word = ["rock", "paper", "scissors"]

computer_choice = random.randint(0,2)

if human_choice >= 0 and human_choice <= 2:
    print(f"you choose:{rps_shape_in_word[human_choice]}\n" + rps_shapes[human_choice])


if computer_choice == 0:
    print(f"Computer chose Rock\n{rps_shapes[0]}")
elif computer_choice == 1:
    print(f"Computer chose Paper\n{rps_shapes[1]}")
elif computer_choice == 2:
    print(f"Computer chose Scissors\n{rps_shapes[2]}")

result = (human_choice == 0 and computer_choice == 2) or (human_choice == 2 and computer_choice == 1) or (human_choice == 1 and computer_choice == 0)

if result == True:
    print("You win!")
elif human_choice == computer_choice:
    print("DRAW!")
else:
    print("Computer wins!")


