# 13/02/2024
# Day - 011


############### Blackjack Project #####################

# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


##################### Hints #####################

# Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# [X] Deal both user and computer a starting hand of 2 random card values.
# [X] Detect when computer or user has a blackjack. (Ace + 10 value card).
# [X] If computer gets blackjack, then the user loses (even if the user also has a blackjack). 
#     If the user gets a blackjack, then they win (unless the computer also has a blackjack).
# [X] Calculate the user's and computer's scores based on their card values.
# [X] If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
# [X] Reveal computer's first card to the user.
# [X] Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
# [X] Ask the user if they want to get another card.
# [X] Once the user is done and no longer wants to draw any more cards, let the computer play. 
#     The computer should keep drawing cards unless their score goes over 16.
# [X] Compare user and computer scores and see if it's a win, loss, or draw.
# [X] Print out the player's and computer's final hand and their scores at the end of the game.
# [X] After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.


##################################################
# DAY 11 PROJECT: BLACKJACK - MY SOLUTION (MIGHT NOT BE COMPLETELY CORRECT)

from art import logo
import random, os

print("\n\n*** Welcome to Blackjack ***")

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = []
computer_hand = []


def deal_card(hand):
    hand.append(random.choice(cards))


def calculate_score(hand):
    score = 0

    for card in hand:
        score += card
        
    if score > 21:
        score = convert_ace(hand)
    
    return score


def convert_ace(hand):
    score = 0
    
    if 11 in hand:
        hand.remove(11)
        hand.append(1)
    
    for card in hand:
        score += card
    
    return score


def check_blackjack_21(hand):
    check = False
    score = calculate_score(hand)
    
    if score == 21:
        check = True
    
    return check


def check_busted(hand):
    check = False
    
    if calculate_score(hand) > 21:
        check = True
        
    return check
    
    

continue_playing = True

while continue_playing:
    
    
    # Cleaning the hands
    user_hand = []
    computer_hand = []
    
    
    # Initial dealing
    for i in range(2):
        deal_card(user_hand)
        deal_card(computer_hand)
    
    
    # BUGs and edgecases
    # user_hand = [11, 11]


    # Testing: cards reveal 
    print("\nUser hand:", user_hand)
    # print("Computer hand:", computer_hand)


    # Computer cards[0] reveal
    print(f"Computer 1st Card Reveal [{computer_hand[0]}][?]")

    
    # User: another card
    flag_card = True
    while flag_card and calculate_score(user_hand) < 21:
        another_card = input("\nGet another card 'y' or 'n' ?: ")
        if another_card == 'y':
            deal_card(user_hand)
            print("User hand:", user_hand)
        else:
            flag_card = False
    
    
    # Computer: another card
    while calculate_score(computer_hand) <= 16:
        deal_card(computer_hand)
    
    
    # Calculate    
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)
    
    if check_blackjack_21(computer_hand):
        print("Computer has 21 BlackJack. Computer wins.")
        print("Thanks for participating!")
    elif check_blackjack_21(user_hand):
        print("User has 21 BlackJack. User wins.")
        print("Congratulations!")
    elif user_score > computer_score:
        if check_busted(user_hand) == False:
            print("User wins. Congratulations!")
        elif check_busted(computer_hand) == False:
            print("Computer wins.")
            print("Thanks for participating!")
        else:
            print("It's a draw...")
    elif computer_score > user_score:
        if check_busted(computer_hand) == False:
            print("Computer wins.")
            print("Thanks for participating!")
        elif check_busted(user_hand) == False:
            print("User wins. Congratulations!")
        else:
            print("It's a draw...")
    else:
        print("It's a draw...")
        
    
    # Results
    print("\n_______________________")
    print("*** Aftermath ***")
    print("Computer's hand:", computer_hand)
    print("Score: ", calculate_score(computer_hand))
    print("User's hand:", user_hand)
    print("Score: ", calculate_score(user_hand))


    # Play again
    play_again = input("\nWould you like to play again 'y' or 'n' ?: ")

    if play_again != 'y':
        continue_playing = False
    else:
        # clear the screen
        os.system('cls||clear')