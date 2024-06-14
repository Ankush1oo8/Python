from turtle import Turtle
import random as r

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        random_x=r.randint(-280,280)
        random_y=r.randint(-280,280)
        self.goto(random_x,random_y)

    def refresh(self):
        random_x=r.randint(-280,280)
        random_y=r.randint(-280,280)
        self.goto(random_x,random_y)
