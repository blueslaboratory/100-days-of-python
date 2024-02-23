# 23/02/2024
# Day - 019

# https://docs.python.org/3/library/turtle.html



##################################################
print("\n\n*** Turtle: Race ***")


from turtle import Turtle, Screen
import random


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")



def create_turtles(quantity):
    y_initial = -100
    
    for i in range(quantity):
        t = Turtle(shape="turtle")
        t.color(colors[i])
        t.penup()
        t.goto(x=-230, y=y_initial)

        all_turtles.append(t)
        y_initial += 40


def race():
    if user_bet:
        is_race_on = True
    
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                
                is_race_on = False
                winning_color = turtle.pencolor()
                
                if user_bet == winning_color:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                        
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
    


create_turtles(len(colors))
race()

screen.exitonclick()