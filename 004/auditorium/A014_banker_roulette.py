# 06/02/2024
# Day - 004



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 4 - Lesson 14 - Banker Roulette
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 

import random

# generate random numbers between 0 and the last index
payer = names[random.randint(0, len(names)-1)]

print(f"{payer} is going to buy the meal today!")