# 22/02/2024
# Day - 018

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

# Refactor: higlight the variable + F2


##################################################
print("\n\n*** Imports ***")


# you can't name this file: turtle.py --> circular import
from turtle import Turtle

# import everything:
from turtle import *

# assigning alias:
import turtle as t
# tom = t.Turtle()

# heroes is not a part of the standard python library:
# pip install heroes
import heroes

print(heroes.gen())