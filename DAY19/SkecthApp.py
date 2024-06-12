from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

def moveForward():
    tim.forward(10)


def moveBackward():
    tim.backward(10)

def turn_left():
    tim.setheading(tim.heading()+10)

def turn_right():
    tim.setheading(tim.heading()-10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(moveForward,"w")
screen.onkey(moveBackward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()