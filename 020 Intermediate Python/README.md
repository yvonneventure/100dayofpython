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



### Local Files, Directories, Paths

<br>

> - [Day 24 Project - Mail Merger](Day%2024%20Project%20-%20Mail%20Merger)

<br>

### CSV Files ans Pandas Library

<br>

> - [Day 25 Project - United States Guessing Game](Day%2025%20Project%20-%20United%20States%20%20Guessing%20Game)
> - [Day 26 Project - NATO Alphabet](Day%2026%20Project%20-%20NATO%20Alphabet)


<br>

### Graphic User Interface (GUI) - TKinter

<br>

> - [Day 27 Project - Unit Converter](Day%2027%20Project%20-%20Unit%20Converter%20Use%20Tkinter)
> - [Day 28 Project - Pomodora Timer](Day%2028%20Project%20-%20Pomodora%20Timer)
> - [Day 29 & 30 Project - My Password Manager](Day%2029%2630%20Project%20-%20My%20Password%20Manager)
> - [Day 31 Project - Flash Cards](Day%2031%20Project%20-%20Flash%20Cards)

<br>

### SMTP Library to Send Emails

<br>

> - [Day 32 Project - Automate Birthday Email](Day%2032%20Project%20-%20Automated%20Birthday%20Email)

<br>


### Application Programming Interface (API) - Requests Library


<br>

> - [Day 33 Project - ISS Overhead Notifier](Day%2033%20Project-%20ISS%20Overhead%20Notifier)
> - [Day 34 Project - Quiz App](Day%2034%20Project%20-%20Quiz%20App)
> - [Day 35 & 36 Project - Stock Trading News SMS](Day%2035%2636%20Project%20-%20Stock%20Trading%20SMS)
> - [Day 37 Project - Habit Tracker Use Pixela](Day%2037%20Project%20-%20Habit%20Tracker)
> - [Day 38 Project - Workout Tracker Use Google Sheet](Day%2038%20Project%20-%20Workout%20Tracker%20Use%20Google%20Sheet)
> - [Day 39&40 Project - Flight Deal Finder](Day%2039%2640%20Project%20-%20Flight%20Deal%20Finder)

<br>

### Front-end Web Development - HTML & CSS

<br>

> - [Day 41 - 44 Project - Web Development with HTML/CSS](Day%2041%20to%2044%20Project%20-%20HTML%20%26%20CSS%20Web%20Devlopment)

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
> - [Day 49 Project - Automate LinkedIn Job Application]()
> - [Day 50 Project - Auto Tinder Swipe Bot]()
> - [Day 51 Project - Internet Speed Complaint Bot]()
> - [Day 52 Project - Instagram Follower Bot]()
> - [Day 53 Project - Data Entry Job Automation]()

<br>

### Back-end Web Development - Flask in Python

<br>

> - [Day 54 Project - ]()
> - [Day 55 Project - ]()
> - [Day 56 Project - ]()
> - [Day 57 Project - ]()

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
- [Find GIF on giphy.com](https://giphy.com)
- [HD wallpaper on Uplash.com](https://unsplash.com)
- [Free html templates (not for commercial use)](https://html5up.net)





