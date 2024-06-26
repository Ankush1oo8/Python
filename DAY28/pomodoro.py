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

#timer reset
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="TIMER")
    check_mark.config(text=" ")


#timer mechanism
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    
    if reps%8==0:
        count_down(long_break)
        title_label.config(text="BREAK",fg=RED)
    elif reps%2==0:
        count_down(short_break)
        title_label.config(text="BREAK",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK",fg=GREEN)

#countdown mechanism

def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<0:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✔️"
        check_mark.config(text=mark)




window=Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,bg=YELLOW)



title_label=Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img=PhotoImage(file="DAY28/tomato.png")
canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(100,130,text="00.00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)




start=Button(text="START",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)


reset=Button(text="RESET",highlightthickness=0,command=reset)
reset.grid(column=2,row=2)

check_mark=Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)





window.mainloop()