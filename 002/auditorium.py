# 02/02/2024
# Day - 002



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 2 - Lesson 5 - Data Types
two_digit_number = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
d1 = int(two_digit_number[0])
d2 = int(two_digit_number[1])

print(d1 + d2)


# Day 2 - Lesson 6 - Data Types
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = float(weight)/float(height)**2
print(int(BMI))


# Day 2 - Lesson 7 - Life in weeks
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 

weeks_left = (90-int(age))*52

print(f"You have {weeks_left} weeks left.")