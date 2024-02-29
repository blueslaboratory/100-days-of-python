# 28/02/2024
# Day - 025

# URL: https://www.sporcle.com/games/g/states


##################################################
# DAY 25 PROJECT: USA MAP GAME SOLUTION

print("\n*** Welcome to the USA States Game! ***")

import turtle
import pandas

DIRECTORY_CSV = ".\\025 - USA Map Game\\PJ_USA_game\\50_states.csv"
DIRECTORY_OUTPUT_CSV = ".\\025 - USA Map Game\\PJ_USA_game\\states_to_learn.csv"
DIRECTORY_IMAGE = ".\\025 - USA Map Game\\PJ_USA_game\\blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
image = DIRECTORY_IMAGE
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(DIRECTORY_CSV)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(DIRECTORY_OUTPUT_CSV)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)