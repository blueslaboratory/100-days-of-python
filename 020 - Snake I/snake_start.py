# 23/02/2024
# Day - 020



##################################################
print("\n\n*** Snake Game: Part 1 ***")

from turtle import Turtle, Screen
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# no traces:
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer
screen.tracer(0) 

segments = []



def create_snake_body(quantity):
    """create the snake body"""
    x_initial = 0
    
    for i in range(quantity):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(x=x_initial, y=0)

        segments.append(t)
        # pixel length of each "turtle" = 20
        x_initial -= 20



create_snake_body(quantity=3)
screen.update()

game_is_on = True
while game_is_on:
    
    # so that the body moves together and not 1 by 1 with delays:
    screen.update()
    time.sleep(0.2)
    
    # move the snake segment to the coord of the previous snake segment
    # for seg_num in range(start=last_segment, stop=first_segment, step=-1):
    for seg_num in range(len(segments)-1, 0, -1):
        # position of the immediate previous segment:
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        # move to the position of the next segment:
        segments[seg_num].goto(new_x, new_y)



screen.exitonclick()