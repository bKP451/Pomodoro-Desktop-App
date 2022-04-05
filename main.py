
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    reps += 1
    if reps == 8:
        title_label.config(fg=RED, text="LONG BREAK")
        counter(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(fg=PINK, text="SHORT BREAK")
        counter(short_break_sec)
    else:
        title_label.config(fg=GREEN, text="WORK")
        counter(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    minutes = int(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, counter, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            times = ''
            for i in range(int(reps/2)):
                times += '✔'
        check_one.config(text=f'{times}')

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomodoro Application")
window.config(bg=YELLOW, pady=50, padx=100)

# TODO To put the missing widgets onto the screen

# let me put the title
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
title_label.grid(row=0, column=1)
# I have to create a PhotoImage widget
canvas = Canvas(width=200,  height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
tomato_canvas = canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 18, "bold"))
canvas.grid(row=1, column=1)

# Start_Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
# Reset button
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

# checkboxes label
check_one = Label(text="", bg=YELLOW, fg=GREEN)
check_one.grid(row=3, column=1)


window.mainloop()