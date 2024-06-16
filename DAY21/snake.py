from turtle import Turtle 
start_pos=[(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        
    def create_snake(self):
        for pos in start_pos:
            self.add_seg(pos)

    def add_seg(self,pos):
        new_seg=Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)
    
    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)