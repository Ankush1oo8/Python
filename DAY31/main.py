from tkinter import *
import pandas as p
import random as r
BACKGROUND_COLOR = "#B1DDC6"
curr_card={}
to_learn={}
# -----------------------Mechanism-----------------------------------------
try:
    data=p.read_csv("DAY31/data/word_to_learn.csv")
except FileNotFoundError:
    org_data=p.read_csv("DAY31/data/french_word.csv")
    to_learn=org_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global curr_card,flip_timer
    window.after_cancel(flip_timer)
    curr_card=r.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=curr_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer=window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=curr_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back)

def is_known():
    to_learn.remove(curr_card)
    data=p.DataFrame(to_learn)
    data.to_csv("DAY31/data/words_to_learn.csv",index=False)
    next_card()



# -----------------------UI SETUP-----------------------------------------
window=Tk()
window.title("FLASHY")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
card_front=PhotoImage(file="DAY31/images/card_front.png")
card_back=PhotoImage(file="DAY31/images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_img=PhotoImage(file="DAY31/images/wrong.png")
unknown_button=Button(image=cross_img,command=next_card,highlightthickness=0)
unknown_button.grid(row=1,column=0)

check_img=PhotoImage(file="DAY31/images/right.png")
known_button=Button(image=check_img,command=is_known,highlightthickness=0)
known_button.grid(row=1,column=1)
next_card()

window.mainloop()