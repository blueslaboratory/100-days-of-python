# 27/02/2024
# Day - 023



##################################################
print("\n\n*** Turtle Crossing Capstone: Scoreboard ***")


from turtle import Turtle


FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        
        self.level = 0
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)