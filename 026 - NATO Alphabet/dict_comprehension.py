# 29/02/2024
# Day - 026



##################################################
print("\n\n*** Dictionary Comprehension ***")



# new_dict = {new_key: new_value for item in list}

# Create a dictionary based on the value of existing dictionaries:
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}



import random


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score > 49}

print(students_scores)
print(passed_students)