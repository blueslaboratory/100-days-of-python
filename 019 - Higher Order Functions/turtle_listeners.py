# 23/02/2024
# Day - 019

# https://docs.python.org/3/library/turtle.html
# https://docs.python.org/3/library/turtle.html#turtle.listen



##################################################
print("\n\n*** Turtle: Listeners ***")

from turtle import Turtle, Screen


def move_forward():
    tim.forward(10)


tim = Turtle()
screen = Screen()


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()