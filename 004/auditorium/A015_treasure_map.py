# 06/02/2024
# Day - 004



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 4 - Lesson 15 - Treasure Map
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].upper()
number = int(position[1])


if letter == "A":
    column_index = 0
elif letter == "B":
    column_index = 1
elif letter == "C":
    column_index = 2

# more elegant
ABC = ["A", "B", "C"]

column_index = ABC.index(letter)
row_index = number-1

map[row_index][column_index] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")