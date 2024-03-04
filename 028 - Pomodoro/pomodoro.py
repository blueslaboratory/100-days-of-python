# 01/03/2024
# Day - 028



##################################################
# DAY 28 PROJECT: POMODORO

print("\n*** Welcome to Pomodoro! ***")

from tkinter import *
import math



# ---------------------------- CONSTANTS ------------------------------- #
# https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2 # 25
SHORT_BREAK_MIN = 0.1 # 5
LONG_BREAK_MIN = 0.15 # 20
reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label "Timer"
    my_label_timer.config(text="Timer")
    # reset check_marks
    my_label_checks.config(text="")
    # restart the reps
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60
    
    # If it's the 8th rep:
    if reps % 8 == 0:
        my_label_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0: 
        my_label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        my_label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count%60
    
    # Dynamic typing: an int can become a string an viceversa
    # https://stackoverflow.com/questions/11328920/is-python-strongly-typed
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checks = ""
        for _ in range(1, reps, 2):
            checks += "✓"
        my_label_checks.config(text=checks)
            


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

"""
def say_something(a, b, c):
    print(a)
    print(b)
    print(c)

# waits 2000ms and calls function: say_something
window.after(2000, say_something, 3, 5, 8)
"""



# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=".\\028 - Pomodoro\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



# Label
my_label_timer = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
my_label_timer.grid(column=1, row=0)
my_label_timer.config(padx=10, pady=20)

# ✓
my_label_checks = Label(font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)
my_label_checks.grid(column=1, row=3)
my_label_checks.config(padx=10, pady=20)



# Button
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)



window.mainloop()