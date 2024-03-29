from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_TEXT = "✔"
SECONDS_OF_A_MINUTE = 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_label.config(text='')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * SECONDS_OF_A_MINUTE
    short_break_sec = SHORT_BREAK_MIN * SECONDS_OF_A_MINUTE
    long_break_sec = LONG_BREAK_MIN * SECONDS_OF_A_MINUTE
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
        check_label.config(text='')
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)

        if reps > 1:
            check_text = CHECK_TEXT * math.floor(reps / 2)
            check_label.config(text=check_text)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / SECONDS_OF_A_MINUTE)
    seconds = math.floor(count % SECONDS_OF_A_MINUTE)
    text = "{:02d}:{:02d}".format(int(minutes), int(seconds))
    canvas.itemconfig(timer_text, text=text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        if reps == 8:
            reset_timer()
        else:
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column=1, row=0)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text='', fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()