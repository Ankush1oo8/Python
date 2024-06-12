from turtle import Turtle, Screen
import random as r
race_on=False
screen=Screen()

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
y_pos=[-70,-40,-10,20,50,80]
all_turtle=[]

for index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[index])
    tim.goto(x=-230,y=y_pos[index])
    all_turtle.append(tim)

if user_bet:
    race_on=True

while race_on:
    for t in all_turtle:
        if t.xcor()>230:
            race_on=False
            winning_turtle=t.pencolor()
            if winning_turtle==user_bet:
                print(f"You've won!! The {winning_turtle} turtle is winner!")
            else:
                print(f"You've lost!! The {winning_turtle} turtle is winner!")

        randist=r.randint(0,10)
        t.forward(randist)
    


screen.exitonclick()