# 05/02/2024
# Day - 003



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 3 - Lesson 12 - Love Calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

names = (name1 + name2).lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

true_count = t+r+u+e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love_count = l+o+v+e

score = int(str(true_count) + str(love_count))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")