from tkinter import *

def mile2kilometer():
    mile=float(miles.get()) 
    kilometer_result_label["text"]=str(mile*1.609)
screen=Tk()
screen.title("Mile to Kilometer")
screen.config(padx=20,pady=20)

miles=Entry(width=5)
miles.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label=Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label=Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate=Button(text="Calculate",command=mile2kilometer)
calculate.grid(column=1,row=2)












screen.mainloop()