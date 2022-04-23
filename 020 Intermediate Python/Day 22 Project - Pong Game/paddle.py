from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self,position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)

    def up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)
        #