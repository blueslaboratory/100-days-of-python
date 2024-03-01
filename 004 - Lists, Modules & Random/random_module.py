# 06/02/2024
# Day - 004



##################################################
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
print("\n\n*** Random Module ***")

# modules
import random
import my_module

print(my_module.pi)

# random_integer: [1, 10]
random_integer = random.randint(1,10)
print(random_integer)

# random_float: [0.0000, 0.9999]
random_float = random.random()
print(random_float)

# [0, 4.9999999]
random_float = random.random()*5
print(random_float)

# love calculator (D003 - auditorium)
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")