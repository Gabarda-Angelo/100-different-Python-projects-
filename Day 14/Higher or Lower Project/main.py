import random
from art import logo, vs
from game_data import data


def correct_answer(a_insta_info, b_insta_info, ans):

    if ans == 'A':
        if a_insta_info['follower_count'] > b_insta_info['follower_count']:
            return "A"
        else:
            return "wrong"
    elif ans == 'B':
        if b_insta_info['follower_count'] > a_insta_info['follower_count']:
            return "B"
        else:
            return "wrong"




def game():
    score = 0
    a_instagram_info = random.choice(data)
    b_instagram_info = random.choice(data)
    game_over = False
    print(logo)
    while not game_over:
        # generate randomize the first TWO lists in the dictionary.


        # generate randomize the first TWO instagram info lists in the dictionary.
        print(f"Compare A: {a_instagram_info['name']}, {a_instagram_info['description']},"
              f"{a_instagram_info['country']}")

        print(vs)
        print(f"Against B: {b_instagram_info['name']}, {b_instagram_info['description']},"
              f"{b_instagram_info['country']}")
        #  answer the question Type 'A' or 'B'
        answer = input("who has more followers? Type 'A' or 'B':")

        # create a function that will compare which one has the highest followers
        #    and return +1 if its correct and return 0 if its wrong


        #store into the compare A variable, the winner sentence should be always store in the a_instagram_info
        if correct_answer(a_instagram_info, b_instagram_info, answer).lower() == "b":
            a_instagram_info = b_instagram_info
            b_instagram_info = random.choice(data)
            score += 1
            print("\n" * 20)
            print(logo)
            print(f"Score: {score}")
        elif correct_answer(a_instagram_info, b_instagram_info, answer).lower() == "a":
            b_instagram_info = random.choice(data)
            score += 1
            print("\n" * 20)
            print(logo)
            print(f"Score: {score}")
        elif correct_answer(a_instagram_info, b_instagram_info, answer).lower() == "wrong":
            print("\n" * 20)
            print(logo)
            print(f"Wrong! Game over sorry! your score: {score}")
            game_over = True







game()