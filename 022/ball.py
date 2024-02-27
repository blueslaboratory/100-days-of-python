# 27/02/2024
# Day - 022



##################################################
print("\n\n*** Pong Game OOP: Ball ***")

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        
        self.goto(0, 0)
        
        self.x_move = 10
        self.y_move = 10
        # self.ball_angle = 45 # 37
        
        self.time_move_speed = 0.1
        

    def move(self):
        # self.setheading(self.ball_angle) 
        # self.forward(10)
        
        # Another way (sol):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
        
    def bounce_y(self):
        # self.ball_angle = -self.ball_angle
        
        # Another way (sol)
        self.y_move *= -1
        
        
    def bounce_x(self):
        self.x_move *= -1
        # make the ball go faster
        self.time_move_speed *= 0.99
        
        
    def reset_position(self):
        self.goto(0, 0)
        self.time_move_speed = 0.1
        self.bounce_x()