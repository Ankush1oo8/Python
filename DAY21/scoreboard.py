from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("DAY21/data.txt") as file:
            self.high_score=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Arial", 24, "normal"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("DAY21/data.txt",mode="w")as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center",font=("Arial", 24, "normal"))


    def inc_score(self):
        self.score+=1
        self.update_score()