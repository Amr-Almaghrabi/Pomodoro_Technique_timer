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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    text.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        text.config(text="Long Break", fg=RED)
        count_down(long_break)

    elif reps % 2 == 0:
        text.config(text="Short Break", fg=PINK)
        count_down(short_break)

    else:
        text.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")

    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, highlightbackground=YELLOW, command=start_count)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

text = Label(text="Timer!", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
text.grid(column=1, row=0)
checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
checkmark.grid(column=1, row=2)

window.mainloop()
