from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

screen.colormode(255)

turtle.speed(0)
def randcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def circle(angle):
    for i in range(int(360/angle)):
        turtle.pencolor(randcolor())
        turtle.circle(100)
        turtle.setheading(turtle.heading()+angle)



circle(5)





screen.exitonclick()

