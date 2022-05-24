# Advanced Level Python (Day 58 - Day 80)

<br>

### Bootstrap 5.1.3

> All notes can be found [here]().
>
> [Bootstrap 5.1.3 documentation]()
>
> [Bootstrap 5.1.3 codes](Bootstrap5.1.3)

<br>

### Flask, WFT-Form, Jinja and Bootstrap 

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

### SQLite & SQLAlchemy
















