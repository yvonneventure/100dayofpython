from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
ubet = screen.textinput(title="Make a Bet", prompt="Which turtle will win? Enter a color: ")
race = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
name = ["a","b","c","d","e","f"]

basey = -180
for i in range(6):
    name[i] = Turtle(shape="turtle")
    name[i].color(colors[i])
    name[i].penup()
    basey+=50
    name[i].goto(x=-230, y=basey)

if ubet:
    race = True
while race:
    for turtle in name:
        if turtle.xcor() > 230:
            race = False
            if turtle.pencolor()==ubet:
                print(f"You win! The winning turtle is in color {turtle.pencolor()}")
            else:
                print(f"You lose! The winning turtle is in color {turtle.pencolor()}")
        turtle.fd(random.randint(0,10))


screen.exitonclick()

