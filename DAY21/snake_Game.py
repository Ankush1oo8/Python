from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
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
food=Food()
score=Score()


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
    
    #collision with food
    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.inc_score()

    #Detect collision with the tail
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        score.reset()
        snake.reset()

    #detect collision with tail
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg)<10:
            score.reset()
            snake.reset()






screen.exitonclick()