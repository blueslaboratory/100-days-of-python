# 07/02/2024
# Day - 005



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 5 - Lesson 17 - High Score
# Input a list of student scores
student_scores = input("> ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# IMPORTANT: Do not use the min() or max() functions
# Write your code below this row 👇
# Example input: 78 65 89 86 55 91 64 89

low_score = 100
high_score = 0

for score in student_scores:
  if score > high_score:
    high_score = score

  if score < low_score:
    low_score = score

print("The highest score in the class is:", high_score)
print("The lowest score in the class is:", low_score)