# 22/02/2024
# Day - 018

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

# Refactor: higlight the variable + F2


##################################################
print("\n\n*** Playing with the turtle: square ***")


from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("red")


# making a square:
for _ in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()