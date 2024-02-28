# 28/02/2024
# Day - 024



##################################################
print("\n\n*** Snake Game OOP: snake ***")


from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.shape("circle")
        self.penup()
        # https://docs.python.org/3/library/turtle.html#turtle.shape
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        
        self.refresh()
        
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        
        self.goto(random_x, random_y)