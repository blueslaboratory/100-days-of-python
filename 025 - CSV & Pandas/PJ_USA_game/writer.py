# 29/02/2024
# Day - 025



##################################################
# DAY 25 PROJECT: USA MAP GAME

print("\n*** Welcome to the USA States Game! ***")

from turtle import Turtle


FONT = ("Courier", 8, "normal")


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        
        
    def write_state(self, x, y, state):
        self.clear()
        self.goto(x, y)
        self.write(f"{state}", align="center", font=FONT)