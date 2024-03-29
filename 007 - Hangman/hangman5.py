# 08/02/2024
# Day - 007



##################################################
print("\n\n*** Hangman - 5 ***")


# Step 5
# Hint: https://www.askpython.com/python/python-import-statement
import random


# importing1.py
import sys
import os

# Agregar la ruta de la carpeta 'hangman_5' al sys.path
# Para que Python pueda encontrar los módulos en esa carpeta
sys.path.append(os.path.join(os.path.dirname(__file__), 'hangman5')) 

# Ahora puedes importar el módulo 'hangman_art'
# from hangman_words import word_list
import hangman_art, hangman_words


# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)


# Testing code
print(f'\nPssst, the solution is {chosen_word}.')


# Create blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    # clear the screen
    os.system('cls||clear')


    # TODO-4: - If the user has entered a letter they've already guessed, 
    # print the letter and let them know.
    if guess in display:
        print(f"\nLetter '{guess}' has already been guessed.")
    

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


    # Check if user is wrong.
    if guess not in chosen_word:
        

        # TODO-5: - If the letter is not in the chosen_word, print out the letter and 
        # let them know it's not in the word.
        print(f"Letter '{guess}' is not in the word.")


        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])


    # Join all the elements in the list and turn it into a String.
    # print(f"{' '.join(display)}")
    print("\nLives:", lives)
    print(display)  