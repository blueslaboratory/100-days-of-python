# 29/02/2024
# Day - 026



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 26 - Lesson 31 - Dictionary Comprehension 1

# input: "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = input()

# 🚨 Don't change code above 👆
# Write your code below 👇

list_words = sentence.split()
result = {word: len(word) for word in list_words}

print(result)