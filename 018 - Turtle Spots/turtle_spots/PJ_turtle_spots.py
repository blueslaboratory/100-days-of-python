# 22/02/2024
# Day - 018


# https://docs.python.org/3/library/turtle.html
# PJ_turtle_spots.py: 10 x 10 spots
# -> spot width: 20
# -> spacing: 50

##################################################
# DAY 18 PROJECT: TURTLE SPOTS

print("\n*** Welcome to the Turtle Art! ***")


from turtle import Turtle, Screen
import random


def paint_filled_circle():
    tim.color(random.choice(color_list))
    tim.begin_fill()
    tim.circle(14)
    tim.end_fill()

def paint_dot():
    color = random.choice(color_list)
    tim.dot(20, color)


# from color_extraction:
color_list = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 232, 237), (146, 28, 66), (239, 75, 35), (230, 237, 232), (7, 148, 94), (220, 171, 45), (182, 159, 48), (44, 191, 232), (28, 126, 194), (253, 223, 0), (125, 192, 79), (84, 28, 91), (245, 219, 50), (179, 40, 98), (42, 169, 116), (209, 131, 165), (205, 56, 35), (239, 161, 192)]


screen = Screen()
tim = Turtle()


# so that random_rgb() works
screen.colormode(255)


tim.hideturtle()
tim.speed(0)
y_start = -180


for y in range(10):
    tim.penup()
    tim.setx(-220)
    tim.sety(y_start)
    tim.pendown

    # drawing the spots:
    for spot in range(10):
        # paint_filled_circle()
        paint_dot()
        tim.penup()
        tim.forward(51)
        tim.pendown
        
    y_start += 50
    

screen.exitonclick()