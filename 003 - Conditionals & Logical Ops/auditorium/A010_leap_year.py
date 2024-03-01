# 05/02/2024
# Day - 003



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 3 - Lesson 10 - Leap Year
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        print("Not leap year")
    elif year % 400 == 0:
        print("Leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
