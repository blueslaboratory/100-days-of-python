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


# Day 3 - Lesson 11 - Pizza Order Practice
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")


# Day 3 - Lesson 12 - Love Calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

names = (name1 + name2).lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

true_count = t+r+u+e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love_count = l+o+v+e

score = int(str(true_count) + str(love_count))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")