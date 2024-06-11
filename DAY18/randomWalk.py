import turtle as t
import random
tim=t.Turtle()

t.colormode(255)

def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

directions=[0,90,180,270]
tim.pensize(15)


tim.speed("fastest")
for _ in range(200):
    tim.color(randomColor())
    tim.forward(30)
    tim.setheading(random.choice(directions))





screen=t.Screen()
screen.exitonclick()