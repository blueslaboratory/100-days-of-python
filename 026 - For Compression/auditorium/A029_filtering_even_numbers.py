# 29/02/2024
# Day - 026



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 26 - Lesson 29 - Filtering Even Numbers

# input: 9, 0, 32, 8, 2, 8, 64, 29, 42, 99
list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
integers = [int(x) for x in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [n for n in integers if n%2==0]

# Write your code 👆 above:
print(result)