# 01/02/2024
# Day - 001



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