from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

def moveForward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space",fun=moveForward)
screen.exitonclick()