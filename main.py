from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(time)
    timer_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 7:
        count_down(long_break_sec)
        timer_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(work_sec)
        timer_text.config(text="Work", fg=GREEN)
    else:
        count_down(short_break_sec)
        timer_text.config(text="Break", fg=PINK)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            mark += CHECKMARK
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_text = Label(text="Timer", font=(FONT_NAME, 70, "bold"), fg=GREEN, bg=YELLOW)
timer_text.grid(column=1, row=0)

start = Button(text="Start", font=(FONT_NAME, 20, "bold"), command=start_timer)
start.grid(column=0, row=2)

end = Button(text="End", font=(FONT_NAME, 20, "bold"), command=reset_timer)
end.grid(column=2, row=2)

checkmark = Label(font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
