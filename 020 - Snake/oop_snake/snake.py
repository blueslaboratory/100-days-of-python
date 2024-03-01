# 23/02/2024
# Day - 020



##################################################
print("\n\n*** Snake Game OOP: snake ***")

from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self, quantity):
        self.segments = []
        self.create_snake_body(quantity)
    

    def create_snake_body(self, quantity):
        """create the snake body"""
        x_initial = 0
        
        for i in range(quantity):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(x=x_initial, y=0)

            self.segments.append(t)
            # pixel length of each "turtle" = 20
            x_initial -= 20


    def move(self):
        """move the snake"""
        # move the snake segment to the coord of the previous snake segment
        # for seg_num in range(start=last_segment, stop=first_segment, step=-1):
        for seg_num in range(len(self.segments)-1, 0, -1):
            # position of the immediate previous segment:
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # move to the position of the next segment:
            self.segments[seg_num].goto(new_x, new_y)
            
        self.segments[0].forward(MOVE_DISTANCE)
    
    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)