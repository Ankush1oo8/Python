import turtle as t
import random
tim=t.Turtle()

t.colormode(255)
tim.speed("fastest")


def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)


def draw_spiral(size_og_gap):
    for _ in range(int(360/size_og_gap)):
        tim.color(randomColor())
        tim.circle(100)
        tim.setheading(tim.heading()+size_og_gap)

draw_spiral(5)
screen=t.Screen()
screen.exitonclick()