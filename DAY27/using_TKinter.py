import tkinter as t

window=t.Tk()
window.title("MY GUI")
window.minsize(300,300)

#Label
my_label=t.Label(text="I am a label",font=("Arial",14,"bold"))
my_label.pack(side="bottom")

#buttons
def button_click():
    print("Clicked")
    # my_label["text"]="Button got clicked!!"
    new_text=input.get()
    my_label["text"]=new_text

button=t.Button(text="Click Me",command=button_click)
button.place(x=100,y=100)

#entry
input=t.Entry(width=10)
input.pack()






window.mainloop()