# 26/02/2024
# Day - 022



##################################################
print("\n\n*** Pong Game OOP: Paddle ***")

from turtle import Turtle


UP = 90
DOWN = 270

MOVE_DISTANCE = 10


class Paddle(Turtle):

    def __init__(self, x_start, y_start):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_start, y=y_start)

    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)