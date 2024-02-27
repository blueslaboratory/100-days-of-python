# 26/02/2024
# Day - 022



##################################################
print("\n\n*** Pong Game OOP: main ***")

from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
# no traces:
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")

screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")


game_is_on = True
while game_is_on:
    
    # so that the body moves together and not 1 by 1 with delays:
    # to make the ball go faster, reduce: time_move_speed
    time.sleep(ball.time_move_speed) 
    screen.update()
    
    
    ball.move()
        
    # detect: collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # detect: collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    
    # detect: collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # detect r_paddle misses the ball:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        
    # detect l_paddle misses the ball:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
    
    
screen.exitonclick()