# 28/02/2024
# Day - 025

# URL: https://www.sporcle.com/games/g/states
# [X] 1. Convert the guess to Title Case
# [X] 2. Check if the guess is among the 50 states
# [X] 3. Write correct guesses onto the map
# [X] 4. Use a loop to allow the user to keep guessing
# [X] 5. Record the correct guesses in a list
# [X] 6. Keep track of the score
# [X] 7. Save the missing states to a .csv

##################################################
# DAY 25 PROJECT: USA MAP GAME

print("\n*** Welcome to the USA States Game! ***")

import turtle
import pandas as pd
from writer import Writer



DIRECTORY_CSV = ".\\025 - CSV and Pandas\\PJ_USA_game\\50_states.csv"
DIRECTORY_OUTPUT_CSV = ".\\025 - CSV and Pandas\\PJ_USA_game\\states_to_learn.csv"
DIRECTORY_IMAGE = ".\\025 - CSV and Pandas\\PJ_USA_game\\blank_states_img.gif"
TOTAL_STATES = 50
correct_guesses = []
answer_state = ""



def get_mouse_click_coor(x, y):
    print(x, y)
    

def check_guess(all_states, answer):
    global correct
       
    if answer in all_states:
        correct_guesses.append(answer)
        all_states.pop(all_states.index(answer))
        return True
    
    return False


def write_in_map(answer):
    
    data_state = data[data.state == answer]
    row_index = data.index[data.state == answer].tolist()[0]
    
    x = data_state.x[row_index]
    y = data_state.y[row_index]
    
    write = Writer()
    write.write_state(x, y, answer)



screen = turtle.Screen()
screen.title("U.S. States Game")


screen.addshape(DIRECTORY_IMAGE)
turtle.shape(DIRECTORY_IMAGE)


# Pandas
data = pd.read_csv(DIRECTORY_CSV)
states = data["state"].to_list()

while (len(correct_guesses) < TOTAL_STATES) and answer_state != "Exit":
    score = f"{len(correct_guesses)}/{TOTAL_STATES}"
    answer_state = screen.textinput(title=f"{score} Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        dataframe = pd.DataFrame(states)
        dataframe.to_csv(DIRECTORY_OUTPUT_CSV)
    
    elif check_guess(states, answer_state):
        write_in_map(answer_state)

turtle.onscreenclick(get_mouse_click_coor)


# cant use it, it closes on click:
# screen.exitonclick()

# instead:
turtle.mainloop()