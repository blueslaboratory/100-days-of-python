# 29/02/2024
# Day - 026



##################################################
print("\n\n*** Looping ***")

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}



print("\nLooping through a dictionary")
for (key, value) in student_dict.items():
    print(value)



print("\nLooping through a data frame 1")
import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_dict)
for (key, value) in student_data_frame.items():
    print("Key:", key)
    print("Values:")
    print(value)



print("\nLooping through a data frame 2")
print(student_data_frame)
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    if row.student == "Angela":
        print(row.score)