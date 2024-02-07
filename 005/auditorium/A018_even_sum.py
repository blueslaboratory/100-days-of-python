# 07/02/2024
# Day - 005



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 5 - Lesson 18 - Even Sum
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
even_sum = 0

for n in range(2, target+1, 2):
    even_sum += n

print(even_sum)