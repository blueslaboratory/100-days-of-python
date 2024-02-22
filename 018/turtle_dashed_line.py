# 22/02/2024
# Day - 018

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

# Refactor: higlight the variable + F2


##################################################
print("\n\n*** Playing with the turtle: dashed line ***")


from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.speed(2)


# making a dashed line:
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    

screen = Screen()
screen.exitonclick()