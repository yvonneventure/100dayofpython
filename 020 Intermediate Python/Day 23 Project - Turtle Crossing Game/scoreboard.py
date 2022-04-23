FONT = ("Courier", 24, "normal")
from turtle import Turtle
SCORE =0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.score=SCORE
        self.write(f"Level: {self.score}",align="left",font=FONT)

    def updatescore(self):
        self.clear()
        self.score+=1
        self.write(f"Level: {self.score}", align="left", font=FONT)
    def gameover(self):
        self.goto(-20, 0)
        self.write("Game Over!", align="center", font=FONT)


