# 23/02/2024
# Day - 019

# https://docs.python.org/3/library/turtle.html
# https://docs.python.org/3/library/turtle.html#turtle.listen


# W = Forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

##################################################
print("\n\n*** Turtle: Drawing ***")

from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.forward(-10)

def rotate_clockwise():
    tim.right(10)

def rotate_counter_clockwise():
    tim.right(-10)
    
def clear_screen():
    tim.clear()
    
def reset_drawing():
    tim.reset()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)

screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="r", fun=reset_drawing)

screen.exitonclick()