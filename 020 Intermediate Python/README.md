# Intermediate Level Python (Day 15 - Day 57)

<br>

### Local Development Setup - PyCharm

<br>

> [Day 15 Project - Coffee Machine](Day%2015%20Project%20-%20Coffee%20Machine)

<br>

- [PEP 8 – Style Guide for Python Code:](https://peps.python.org/pep-0008/) 
  - promotes consistency and clarity, and help other developers better understand your code



### Object Oriented Programming (OOP) & Graphic User Interface (GUI) - [Turtle](https://docs.python.org/3/library/turtle.html)

<br>

> - [Day 16 Project - Coffee Machine OOP](Day%2016%20Project%20-%20Coffee%20Machine%20OOP): Modify Day 15 Project code to use OOP, instead of Procedual Programming
> - [Day 17 Project - Quiz Game](Day%2017%20Project%20-%20The%20Quiz%20Game) : Build own class
> - [Day 18 Project - Dots Artwork Mirror Damien Hirst](Day%2018%20Project-%20Dots%20Artwork%20Mirror%20Damien%20Hirst) 
> - [Day 19 Project - Turtle Race Game](Day%2019%20Project%20-%20Turtle%20Race) : Create multiple objects from class
> - [Day 20 & 21 Project - Snake Game](Day%2020%2621%20Project%20-%20Snake%20Game) : Class Inheritance
> - [Day 22 Project - Pong Game](Day%2022%20Project%20-%20Pong%20Game)
> - [Day 23 Capstone Project - Turtle Crossing Game](Day%2023%20Project%20-%20Turtle%20Crossing%20Game)

<br>

#### Object Oriented Programming


- Why use **Object Oriented Programming**?

  - So far what we've done are just **procedural programing**, where program runs from top to bottom and jump to function whenever called. When relationships get complex, it's hard to manage and remember them.


  - OOP breaks down the problems and each person/team works on the individual object and can work simutaniously to promote productivity.

  - Also, these objects are often reuseble for another future project.

  - eg. A project of creating an automated car can be broken into navigation, camera, lane direction, .etc modules and each team can work on individual module/object at the same time. In the future, when we want to build a drone, some of the modules can be reused too.

<br>

- How to use OOP?

  - **Class**: A blueprint, multiple objects can be generated from the class that have same function

  - **Attributes**: Variables in object - what object has 

  - **Methods**: Functions in object  - what object can do

  - eg. Waiter is a class, then objects can be Henry the waiter and James the waiter, the attribute can be `can_hold_plates=True`, the method can be  `def take_orders():`
 
<br>

- Create an object from class `car= CarBluePrint()`, Class name has to be pascal case 

> - pascal case: MyFirstScript
> - camel case: myFirstScript
> - snake case: my_first_script

<br>

```python

#import class Turtle and Screen from module turtle
#Turtle is a class and it has first letter capitalized
from turtle import Turtle, Screen

#ben is the name of the object, created/constructed from Turtle class (class is a blueprint)
ben = Turtle()
print(ben)
ben.shape("turtle")
ben.fillcolor("chartreuse4")
ben.fd(100)

myscreen = Screen()
#calling object's attribute/variable : without '()'
print(myscreen.canvheight)
#calling object's methods/fuctions: with '()'
myscreen.exitonclick()

```

> [turtle package documentation](https://docs.python.org/3/library/turtle.html)


- Create Own Class in Python
  - Create own attributes/variables in class
  - Create methods/functions in class
  
  
```python
###### Class and Constructor ######

# create a class called User, the name of the class should be pascal case
class User:
    #initialize or constructor : everytime the object of the class calls, this def block will be executed
    #can be used to set up the default value, or default attributes that object will use repeatly
    def __init__(self, id, name):  #(self) here means the object name when object= Class()
        self.id = id
        self.name = name      #name and id variable must be passed when object calls a class
        self.follower = 0    #default value of follower attribute/variable
        self.following = 0
    def follow(self,user):     #similar to create function like other place, but always have self as a parameter
        self.following += 1
        user.follower += 1

# let's say a instagram case where has user name, id and can follow other people
user1 = User(1,"kate")
user2 = User(2,"UG")
user1.follow(user2)           #user1 follow user2
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)
```

<br>


#### GUI - Turtle

- Turtle challenge 1 : draw shapes with random color


```python
#draw shapes with random color
from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

screen.colormode(255)

for i in range(3, 11):
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    turtle.pencolor(r,g,b)
    for n in range(i):
        turtle.fd(100)
        turtle.right(360/i)


screen.exitonclick()
```
- Turtle challenge 2 : draw random walk

```python
#draw random walk
from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

screen.colormode(255)
angles = [0, 90, 180, 270]

for i in range(50):
    screen.colormode(255)
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    turtle.pencolor(r,g,b)
    turtle.pensize(15)
    turtle.setheading(random.choice(angles))
    turtle.fd(30)

screen.exitonclick()
```

- Turtle challenge 3 : draw Spirograph

```python
#draw Spirograph
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
```

<br>

- Python **Tuple** (eg.`(1,2,8)`)
    - Tuple is like a list, and has order, but cannot change the value inside or make any changes


<br>

- Event Listener: listen to user's key press or mouse click


```python
####event listener : listen to user's key press or mouse click
from turtle import Turtle, Screen
t=Turtle()
screen = Screen()

def moveforward():
  t.forward(10)
## first listen, then specify the function and action
screen.listen()
screen.onkey(key="space",func="moveforward")
##calling function as a parameter doesn't need '()'

```

<br>

- Create multiple objects from same class

```python
###Turtle race : multiple instances/objects from same Class - create multiple turtles from Turtle class and control different turtles
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
```

<br>

- Class Inheritance

```python
import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()    ## inherit all methods and attributes from parent class Turtle
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        randomx = random.randint(-280, 280)
        randomy = random.randint(-280, 280)
        self.goto(randomx, randomy)
```

<br>

- List & Tuple slicing

```python
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_keys[1:])
print(piano_keys[:5])
print(piano_keys[1:5:2])   #every other element
print(piano_keys[::-1])    #print from right to left, reverse the order

print(piano_tuple[:5])
print(piano_tuple[1:])
print(piano_tuple[1:5:2])
```



### Local Files, CSV Files ans Pandas Library

<br>

> - [Day 24 Project - Mail Merger](Day%2024%20Project%20-%20Mail%20Merger)
> - [Day 25 Project - United States Guessing Game](Day%2025%20Project%20-%20United%20States%20%20Guessing%20Game): GUI & CSV
> - [Day 26 Project - NATO Alphabet](Day%2026%20Project%20-%20NATO%20Alphabet) : CSV


<br>

#### Local files, directory, file path

- Absolute File Path vs. Relative File Path
   - For mac, absolute file path starts with Macintosh, starts with "/": `/Users/xxx/PycharmProjects/`; 
   - For windows, it's C drive 
   - Relative file path starts with your working directory/folder, starts with "./" : `./Day 24/`
   - if we want to get to the parent folder `../Applications/`
   - `../../xxx`  : going up two levels

- Open files and create files

```python
# ----There are 2 ways of opening file -------#

# 1st way:
"""is to open the file from backend , and
the file will take up space in your computer, and you should always remember
to close it """

file = open("my_file.txt")
contents = file.read()   #content will be a string
print(contents)
file.close()

# 2nd way is easier, as you don't need to close the file
##  - mode default is "r" as read mode, won't be able to make changes
##  - mode="w"  --> write mode, will delete everythin existed and write
##  - mode="a"  --> append mode, will append the text onto the existing text
with open("my_file.txt",mode="a") as f:
    contents = f.read()
    print(contents)
    f.write("\nsomething")


# * when in "w"(write) mode, if the file you want to open doesn't exist, it will create it for you; "a" append mode will also create the file 

with open("newfile.txt",mode="w") as m:
    m.write("a")
    
file.readlines()  ##--> return a list and each line will be an element in the list
string.lstrip()  ##--->like trim(), also get rid off the new line \ n
string.replace()

```
<br>

#### CSV file and [Pandas Library](https://pandas.pydata.org/docs/reference/index.html)

- DataFrame vs. Series
  - Two dimension data(Table) is called "DataFrame"
  - One dimension data (Column) is called "series"

```python

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))

# table here is a two-dimension, called "data frame"
print(data["temp"])   #get the column by using column name
print(type(data["temp"]))

# one column is one-dimensional, called "series"
mean= data["temp"].max()
print(mean)

# Get data in columns
print(data["temp"])
print(data.temp)    #like an attribute in an object

# Get data in row

print(data[data.temp==data.temp.max()])   #gettting row by filter with a condition


# Create dataframe from scratch

data_dic={
    "students" : ["Amy","Bob","Cathy"],
    "score": [76,56,65]
}
#create dataframe from dictionary, where the key become colum name, and each list becomes a series --> so basically, passing each series
score=pandas.DataFrame(data_dic)
print(score)
```

<br>

#### List Comprehension & Dictionary Comprehension

<br>

- List Comprehension
  - Simpler way to create list then a complete for loop
  - Works for list, string, dictionary, range, tuples, etc 


```python
## work with list
list = [1,2,3]
new = [n+1 for n in list]

##work with string to create a list
name = "angela"
new = [letter for letter in name]

##work with range to create a list
r=range(1,5)
new = [n*2 for n in r if n==2]

#=> this equals to below full for loops
r=range(1,5)
new = []
for n in r:
  if n==2:
    n*=2
    new.append(n)
    
```

<br>

- Dictionary Comprehension

```python
##create dicitonary from list (list, string, tuple,dictionary....)
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list=sentence.split()
result={ word: len(word) for word in list }
print(result)



##create dictionary from dictionary
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f={
  weekday: (temp_c * 9/5) + 32 for (weekday,temp_c) in weather_c.items()
}
print(weather_f)

```

<br>

- List comprehension in Pandas DataFrame

```python
###loop through dataframe through pandas iterrow() function
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
#   #Access index and row
#   #Access row.student or row.score
#    pass

# Keyword Method with iterrows()
 {new_key:new_value for (index, row) in dataframe.iterrows()}

```

<br>       




### Graphic User Interface (GUI) - [TKinter](https://docs.python.org/3/library/tkinter.html#the-packer)

<br>

> - [Day 27 Project - Unit Converter](Day%2027%20Project%20-%20Unit%20Converter%20Use%20Tkinter)
> - [Day 28 Project - Pomodora Timer](Day%2028%20Project%20-%20Pomodora%20Timer)
> - [Day 29 & 30 Project - My Password Manager](Day%2029%2630%20Project%20-%20My%20Password%20Manager)
> - [Day 31 Project - Flash Cards](Day%2031%20Project%20-%20Flash%20Cards)

<br>

#### `*args` and `**kwags`

- `*args` is a tuple data type, for createing unlimitated ***positional*** arguments in function, position matters
- `**kwargs` is a dictionary data type, to create unlimited ***keyword*** arguments

```python
##create a function with unlimited positional arguments
#  args is a tuple data type, position matters
def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum

print(add(1,2,3,4,5))

##create a function with unlimited keyword arguments
def calculate(n, **kwargs):   #kwargs is a dictionary data type
    print(type(kwargs))
    for key,value in kwargs.items():  #go through the dictionary and find what you need
        print(key)
        print(value)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiple"]
    print(n)
calculate(2,add=3,multiple=5)

####use **kwargs in class
class Car:
    def __init__(self,**kwargs):
        #self.model=kwargs["model"]  -->Compared with the below line, this will return an error if no input of "model" comes in, which doesn't fit the feature of kwags as optional arguments, so should be use the below line 
        #Below way is better to get the value of the key, if there's no this key exits, it will return "None", rather than an error        
        self.model = kwargs.get("model")  
        self.car = kwargs.get("car")

mycar=Car(model="nissan",car="GTR")
print(mycar.model)
```

<br>

#### GUI - Tkinter

- [TK Commands](http://tcl.tk/man/tcl8.6/TkCmd/contents.htm)
- [TKinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Tk Canvas documentation](https://tkdocs.com/tutorial/canvas.html)

```python
## Use Tkinter
from tkinter import *  #import all classes in tkinster

window=Tk()
window.title("Unit Converter")
window.minsize(500,300)
window.after(1000,function) # after 1s, execute function

## with window.mainloop() on, we cannot use time.sleep()

# create label
label = Label(text="I am a lable",font=("Arial",24,"normal"))
label.pack()  # use this to show the label

# Use Image

img1=PhotoImage(file="file_path")
some_button= Button(image=img1,highlightthickness=0)  // to create a button from image, and get rid of the hightlight border

#create button
def buttonclick():
    label["text"]=entry.get()
    label.pack()
button=Button(text="click me",command=buttonclick)
button.pack()



#create entry

entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()  # like a while loop


#to show the widget we use either .pack() or .place(x= ,y= ) or .grid(colomn= ,row= )
##pack and grid cannot be used together
##pack is simply put things together from the top
##place is for specific x and y coordinates, can be very tideous (0,0) is top left
###grid is like a relative position, if top left is (column=0,row=0) then you can move the rest

## Create Canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

## To configure the window or the canvas, use .config
window.config(padx=0,pady=0,bg="color")
canvas.itemconfig(timer_text, text="00:00")

```

<br>


#### Exception Handling

- `try:` block is to try something that may go wrong and try to catch that exception
- `except:` block is to do somethin if exception happens, if not followed by specific error, it will catch all exceptions
- `else:` block is to do something if no exceptions in try block, which means the process can only execute except block or the else block, else and except cannot excute in the same run
- `finally:` block is to do something whether there's exception or not, so it will execute no matter what
- `raise:` will break the process and raise the exception

```python
### For example. FileNotFound error

try:  
  		file=open("a_file.txt")  #FileNotFound error
  		a_dic={"key":"value"}
  		print(a_dic["a"])   #KeyError, as there's no such key exists
except FileNotFoundError:
  		file=open("a_file.txt","w")
    	file.write("something")
except KeyError as error_message:   #catch the error message
  		print(f"The key {error_message} doesn't exist")
else:  #only execute when try block has no exceptions/errors
   	  content=file.read()
    	print(content)
finally:  #will execute no matter what
    	file.close()
    	print("file was closed.")
      
#raise exceptions, can be used with if 
raise KeyError  #this will break the program and show this error
raise TypeError("I made up this")    # break the program with this error message
  
```


<br>

### SMTP Library to Send Emails

<br>

> - [Day 32 Project - Automate Birthday Email](Day%2032%20Project%20-%20Automated%20Birthday%20Email)

<br>


```python
import smtplib
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        #make connection secure
        connection.starttls()
        connection.login(user=my_email,password=my_pw)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                        msg=f"Subject: Happy Birthday!\n\n {content}")
```

<br>

- Python **Datetime** Module

```python
#date time module in python
import datetime as dt

now=dt.datetime.now()
year= now.year()
month=now.month()
day_of_week = now.weekday()

print(now)

#create datetime object for birthdays
date_of_birth = dt.datetime(year=1993,month=10,day=31)
```

- Python type Hints & ->

```python
# the function check is expecting an integer input/parameters, and will output a boolean value

def check(age:int) -> bool :
  do something
  return yes
  
## this will make sure when you use the function, it will pop up type hints
```

<br>

### Application Programming Interface (API) - Requests Library


<br>

> - [Day 33 Project - ISS Overhead Notifier](Day%2033%20Project-%20ISS%20Overhead%20Notifier) :Basic API
> - [Day 34 Project - Quiz App](Day%2034%20Project%20-%20Quiz%20App): API & TKinter
> - [Day 35 & 36 Project - Stock Trading News SMS](Day%2035%2636%20Project%20-%20Stock%20Trading%20SMS)
> - [Day 37 Project - Habit Tracker Use Pixela](Day%2037%20Project%20-%20Habit%20Tracker)
> - [Day 38 Project - Workout Tracker Use Google Sheet](Day%2038%20Project%20-%20Workout%20Tracker%20Use%20Google%20Sheet)
> - [Day 39&40 Capstone Project - Flight Deal Finder](Day%2039%2640%20Project%20-%20Flight%20Deal%20Finder)

<br>



#### What's API?

<br>

  - just like teller between you and the bank vault, API is the teller, data is in vault and we need to tell teller, and teller may ask questions to verify us, also general information may don't need verification
  - API usually is an url, and website usually has an API documentation
  - to access website data/other system data, we need to make **requests**
  - **requests** are like rules or diff level of securities, not everyone can access the data
  - **API Endpoint** is where all the data located
  - In python, use [requests](https://docs.python-requests.org/en/latest/) module to work with API

```python
import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")   
response.raise_for_status()

## print response code
print(response)

# getting the data from the api endpoint
data =response.json()
print(data)

```

<br>

- API Parameters

Just like parameters in function, passing in different parameters allow to get different pieces of data.

Not all APIs have parameters, and some parameters are required, some are optional. Optional ones all have default value.

Parameters can be passed as a dictionary, with keys and values.

```python
parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
```

> URL before `?` is usually the API endpoint, after that, you can put in your parameters. If you see several URLs, you will find the pattern.

<br>

- [HTTP Response Codes Glossary](https://www.webfx.com/web-development/glossary/http-status-codes/) : eg. 404 website not found
    - 1XX : Hold on
    - 2XX: Sucess, here you go
    - 3XX: Go away
    - 4XX: You screwed up
    - 5XX: I (server) screwed up
 
 <br>
 
 > - JSON data is like a dictionary. Use this [json online viewer](http://jsonviewer.stack.hu/) to better see the structure of data
 > - Sometimes data will return [html entities](https://www.w3schools.com/html/html_entities.asp), to decode them first `import html` then `html.unescape('xxx')`
 > - A collective [list of APIs](https://apilist.fun/) to have fun


<br>

#### API Authentication, Keys, Headers

**API Key** is like your personal account and password, it allows the API provider to track how much you're using their API to grant you access or deny your access once you've gone over the limit.

<br>

**API Headers** 



#### HTTP Post requests, Put requests, Delete requests


<br>

#### Environment Variable

<br>

To see all your environment variables, type `env` in the terminal.

Environment variables can be easily updated without tapping into the codes. Also for security reason, you don't want your authentication keys visiable to others.

To create a ENV, type `export ENV_NAME="value"` then press enter, now you can see the environement variable you created in the list.

To access the ENV in our python code:

```python
import os
api_key=os.environ.get("ENV_NAME")
```

### Front-end Web Development - HTML & CSS

<br>

> - [Day 41 - 44 Project - Web Development with HTML/CSS](Day%2041%20to%2044%20Project%20-%20HTML%20%26%20CSS%20Web%20Devlopment)
> 
> All notes of Web Development are available at [my web-design repository.](https://github.com/yvonneventure/web-design)

<br>

### Web Scraping - Beautiful Soup Library

<br>

> - [Day 45 Project - 100 Movies You Must Watch](Day%2045%20Project-%20100%20Movies%20You%20Must%20Watch)
> - [Day 46 Project - Spotify Top 100 Songs](Day%2046%20Project%20-%20Spotify%20Top%20100%20Songs)
> - [Day 47 Project - Amazon Price Tracker](Day%2047%20project-%20Amazon%20Price%20Tracker)

<br>

### Automation & Web Scraping - Selenium Web Driver Library

<br>

> - [Day 48 Project - Cookie Game Playing Bot](Day%2048%20Project-%20Cookie%20Game%20Playing%20Bot%20Use%20Selenium)
> - [Day 49 Project - Automate LinkedIn Job Application](Day%2049%20Project-%20Automate%20LinkedIn)
> - [Day 50 Project - Auto Tinder Swipe Bot](Day%2050%20Project%20-%20Automate%20Tinder%20Swiping%20Bot)
> - [Day 51 Project - Internet Speed Complaint Bot](Day%2051%20Project%20-%20Internet%20Speed%20Twitter%20Complaint%20Bot)
> - [Day 52 Project - Instagram Follower Bot](Day%2052%20Project%20-%20Instagram%20Follower%20Bot)
> - [Day 53 Project - Data Entry Job Automation](Day%2053%20Project%20-%20Data%20Entry%20Job%20Automation)

<br>

### Back-end Web Development - Flask in Python

<br>

> - [Day 54 Project - Python Decorator](Day%2054%20Project%20-%20Python%20Decorator)
> - [Day 55 Project - Higher Lower URLs](Day%2055%20Project%20-%20Higher%20Lower%20URLs)
> - [Day 56 Project - My Personal Site](Day%2056%20Project%20-%20My%20Personal%20Site)
> - [Day 57 Project - Blog Templating use Jinja](Day%2057%20Project%20-%20Blogs%20Templating)

<br>

#### Intro to Flask

- Front-end languages : HTML, CSS, Javascript

- Back-end languages : Javascript, Python, Java, etc.

- Full-stack = Front-end + Back-end

- Frameworks: tools come with code pre-built for common used functions. 
  - Front-end: React, Angular, etc
  - Back-end: Node, Flask, etc

> [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) vs. Django
> - Flask is more for beginners and small projects
> - Django is more for larger commercial projects


[Framework vs. Library]()

The biggest difference is that we have to obey the rules of framework, so that framework can call our methods (rather than we call methods from library).

#### Command Line

- Shell : command lines or GUI to interface with Kernel (hardwares)
 - For Mac: Terminal app
 - For Windows: Command Prompt
 
 <br>

`pwd` ➡️ print working directory (where you are)

`ls`  ➡️ list all files and folders in your current working directory

`cd directory_name`  ➡️ change directory

`mkdir directory_name`  ➡️ make directory

`touch file_name.file_extension` ➡️ make file

`cd ..` ➡️ change to parent folder

`rm file_name.file_extension` ➡️ delete file

`rm -rf directory_name` ➡️  delete directory, directory cannot be deleted if you are in it


> ❗️ Be careful with `rm -rf`, it will delete everything in the folder and cannot be recovered;
> 
> ❗️ Also be careful of where you are, you may accidently delete everything in your computer and cannot be recovered

<br>

 [Command Line Cheatsheet (Mac)](https://github.com/appbrewery/terminal-mac-cheatsheet#english-version) or search "Terminal Cheatsheet" on Google

<br>


#### Python Decorator

<br>

Python Decorator : functions build on other function to allow for more functionality

<br>

```python
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()
```

<br>

#### Basic Flask App

<br>

```python

###Basic Flask App

from flask import Flask
app = Flask(__name__)

## python decorator function start with @

# '/' is homepage
@app.route('/')
def hello_world():
    return 'Hello, World!'
## 'Hello, World!' is render in local address and has a basic html structure

# we can do something similar
@app.route('/bye')
def bye():
    return 'Goodbye!'

## now when we go to 'homepage/bye' we will see "Goodbye" rendered.


## __main__ refers to hello.py, by doing below, we don't need to use "Flask run" in terminal
## we can now run and stop by using button
if __name__ == '__main__':
    app.run()
    
```

<br>

#### Advanced Python Decorator with variables and arguments

- [Flask Rules of variables](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)

<br>

```python
## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)
```

<br>



- [Render HTML files under Flask Framework](https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates)
  - Put html files under 'templates' folder

```python

from flask import Flask, render_template

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


```

<br>

- Render Static files (imgs, css files, etc)
  - 1. Put them under 'static' folder
  - 2. update the path in html file


<br>

> ❗️ Use google developer tool, in console, type in `document.body.contentEditable=true` and run, this will allow you to make changes to the website on the spot(none of the changes are saved and will be lost on refresh). And once you are done, save it as html file and render it then you can have a copy.






























## Related Reources

<br>

- [PyCharm Keyboard Shortcuts](https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html)
- [Pypi: Repository of Python Packages](https://pypi.org/)
- [clogram.py:](https://pypi.org/project/colorgram.py/#description) a python module to extract colors from image
- [pythonanywhere to host your python script on cloud and run it on sheduled time](https://www.pythonanywhere.com/)
- [json online viewer](http://jsonviewer.stack.hu/) to better see the structure of data
- [twilio: send SMS API](https://www.twilio.com/docs/sms/quickstart/python)
- [color palettes use color hunt](https://colorhunt.co/) : My favorite [color palette](https://colorhunt.co/palette/14832)
- A collective [list of APIs](https://apilist.fun/) to have fun
- [Find GIF on giphy.com](https://giphy.com)
- [HD wallpaper on Uplash.com](https://unsplash.com)
- [Free html templates (not for commercial use)](https://html5up.net)





