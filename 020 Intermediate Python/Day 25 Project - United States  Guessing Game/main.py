import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
#add the image as a tutle shape
image="blank_states_img.gif"
screen.addshape(image)

timmy=turtle.Turtle()
timmy.penup()
timmy.hideturtle()
turtle.shape(image)
############
#get the x, y coodinates for mouse click on screen, listen to the mouse click and print x, y
# ####since the teacher gave us the x,y coordinated already in csv file, we will not be using below blcok
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

############
states=pandas.read_csv("50_states.csv")

score=0
correct=[]
for i in range(50):
#add an answer prompt
    answer=screen.textinput(title=f"Guess {score}/50 correct states",prompt="What's another state's name?")
    answer=answer.title()
    row=states[states.state==answer]
    if answer=="Exit":
        break

    # if row.empty==True:
    #     pass
    if row.empty==False:
        score+=1
        correct.append(answer)
        #print(row)
        xcor = int(row.x)
        ycor = int(row.y)
        state=str(row.state)
        timmy.goto(xcor,ycor)
        timmy.write(answer,align="center",font=("Ariel",10,"normal"))









#turtle.mainloop()  #keep the screen open
