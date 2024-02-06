# 05/02/2024
# Day - 003



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 3 - Lesson 8 - Odd or Even
# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
remainder = number%2
if remainder == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")