from art import logo

# TODO-1: Ask the user for input
bidder = {}
add_bidder = True


def find_the_highest_bid(bidding_information):
    # TODO-4: Compare bids in dictionary
    highest_bidder = ""
    highest_bid = 0
    for name in bidding_information:
        if bidder[name] > highest_bid:
            highest_bid = bidding_information[name]
            highest_bidder = name

    print(f"highest bidder: {highest_bidder} is winner, bid: {highest_bid}")
    # highest_bidder_usingmax = max(bidding_information, key=bidding_information.get)
    # print(highest_bidder_usingmax)
    # print(bidding_information[highest_bidder_usingmax])

while add_bidder:
    print(logo)
    print("Welcome to secret auction program.\n")
    bidder_name = input("What is your name?: ")
    bidder_offer_money = input("What's your bid?: ").replace('$', '')

# TODO-2: Save data into dictionary {name: price}
    bidder[bidder_name] = int(bidder_offer_money)

# TODO-3: Whether if new bids need to be added
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if yes_or_no == 'yes':
        add_bidder = True
        print("\n" * 20)
    elif yes_or_no == 'no':
        add_bidder = False
        find_the_highest_bid(bidder)




