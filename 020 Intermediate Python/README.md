# Intermediate Level Python (Day 15 - Day 57)

<br>

### Local Development Setup - PyCharm

<br>

> [Day 15 Project - Coffee Machine](Day%2015%20Project%20-%20Coffee%20Machine)

<br>

### Object Oriented Programming 

<br>

 > - [Day 16 Project - Coffee Machine OOP](Day%2016%20Project%20-%20Coffee%20Machine%20OOP)
 > - [Day 17 Project - Quiz Game](Day%2017%20Project%20-%20The%20Quiz%20Game)

<br>

### Graphic User Interface (GUI) - Turtle

<br>

> - [Day 18 Project - Dots Artwork Mirror Damien Hirst](Day%2018%20Project-%20Dots%20Artwork%20Mirror%20Damien%20Hirst)
> - [Day 19 Project - Turtle Race Game](Day%2019%20Project%20-%20Turtle%20Race)
> - [Day 20 & 21 Project - Pong Game](Day%2020%2621%20Project%20-%20Snake%20Game)
> - [Day 22 Project - Snake Game](Day%2022%20Project%20-%20Pong%20Game)
> - [Day 23 Project - Turtle Crossing Game](Day%2023%20Project%20-%20Turtle%20Crossing%20Game)

<br>

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
def hello_world():
    return 'Goodbye!'

## now when we go to 'homepage/bye' we will see "Goodbye" rendered.


## __main__ refers to hello.py, by doing below, we don't need to use "Flask run" in terminal
## we can now run and stop by using button
if __name__ == '__main__':
    app.run()
    
```































