# 12/02/2024
# Day - 009



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 9 - Lesson 22 - Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆


# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    score = student_scores[key]
    if (score > 90 and score <= 100):
        student_grades[key] = "Outstanding"
    elif (score > 80):
        student_grades[key] = "Exceeds Expectations"
    elif (score > 70):
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
        

# for key in student_grades:
#     print(key, ":", student_grades[key])


# 🚨 Don't change the code below 👇
print(student_grades)