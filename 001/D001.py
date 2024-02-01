# 01/02/2024
# Day - 001



##################################################
print("\n\n*** print function ***")

print("Hello world! \n" +"Hello" +" " +"_______")
print()
print("Hello world! \n", "Hello", "Michael", "Angela")
print()
print("Hello world!", "\nHello", "Michael", "Angela")
print()



##################################################
print("\n\n*** input function ***")

input("Wassa wasa wassuuuuuup? ")

print("Moshi moshi", input("What is your name? "))
print("Moshi moshi " + input("What is your name? ") +"!")



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** auditorium ***")


# Day 1 - Lesson 1 - Printing
print("print('what to print')")
print()


# Day 1 - Lesson 2 - Debugging
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Day 1 - Lesson 3 - Input Function
n1 = int(input())
n2 = int(input())
print(n1 * n2)

name = input()
print(len(name))

# one-liner
print(len(input()))


# Day 1 - Lesson 4 - Variables
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️

# Write your code below this line 👇
c = a
a = b
b = c

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)



##################################################
# DAY 1 PROJECT: BAND GENERATOR

#1. Create a greeting for your program.
print('\n\n*** Welcome to the Band Name Generator ***')

#2. Ask the user for the city that they grew up in.
print("What's the name of the city you grew up in?")
city = input()

#3. Ask the user for the name of a pet.
pet = input('What\'s your pet\'s name?\n')

#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be:", city.capitalize(), pet.capitalize())
print()

# Solution: https://replit.com/@appbrewery/band-name-generator-end