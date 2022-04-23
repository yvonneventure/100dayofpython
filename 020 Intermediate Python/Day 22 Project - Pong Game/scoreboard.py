from turtle import Turtle, Screen

class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.updatescore()



    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, font=("Courier", 80, "normal"), align="center")
        self.goto(100, 200)
        self.write(self.rscore, font=("Courier", 80, "normal"), align="center")

    def addl(self):
        self.lscore+=1
        self.updatescore()

    def addr(self):
        self.rscore+=1
        self.updatescore()
