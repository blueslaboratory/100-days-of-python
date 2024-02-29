# 28/02/2024
# Day - 024

# https://docs.python.org/3/library/turtle.html#turtle.write

##################################################
print("\n\n*** Snake Game OOP: snake ***")


from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
HIGH_SCORE_DIRECTORY = ".\\024 - Mail Merge\\oop_snake\\high_score.txt"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = 0
        
        with open(HIGH_SCORE_DIRECTORY) as file:
            self.high_score = int(file.read())
        
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        
        self.refresh()
            
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
            # write in a file
            with open(HIGH_SCORE_DIRECTORY, mode="w") as file:
                file.write(str(self.high_score))
                
        self.score = 0
        self.refresh()

        
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
          
        
    def increase_score(self):
        self.score += 1
        self.refresh()