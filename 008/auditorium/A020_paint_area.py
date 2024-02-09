# 09/02/2024
# Day - 008



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 8 - Lesson 20 - Paint Area Calculator
# Hint: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number


# Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    area = height * width
    number_cans = math.ceil(area / cover)
    print(f"You'll need {number_cans} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   


# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)