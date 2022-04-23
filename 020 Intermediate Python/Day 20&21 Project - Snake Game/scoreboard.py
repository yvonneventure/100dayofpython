from turtle import Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score: {self.score}", font=('Ariel', 24, 'normal'), align='center')


    def updatescore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=('Ariel', 24, 'normal'), align='center')

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over!", font=('Ariel', 24, 'normal'), align='center')
