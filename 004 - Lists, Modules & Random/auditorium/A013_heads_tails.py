# 06/02/2024
# Day - 004



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 4 - Lesson 13 - Heads or Tails
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random

# [0,1]
binary = random.randint(0,1)

# 0 --> Tails
# 1 --> Heads
if binary == 0:
    print("Tails")
else:
    print("Heads")