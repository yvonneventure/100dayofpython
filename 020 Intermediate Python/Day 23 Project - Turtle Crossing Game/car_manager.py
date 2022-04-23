import random
import time
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 10
TIME = 0.1
X=280
Y=[]
for i in range(-250,250,10):
    Y.append(i)


class CarManager:
    def __init__(self):
        #super().__init__()
        self.newcars = []
        self.createcars()
        self.time=TIME
        self.speed=STARTING_MOVE_DISTANCE


    def createcars(self):
        n=random.randint(1,6)
        if n==1:
            newcar=Turtle("square")
            newcar.shapesize(1,2)
            newcar.penup()

            newcar.color(random.choice(COLORS))
            newcar.goto(270,random.choice(Y))
            self.newcars.append(newcar)

    def move(self):
        # time.sleep(self.time)
        for car in self.newcars:
            car.backward(self.speed)

    def increasespeed(self):
        self.speed+=MOVE_INCREMENT
