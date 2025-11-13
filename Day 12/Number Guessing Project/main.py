from art import logo
import random

EASY_TURNS = 5
HARD_TURNS = 10

def guess_answer(guess_answer, real_answer, num_of_attempts):

    if guess_answer == real_answer:
        print(f"Correct! Gotcha! {real_answer} is the correct answer!")
        return 777

    if guess_answer > real_answer:
        num_of_attempts -= 1
        print("Too High! guess again")
        return num_of_attempts
    elif guess_answer < real_answer:
        num_of_attempts -= 1
        print("Too Low! guess again")
        return num_of_attempts


def difficulty():
    chose_difficulty = input("Choose a difficulty level (easy or hard): ").lower()

    if chose_difficulty == "easy":
        return EASY_TURNS
    elif chose_difficulty == "hard":
        return HARD_TURNS





random_number = random.randint(1, 100)



print(logo)
print("Welcome to Number guessing Game!")
print(f"correct random number is {random_number}")
attempts = difficulty()

while attempts != 0 and attempts != 777:
    print(f"you have {attempts} attempts remaining. to guess the number")
    guess = int(input("Make a guess:"))

    attempts = guess_answer(guess, random_number, attempts)

    if attempts == 0:
        print(f"you lose sorry! you didn't guessed correctly {attempts} remaining attempts")



