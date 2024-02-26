# 23/02/2024
# Day - 020



##################################################
print("\n\n*** Snake Game OOP: main ***")

from turtle import Screen
import time
from snake import *



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# no traces:
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer
screen.tracer(0)


snake = Snake(3)

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

screen.exitonclick()