# 14/02/2024
# Day - 012



##################################################
# DAY 12 PROJECT: GUESS NUMBER

# Include an ASCII art logo: https://patorjk.com/software/taag/
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print("\n*** Welcome to Guess the Number! ***")

HARD = 5
EASY = 10

turns = 0
number = random.randint(1, 100)

print(logo)
print("I'm thinking of a number between 1 and 100.")
# print("Debugging hing:", number)


print("Choose a difficulty. Type 'easy' or 'hard'. ")
difficulty = input("> ").lower()

if difficulty == "hard":
    turns = HARD
else:
    turns = EASY

    

while turns > 0:
    print(f"\nYou have {turns} attempts remaining to guess the number")
    guess = int(input("Make an educated guess: "))

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print(f"You got it! The answer was {number}")
        
    turns -= 1
    
if turns == 0:
    print(f"Sorry, you lose. Answer: {number}")