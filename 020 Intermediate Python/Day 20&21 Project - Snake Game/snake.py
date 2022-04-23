POS = [(0,0),(-20,0),(-40,0)]
RIGHT = 0
DOWN = 270
UP = 90
LEFT = 180

from turtle import Turtle

class Snake:


    def __init__(self):

        self.snake = []

        self.createsnake()

    def createsnake(self):
        for i in POS:
            self.addseg(i)

    def addseg(self,position):
        newturtle = Turtle("square")
        newturtle.speed(0)
        newturtle.color("white")
        newturtle.penup()
        newturtle.goto(position)
        self.snake.append(newturtle)
        self.head = self.snake[0]

    def extend(self):
        self.addseg(self.snake[-1].position())


    def move(self):
        for n in range(len(self.snake) - 1, 0, -1):
            newx = self.snake[n - 1].xcor()
            newy = self.snake[n - 1].ycor()
            self.snake[n].goto(newx, newy)
        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
