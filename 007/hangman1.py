# 08/02/2024
# Day - 007



##################################################
print("\n\n*** Hangman - 1 ***")


# Step 1
# Hint: https://developers.google.com/edu/python/lists#for-and-in
word_list = ["aardvark", "baboon", "camel"]


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

n_random = random.randint(0, len(word_list))
chosen_word = word_list[n_random - 1]
# chosen_word = random.choice(word_list)


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. 
# Make guess lowercase.
guess = input("Guess a letter: ").lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("False")