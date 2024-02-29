# 12/02/2024
# Day - 009



##################################################
# DAY 9 PROJECT: SECRET AUCTION PROGRAM
import os, art

print("\n*** Welcome to the secret auction program ***")

print(art.logo)



flag = True
bidders = {}

def highest_bidder(dict_bidders):
    highest_bid = 0
    winner = ""

    for key in dict_bidders:
        bid_amount = dict_bidders[key]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key

    print(f"The winner of this auction is: {winner}")
    print(f"Final selling price: ${highest_bid}")



while flag == True:
    name = input("\nWhat is your name?: ")
    bid = float(input("What's your bid?: $"))

    bidders[name] = bid

    print("Are there any other bidders? Type 'yes' or 'no'.")
    more_bidders = input("> ")
    
    # clear the screen
    os.system('cls||clear')

    if more_bidders != 'yes':
        flag = False
        highest_bidder(bidders)