from turtle import Screen, Turtle
import time
from snake import Snake
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

#TODO create a snake body
# segment_1=Turtle("square")
# segment_1.color("white")

# segment_2=Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)

# segment_3=Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)
snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


#TODO move the snake 
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()











screen.exitonclick()