# 27/02/2024
# Day - 023



##################################################
print("\n\n*** Turtle Crossing Capstone: Main ***")



import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



MAX_CARS = 42



def gameover():
    game_over = Turtle()
    game_over.color("black")
    game_over.penup()
    game_over.hideturtle()
    game_over.clear()
    game_over.goto(0, 0)
    game_over.write("GAME OVER", align="center", font=("Courier", 14, "normal"))



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()
cars = []
scoreboard = Scoreboard()



for i in range(MAX_CARS):
    car = CarManager()
    cars.append(car)
    
    
    
screen.listen()

# it can only move forward:
screen.onkey(player.up, key="space")



game_is_on = True
while game_is_on:
    
    # refresh rate of the moving parts:
    time.sleep(0.1)
    screen.update()
    
    for car in cars:
        car.move()
        
        # detect: collision with left wall --> reset
        if car.xcor() < -330:
            car.reset_position()
            
        # detect: collision with player --> game_over
        if player.distance(car) < 27:
            gameover()
            game_is_on = False
            
    # detect: player collision upper --> level_up
    if player.ycor() > 300:
        
        scoreboard.level += 1
        scoreboard.update_scoreboard()
        
        player.reset_position()
        
        for car in cars:
            car.level_up()
        
    

screen.exitonclick()