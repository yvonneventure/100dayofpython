import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
timmy = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(timmy.move,"Up")
screen.update()
sleeptime=0.1

game_is_on = True

while game_is_on:
    time.sleep(sleeptime)
    screen.update()
    cars.createcars()
    cars.move()
    for car in cars.newcars:
        if car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.gameover()

    if timmy.ycor()>260:
        scoreboard.updatescore()
        timmy.resetpos()
        cars.increasespeed()
        sleeptime*=0.9
    # if cars.checkcollision(timmy):
    #     game_is_on=False






    #cars.move()
    #detact to the wall (score +1), and return to the starting posistion

    #detact the car and game over


screen.exitonclick()

