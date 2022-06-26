# Advanced Level Python (Day 58 - Day 80)

<br>

## Bootstrap 5.1.3

> All notes can be found [here]().
>
> [Bootstrap 5.1.3 documentation]()
>
> [Bootstrap 5.1.3 codes](Bootstrap5.1.3)

<br>

## Flask, WFT-Form, Jinja and Bootstrap 


> - [Day 58-60 Project - Upgraded Blog Website](Day%2058-60%20Project%20-%20Upgraded%20Blog%20w%20Bootstrap): Flask & Bootstrap
> - [Day 61 Project - FlaskWTforms: Advanced Contact Form](Day%2061%20Project%20-%20FlaskWTForms) 
> - [Day 62 Project - Coffee & Wifi](Day%2062%20Project%20-%20Coffee%20and%20Wifi)

<br>

> [Flask 2.1 documentation](https://flask.palletsprojects.com/en/2.1.x/quickstart/)
>
> [Jinja 3.0 documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)


- To reduce the repeatition, make a seperate `header.html` and `footer.html`, then add below lines every other html files to include the templates use jinja.

```html
{% include 'header.html' %}
    Body
{% include 'footer.html' %}
```

- Render static files in html files use jinja

```html
 <header class="masthead" style="background-image: url('{‌{ url_for('static', filename='img/contact-bg.jpg')}}')">
 
<!-- Bootstrap core CSS -->
<link href="{‌{ url_for('static', filename='vendor/bootstrap/css/bootstrap.min.css') }}" rel="stylesheet">

<!-- Custom fonts for this template -->
<link href="{‌{ url_for('static', filename='vendor/fontawesome-free/css/all.min.css')}}" rel="stylesheet" type="text/css">
<link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

<!-- Custom styles for this template -->
<link href="{‌{ url_for('static', filename='css/clean-blog.min.css')}}" rel="stylesheet">
   
```

- HTML method in Flask

In html, create a simple html form with action and method.

```html
<!--  to make our HTML form submit a "POST" request to the path "/login"-->

<!-- in order for our python server to catch the post requests, we need to add "name" attribute to each input-->
<form action="/login" method="post">    <!-- can also use <form action="{‌{ url_for('receive_data') }}" method="post"> -->
    
        <label>Name</label>
        <input type="text" placeholder="name" name="username">
        <label>Password</label>
        <input type="text" placeholder="password" name="password">
        <button type="submit">Ok</button>
    </form>
   
```

then in our python server:

```python
from flask import Flask, render_template, request

@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]   ## get the username from html form and pass into our server
    password = request.form["password"]
    ## can also use `data = request.form` then `name=data["username"]`
    return f"<h1>Name: {name}, Password: {password}</h1>"

```

- Check which html method used

In python:

```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
```

In html, different text will be rendered.

```html
{% if msg_sent: %}
            <h1>Successfully sent your message</h1>
            {% else: %}
            <h1>Contact Me</h1>
            {% endif %}
```

#### Flask [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)

- `Requirements.txt`

The requirements.txt file is a file where you can specify all the dependencies (the installed packages that your project depends on) and their versions. This means that you can share your project without all the installed packages, making it a lot more lightweight. When someone downloads your project , the requirements.txt file tells their code editor which packages need to be installed. [Read more on this here.](https://docs.google.com/document/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub)

> [Example requirements file](requirements.txt)

#### Why use Flask-WTF


- Easy Form Validation - Makes sure the user is entering data in the required format in all the required fields. e.g. checking that the user's email entry has a "@" and a "." at the end. All without having to write your own validation code.

- Less Code - If you have a number of forms in your website, using WTForm can dramatically reduce the amount of code you have to write (or copy & paste).

- Built in CSRF Protection - CSRF stands for Cross Site Request Forgery, it's an attack that can be made on website forms which forces your users to do unintended actions (e.g. transfer money to a stranger) or compromise your website's security if it's an admin.

```python

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

# form = FlaskForm(meta={'csrf': False})  ## shut down csrf

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()],Email())
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"   ## required
Bootstrap(app)

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():  ## validate when user hit submit
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":  
        ## get hold of inputted data can be easy as login_form.email.data
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)
```

Then in html file

```html
<form method="POST" action="{{ url_for('login') }}">
			    {{ form.csrf_token }}
			    <p>
				{{ form.email.label }} <br> {{ form.email(size=30) }}
			    </p>
			    <p>
				{{ form.password.label }} <br> {{ form.password(size=30) }}
			    </p>
			    {{ form.submit }}
			</form>
```

#### Inherit templates

Template inheritance is similar to Class inheritance, you can take a parent template and extend its styling in your child web pages.

For example, if we create a base.html file that has the following code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

It has predefined areas (or blocks) where new content can be inserted by a child webpage inheriting from this template.

1. We could re-write the success.html page to inherit from this base.html template:

```html
#1.
{% extends "base.html" %}
#2.
{% block title %}Success{% endblock %}
#3.
{% block content %}
   <div class="container">
      <h1>Top Secret </h1>
      <iframe src="https://giphy.com/embed/Ju7l5y9osyymQ" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
      <p><a href="https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ">via GIPHY</a></p>
   </div>
{% endblock %}
#1. This line of code tells the templating engine (Jinja) to use "base.html" as the template for this page.
#2. This block inserts a custom title into the header of the template.
#3. This block provides the content of the website. The part that is going to vary between webpages.
```

- Super Blocks

When we inherit from Python classes, you often see `super.init()`. The super keyword refers to the parent that the child is inheriting from.

When we are inheriting templates. Sometimes, there's some part of the template that we want to keep, but we also want to add to it. So we can use super blocks in this case.

3. Add the following code to your base.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <style>
{% block block_name %}  <!--now all pages use this base.html template will have a background color of purple-->
body{
    background: purple;
}
{% endblock %}
</style>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

Now you can see how easy it is to modify all web pages in your website if you use the same template. But what if on the sucess page we also wanted to make the` <h1>` red? We would need to modify the internal styling in the `<style>` tag. But that code is in the base.html template. Luckily we have super blocks.
    
4. On the success.html page, add a super block using `{‌{ super() }}`, this will inject all the code in the styling block to this child page. Then afterwards before the `{% endblock %}`, we can add some more styling to change the colour of the `<h1>`.

```html
{% extends "base.html" %}
{% block title %}Success{% endblock %}
{% block block_name %}
	{{ super() }}   <!-- inherited super -->
	<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">   <!-- get css stylesheet -->
	h1 {
		color:red;    <!-- update/overwrite h1 tag-->
	}
{% endblock %}
{% block content %}
	<div class="container">
		<h1>Success </h1>
		<iframe src="https://giphy.com/embed/1xeVd1vr43nHO" width="480" height="271" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
		<p><a href="https://giphy.com/gifs/cheezburger-funny-dog-fails-1xeVd1vr43nHO">via GIPHY</a></p>
	</div>
```

#### [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html)

- Flask-Bootstrap quick form


```python
from flask_bootstrap import Bootstrap

Bootstrap(app)

```

In html file other than base.html , change to `{% extends 'bootstrap/base.html' %}`

To add a quick form, first import at the top, then add one-line ` {{ wtf.quick_form(form) }}` at where you want the form.

```hmtl
{% import "bootstrap/wtf.html" as wtf %}

{{ wtf.quick_form(form, novalidate=True) }} 
<!-- `novalidate=True` is to shut down the default browser validation, as the wtforms already have validation -->

```


Another example of using wtf

```python
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_secret_key'
Bootstrap(app)


class CafeForm(FlaskForm):   ## create dropdown field with labels and chocies
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))                                      ## redirect 
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
```



<br>

## SQLite & SQLAlchemy

> - [Day 63 Project - Virtual Bookshelf](Day%2063%20Project%20-%20Virtual%20Bookshelf-%20SQLite%20%26%20SQLAlchemy)
> - [Day 64 Project - TOP 10 Movies](Day%2064%20Project%20-%20TOP%2010%20movies)

#### - SQLite

```python
import sqlite3
db = sqlite3.connect("books-collection.db")     ## create a database if not exists

cursor = db.cursor()    ## create a cursor to control (edit,add,delete) data in database

## create table "books"

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# four fields are created : "id","title","author","rating"
#1. id INTEGER PRIMARY KEY -  This is the first field, it's a field called "id" which is of data type INTEGER and it will be the PRIMARY KEY for this table. This field is not required, can be generated automatically.

#2. title varchar(250) NOT NULL UNIQUE -  This is the second field, it's called "title" and it accepts a variable-length string composed of characters. The 250 in brackets is the maximum length of the text. NOT NULL means it must have a value and cannot be left empty. UNIQUE means no two records in this table can have the same title.

#3. author varchar(250) NOT NULL -  A field that accepts variable-length Strings up to 250 characters called author that cannot be left empty.

#4. rating FLOAT NOT NULL -  A field that accepts FLOAT data type numbers, cannot be empty and the field is called rating.

### Add data to database

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

```

#### - [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)

SQLAlchemy is defined as an ORM Object Relational Mapping library. This means that it's able to map the relationships in the database into Objects. Fields become Object properties. Tables can be defined as separate Classes and each row of data is a new Object. 

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
db.create_all()


#CREATE RECORD
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)

##NOTE: When creating new records, the primary key fields is optional. you can also write:
##new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)

db.session.add(new_book)
db.session.commit()

#Read All Records
all_books = session.query(Book).all()


#Read A Particular Record By Query
book = Book.query.filter_by(title="Harry Potter").first()


#Update A Particular Record By Query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()  

#Update A Record By PRIMARY KEY
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()  


#Delete A Particular Record By PRIMARY KEY
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()

## You can also delete by querying for a particular value e.g. by title or one of the other properties.

```

- Working with any new database technology is how to **CRUD** data records : **Create, Read, Update, Delete**.


## Web Design

> Notes and project will be [here](https://github.com/yvonneventure/web-design/blob/main/Principles%20for%20web%20design.md)

- Color Theory
- Typography
- UI design
- UX design


## Build REST API Use Flask

### REST (**RE**presentational **S**tate **T**ransfer)

1. Use HTTP Request Verbs (Get, Post, Put/Patch, Delete)

> Similar to database CRUD (Create, Read, Update, Delete)

#### Put vs Patch

- Put : Replace the entire entry
- Patch: Replace only pieces of data

2. Use specific Pattern of Routes/Endpoint URLs

<img width="591" alt="Screen Shot 2022-06-25 at 09 42 48" src="https://user-images.githubusercontent.com/103771536/175776190-5cb681b1-18c2-4a84-aac2-45b4d125e29d.png">

> Use [Postman](https://www.postman.com/postman/workspace/) to test API Endpoints and generate API documentation


## Day 67

What if a user manipulated the webpage and wrote <script> evil script</script> inside the article?

Bleach is a good Python tool for sanitizing html inputs before storing inside the DB or rendering inside the template.

You should never declare raw user inputs as |safe without any measures taken server-side. See https://ckeditor.com/docs/ckeditor4/latest/guide/dev_best_practices.html#filter-content-server-side .

```python
import bleach
 
## strips invalid tags/attributes
def strip_invalid_html(content):
    allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul']
 
    allowed_attrs = {
        'a': ['href', 'target', 'title'],
        'img': ['src', 'alt', 'width', 'height'],
    }
 
    cleaned = bleach.clean(content,
                           tags=allowed_tags,
                           attributes=allowed_attrs,
                           strip=True)
 
    return cleaned
 
## use strip_invalid_html-function before saving body
body=strip_invalid_html(article.body.data)
 
## you can test the code by using strong-tag
```

> HTML forms (WTForms included) do not accept PUT, PATCH or DELETE methods. We can update the database and re-render the items in database to have the same effect.




## Authentication with Flask

The most important component of a website is having users. Real humans who can contribute to the website. If Facebook had no users then it would just be adverts. If blogs had no users then it would just be the ramblings of an author.

But in order to have users and associate data to user accounts, we need a way to register them and allow them to sign back into their accounts at a later date.

Restrict Access with different user status (ie. different subscription).


### Encrytion & Hashing

Levels of security:

- Level 1 : Simply store plain text in server

- Level 2 (Encryption) : Password + Key with cipher method, then we end up with some ciphertext

> Limitation is that encrytion needs key, which is not that secure if the hacker is motivated enough.

- Level 3 (Hashing) : Password with a hash function will produce a Hash and we will store the hash in the server. Hash function is a mathematical function that will take no time going forward, but almost impossible going backward. Meaning it may take 1 millisecond to hash it, but may take 2 years to decode it. Hashing also doesn't need a key.

> [plaintextoffenders: ](https://plaintextoffenders.com)a list of companies will email your password back to you when you want to reset your password, which we learnt in hashing that it's impossible to get the plain text of your password. This means that their websites are not secure.

- Level 4 (Salting): Adding random characters to user's password to generate the hash. We will only store the salt and the Hash in the database. MD5 is the most easiest hash to be hacked. Now the industry standard is bcrypt and also use Salt Rounds. 

Salt Rounds: First we use password and a random set of salt to generate Hash, then we take this Hash and add the same salt agin and create another Hash, then do this again and again. This is called Salt Rounds. In this case, we only store the salt and end Hash in the database. Once user input the password, we will use the salt stored in database, and hash the same number of rounds and compare with the end hash stored in database, if it's a match then we have our user verified.

> - [Cryptii](https://cryptii.com)
> - [YouTube Video: Enigma Machine - Numberphile](https://www.youtube.com/watch?v=G2_Q9FoD-oQ)
> - [YouTube Video: Flaw in the Enigma Code - Numberphile](https://www.youtube.com/watch?v=V4V2bpZlqx8)
> - [Book: The Code Book by Simon Singh](https://www.torontopubliclibrary.ca/search.jsp?Ntt=The+code+book)


### Hacking Passwords 101

> - [Check if your password got hacked](https://haveibeenpwned.com)
> - [List_of_the_most_common_passwords](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords)
> - [Password Complexity Checker](http://password-checker.online-domain-tools.com)

❗️The longer the password, the time hacking will increase exponentially (recomended 12+ characters.
❗️Don't use words in dictionary.

For fun, you can use https://hackertyper.net to mess up with your friends, you can type anything but it will produce something seems realistic.


[Use werkzeug to hash and salt user's password.](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security)




















