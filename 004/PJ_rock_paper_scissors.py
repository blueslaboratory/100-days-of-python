# 06/02/2024
# Day - 004



##################################################
# DAY 4 PROJECT: ROCK, PAPER & SCISSORS

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below this line 👇

import random

computer_choice = random.randint(0,2)
ascii_images = [rock, paper, scissors]

print("Type 0 for Rock, 1 for Paper or 2 for Scissors.")
print("What do you choose?")
user_choice = int(input("> "))

if user_choice < 0 or user_choice > 2:
    print("You typed and invalid number, you lost!")
else:
    print("\nComputer chose:")
    print(ascii_images[computer_choice])
    print("\nUser chose: ")
    print(ascii_images[user_choice])

    if computer_choice == user_choice:
        print("It's a draw!")
    elif computer_choice == 0:
        # rock(0), paper(1)
        if user_choice == 1:
            print("You won!")
        else:
            print("You lost!")
    elif computer_choice == 1:
        # paper(1), rock(0)
        if user_choice == 0:
            print("You lost!")
        else:
            print("You won!")
    elif computer_choice == 2:
        # scissors(2), rock(0)
        if user_choice == 0:
            print("You won!")
        else:
            print("You lost!")

