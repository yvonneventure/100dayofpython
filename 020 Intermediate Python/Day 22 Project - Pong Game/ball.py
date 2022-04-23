from turtle import Turtle


class Ball(Turtle):


    def __init__(self):

        super(Ball, self).__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1

    def move(self):

        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def bounce(self):
        self.ymove *= -1

    def bouncex(self):
        self.xmove *= -1
        self.movespeed*=0.9

    def resetpos(self):
        self.goto(0,0)
        self.bouncex()
        self.movespeed=0.1


