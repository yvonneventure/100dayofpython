from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0) #turn off animation, only show up when call screen.update()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")


#create paddle
lpaddle = Paddle((-350,0))
rpaddle = Paddle((350,0))
#create ball
ball = Ball()
scoreboard=ScoreBoard()


screen.update()

screen.listen()
screen.onkey(rpaddle.up,"Up")
screen.onkey(rpaddle.down,"Down")
screen.onkey(lpaddle.up,"w")
screen.onkey(lpaddle.down,"s")
game = True
while game:
    screen.update()

    time.sleep(ball.movespeed)
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()
    if (ball.distance(rpaddle) <50 and ball.xcor() >320) or (ball.distance(lpaddle) <50 and ball.xcor() <-320):
        ball.bouncex()
    if ball.xcor()>380:
        ball.resetpos()
        scoreboard.addl()
    if ball.xcor()<-380:
        ball.resetpos()
        scoreboard.addr()



screen.exitonclick()