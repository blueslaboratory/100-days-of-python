# 05/02/2024
# Day - 003



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 3 - Lesson 9 - BMI (Body Mass Index) 2.0
# Enter your height in meters e.g., 1.55
height = float(input("Height (m): "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Weight (kg): "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight/(height**2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")