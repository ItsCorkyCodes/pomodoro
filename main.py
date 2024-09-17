from tkinter import *
from tkinter.ttk import *
import math
from plyer import notification


def notify(text):
    notification.notify(
        title='Tomoto',
        message=text,
        app_icon="C:/Users/aniru/Documents/Non-School Work/Pycharm Projects/Pomodoro/tomato icon.ico",
        timeout=10,
    )


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
GREEN2 = "#d6ffd9"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    #timer_text 0:00
    canvas.itemconfig(timer_text, text="00:00")
    # Title label tomoto
    title.config(text="Tomoto", foreground=RED)
    # Reset Check Marks
    check_marks.config(text="")
    start_button.config(state="normal")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    start_button.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        notify("Long Break Started.")
        title.config(foreground=RED, text="Long Break")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        notify("Short Break Started.")
        title.config(foreground=PINK, text="Short Break")
        count_down(short_break_sec)
    else:
        notify("Start Working! 😄")
        title.config(foreground=GREEN, text="Work Time")
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks.config(text="✔️")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomoto Focus")
window.config(padx=100, pady=50)
window.minsize(200, 300)

# Tomato Image
canvas = Canvas(width=200, height=300, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Futura", 24, "bold"))

# Reset Button
reset_button = Button(text="Reset", width=10, command=reset_timer)

# Start Button
start_button = Button(text="Start", width=10, command=start_timer)

# Title
title = Label(text="Tomoto", font=("Futura", 24, "bold"))
title.config(foreground=RED)

# Check Marks
check_marks = Label()

# Grid Layouts
canvas.grid(row=1, column=1)
reset_button.grid(row=3, column=1)
start_button.grid(row=2, column=1)
title.grid(row=0, column=1)
check_marks.grid(row=5, column=1)

window.mainloop()
