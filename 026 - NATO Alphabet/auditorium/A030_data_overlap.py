# 29/02/2024
# Day - 026



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 26 - Lesson 30 - Data Overlap

# Hint:
# Use the keyword method for starting the List comprehension and fill in the relevant parts.
# First, you will need to read from the files and create a list using the lines in the files.
# This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp
# Remember you can check if a value exists in a list using the in keyword. 
# https://www.w3schools.com/python/ref_keyword_in.asp
# Remember you can use the int() method in python to convert a string into an integer.



DIRECTORY_FILE_1 = ".\\026 - NATO Alphabet\\auditorium\\file1.txt"
DIRECTORY_FILE_2 = ".\\026 - NATO Alphabet\\auditorium\\file2.txt"



with open(DIRECTORY_FILE_1) as file:
    list1 = file.readlines()
    list1 = [int(x.strip()) for x in list1]
    print(list1)

with open(DIRECTORY_FILE_2) as file:
    list2 = file.readlines()
    list2 = [int(x.strip()) for x in list2]
    print(list2)
    

result = [num for num in list1 if num in list2]



# Write your code 👆 above:
print(result)