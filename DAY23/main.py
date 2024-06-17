import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
cars=CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    #detect collision with cars
    for car in cars.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()
    
    #detect winning
    if player.won():
        player.goto_start()
        cars.levelup()
        score.increase()


screen.exitonclick()