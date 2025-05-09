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
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="POMODORO", font=(FONT_NAME, 35, "bold"), fg=GREEN)
    check_marks.config(text="",fg=GREEN, bg=YELLOW, highlightthickness=0)
    global REPS
    REPS = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
       timer_label.config(text="Long Break",font=(FONT_NAME,35, "bold"), fg = RED)
       count_down(long_break_min)

    elif REPS % 2 == 0:
       timer_label.config(text="SHORT BREAK", font=(FONT_NAME, 35, "bold"), fg=PINK)
       count_down(short_break_min)

    else:
       timer_label.config(text="WORK TIME", font=(FONT_NAME, 35, "bold"), fg=RED)
       count_down(work_min)
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if count > 0:
      timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

timer_label = Label(text="POMODORO", font=(FONT_NAME,35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)

timer_label.grid(column=1,row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, command= start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_marks.grid(column=1, row=2)


window.mainloop()