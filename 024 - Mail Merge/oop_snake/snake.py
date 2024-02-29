# 28/02/2024
# Day - 024



##################################################
print("\n\n*** Snake Game OOP: snake ***")

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake_body()
    

    def create_snake_body(self):
        """create the snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())


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
            
            
    def reset(self):
        # move the segments somewhere out of the screen:
        for s in self.segments:
            s.goto(1000, 1000)
        self.segments.clear()
        self.create_snake_body()