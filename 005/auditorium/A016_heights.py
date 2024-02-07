# 07/02/2024
# Day - 005



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 5 - Lesson 16 - Average Height
# Input a Python list of student heights
student_heights = input('> ').split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# IMPORTANT: Do not use the sum() or len() functions
# Write your code below this row 👇
  
# Example input: 156 178 165 171 187

sum_heights = 0
counter = 0

for height in student_heights:
  sum_heights += height
  counter += 1

average_height = round(sum_heights/counter)

print()
print(f"total height = {sum_heights}")
print(f"number of students = {counter}")
print(f"average height = {average_height}")