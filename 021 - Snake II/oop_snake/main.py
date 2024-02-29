# 26/02/2024
# Day - 021



##################################################
print("\n\n*** Snake Game OOP: main ***")

from turtle import Screen
import time
from snake import *
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# no traces:
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")


game_is_on = True
while game_is_on:
    
    # so that the body moves together and not 1 by 1 with delays:
    screen.update()
    time.sleep(0.2)

    snake.move()
    
    # detect: collision with food
    if snake.segments[0].distance(food) < 15:
        print("mmm tasty mmm tasty")
        food.refresh()
        snake.extend()
        scoreboard.refresh()
        
    # detect: collision with wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        scoreboard.game_over()
        game_is_on = False
        
    # detect: collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        

screen.exitonclick()