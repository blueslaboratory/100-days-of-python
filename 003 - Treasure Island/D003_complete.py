# 05/02/2024
# Day - 003



##################################################
print("\n\n*** Conditional statements (if, elif, else) ***")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    
    # nesting: if/elif/else (secuential)
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Child tickets price: 丰{bill}")
    elif age <=18:
        bill = 7
        print(f"Youth tickets price: 丰{bill}")
    elif age >= 45 and age <= 55:
        print("MIDLIFE CRISIS FREE RIDE!")
    else:
        bill = 12
        print(f"Adult tickets price: 丰{bill}")

    wants_photo = input("Do you want a photo taken? Y or N: ").upper()
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is 丰{bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

# Comparison operators:
# >     greater than
# <     less than
# >=    greater than or equal to
# <=    less than or equal to
# ==    equal to
# !=    not equal to



##################################################
print("\n\n*** Logical operators (and, or, not) ***")

print("True and True:", True and True)
print("True and False:", True and False)
print("False and False:", False and False) 

print()
print("True or True:", True or True)
print("True or False:", True or False)
print("False or False:", False or False)
print()

print("not True:", not True)
print("not False:", not False)
print()



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



##################################################
# DAY 3 PROJECT: TREASURE ISLAND

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"")
choice_cross = input("> ").lower()

if choice_cross != "right":
    print("You fell into a hole. Game Over.")
else:
    print("You come to a lake. There is an island in the middle of the lake.")
    print('Type "wait" to wait for a boat. Type "swim" to swim across.')
    choice_lake = input("> ").lower()

    if choice_lake != "wait":
        print("You were attacked by a trout. Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("One red, one yellow and one blue. Which colour do you choose?")
        choice_door = input("> ").lower()

        if choice_door == "yellow":
            print("You found the treasure! You Win!")
            print("Congratulations young padawan!")
        elif choice_door == "blue":
            print("You were eaten by beasts. Game Over.")
        elif choice_door == "red":
            print("You were burned by fire. Game Over.")
        elif choice_door == "alohomora":
            print("""
                         ,    _
                        /|   | |
                      _/_\_  >_<
                     .-\-/.   |
                    /  | | \_ |
                    \ \| |\__(/
                    /(`---')  |
                   / /     \  |
                _.'  \ '-' /  |
                `----'`=-='   '
                """)
            print("Magic is not allowed! Game Over.")
        else:
            print("You chose an imaginary door. Game Over.")