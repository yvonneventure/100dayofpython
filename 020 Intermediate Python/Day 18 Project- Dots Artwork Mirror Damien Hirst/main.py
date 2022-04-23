#
# import colorgram
#
# color=colorgram.extract('spots.png',30)
# colorlist = []
# for i in color:
#     rgb = i.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     colorlist.append((red,green,blue))
#
#
#
# print(color)
# print(colorlist)


##### above steps are to get the below color list #####
from turtle import Turtle, Screen
import random

screen = Screen()
t = Turtle()
screen.colormode(255)


list = [(210, 158, 84), (172, 50, 79), (47, 98, 148), (226, 209, 108), (225, 233, 231), (136, 90, 66), (116, 175, 202), (212, 132, 174), (163, 169, 52), (200, 74, 121), (226, 74, 56), (85, 109, 192), (72, 160, 71), (126, 218, 207), (53, 57, 90), (43, 132, 93), (117, 45, 72), (224, 172, 189), (132, 182, 155), (177, 185, 216), (229, 174, 164), (158, 206, 216), (83, 148, 159), (51, 54, 72), (100, 51, 43), (47, 73, 76), (44, 78, 75)]
t.penup()
t.hideturtle()
t.goto(-200,-250)
t.speed(0)

for n in range(10):
    x=-200
    y=int(t.ycor())
    y+=50
    t.goto(x,y)
    for i in range(10):
        #print(t.position())
        screen.colormode(255)
        color=random.choice(list)
        t.pendown()
        t.dot(20,color)
        t.penup()
        t.fd(50)

print(t.position())
screen.exitonclick()