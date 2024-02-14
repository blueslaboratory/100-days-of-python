# 14/02/2024
# Day - 014



##################################################
# DAY 14 PROJECT: Higher or Lower
# GAME: https://www.higherlowergame.com/

# Steps

# [X] Add art.
# [X] Generate a random account from the game data.
# [X] Format account data into printable format.
# [X] Ask user for a guess.
# [X] Check if user is correct.
#### [X] Get follower count.
#### [X] If Statement

# [X] Feedback.
# [X] Score Keeping.
# [X] Make B become the next A.
# [X] Clear screen between rounds.
# [X] Make game repeatable.



import random, os
import art, game_data



# [X] Add art.
print("\n*** Welcome to the Higher or Lower! ***")
print(art.logo)

SCORE = 0



# [X] Generate a random account from the game data.
def get_random_account():
    '''gets a random account from game_data.py and returns a presentation and the followers'''
    person = random.choice(game_data.data)
    
    # [X] Format account data into printable format.
    # presentation = f"{person['name']}, a {person['description']}, from {person['country']}"
    presentation = f"{person['name']}, a {person['description']}, from {person['country']}, followers {person['follower_count']}"
    followers = person["follower_count"]
    
    return presentation, followers



# [X] Check if user is correct.
#### [X] Get follower count.
#### [X] If Statement
def check_guess(guess, followers_A, followers_B):
    '''checks if the guess is correct and returns a boolean'''
    global SCORE
    if guess == 'A':
        if followers_A >= followers_B:
            SCORE += 1
            print(f"Correct!! Score: {SCORE}")
            return True
        else:
            print(f"You lost. A: {followers_A} - B: {followers_B}. Score: {SCORE}")
            return False
    elif guess == 'B':
        if followers_B >= followers_A:
            SCORE += 1
            print(f"Correct!! Streak: {SCORE}")
            return True
        else:
            print(f"You lost. A: {followers_A} - B: {followers_B}. Score: {SCORE}")
            return False
    else:
        print(f"Invalid option. You lost. A: {followers_A} - B: {followers_B}. Score: {SCORE}")
        return False



def game(introducing_A, followers_A):
    '''higher lower game dynamics, returns if the guess is correct'''
    introducing_B, followers_B = get_random_account()
    global SCORE
    
    print("Current Streak:", SCORE)
    print("Compare A:", introducing_A)
    print(art.vs)
    print("Compare B:", introducing_B)
    
    # [X] Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    # [X] Check if user is correct.
    correct_guess = check_guess(guess, followers_A, followers_B)

    if correct_guess:
        
        # [] Make B become the next A.
        # local scope: doesn't work
        # introducing_A, followers_A = introducing_B, followers_B
        
        # [X] Clear screen between rounds.
        os.system('cls||clear')
        
    return correct_guess, introducing_B, followers_B



introducing_A, followers_A = get_random_account()

correct_guess = True
continue_playing = True

# [X] Make game repeatable.
while correct_guess or continue_playing:
    
    # [X] Make B become the next A.
    correct_guess, introducing_A, followers_A = game(introducing_A, followers_A)
    
    if not correct_guess:
        play_again = input("\nWould you like to play again 'y' or 'n' ?: ")
        
        if play_again != 'y':
            SCORE = 0
            continue_playing = False