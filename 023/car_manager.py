# 27/02/2024
# Day - 023



##################################################
print("\n\n*** Turtle Crossing Capstone: Car Manager ***")

from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2)
        
        self.penup()
        self.goto(random.randint(200, 900), random.randint(-300, 300))
        self.setheading(180)
        
        self.move_distance = STARTING_MOVE_DISTANCE
        
        
    def move(self):
        self.forward(self.move_distance)
        
        
    def reset_position(self):
        self.goto(random.randint(300, 900), random.randint(-300, 300))
        
    
    def level_up(self):
        self.goto(random.randint(200, 900), random.randint(-300, 300))
        self.move_distance += MOVE_INCREMENT