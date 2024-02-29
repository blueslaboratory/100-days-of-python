# 29/02/2024
# Day - 026



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 26 - Lesson 32 - Dictionary Comprehension 2


# input: {"Monday": 4, "Tuesday": 5, "Wednesday": 10, "Thursday": 11, "Friday": 12, "Saturday": 14, "Sunday": 16}
weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day:(temp_c*9/5 + 32) for (day, temp_c) in weather_c.items()}

print(weather_f)