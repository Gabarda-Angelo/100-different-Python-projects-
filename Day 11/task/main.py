from art import logo
import random

def dealt_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    score = sum(cards)

    return score

def compare_score(u_score, c_score):

    if u_score == c_score:
        return "it's a draw"
    elif c_score == 0:
        return "you lose! computer wins got a blackjack"
    elif u_score == 0:
        return "you win got a blackjack! computer lose"
    elif u_score > 21:
        return "you lose over 21"
    elif c_score > 21:
        return "you win! computer has over 21 score!"
    else:
        if u_score > c_score:
            return "you win! your score is higher than computer score!"
        elif c_score > u_score:
            return "you lose! computer is higher than your score!"




def play_blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    game_over = False

    for iterator in range(2):
        user_cards.append(dealt_cards())
        computer_cards.append(dealt_cards())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards},current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or  computer_score == 0 or user_score > 21:
            game_over = True
        else:
            get_card = input("Type 'y', to get another card, type 'n' to pass:").lower()
            if get_card == "y":
                user_cards.append(dealt_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealt_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} total score: {user_score}")
    print(f"Computer final hand: {computer_cards} total score: {computer_score}")

    print(compare_score(user_score, computer_score))



while input("Do you want to play BlackJack? 'y' or 'n':").lower() == "y":
    print("\n" * 20)
    play_blackjack()
