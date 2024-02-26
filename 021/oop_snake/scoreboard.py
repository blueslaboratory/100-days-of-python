# 26/02/2024
# Day - 021

# https://docs.python.org/3/library/turtle.html#turtle.write

##################################################
print("\n\n*** Snake Game OOP: snake ***")


from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        
        self.refresh()
        
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        
        
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1