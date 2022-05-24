# Advanced Level Python (Day 58 - Day 80)

<br>

### Bootstrap 5.1.3

All notes can be found [here]().

[Bootstrap 5.1.3 documentation]()

[Bootstrap 5.1.3 codes](Bootstrap5.1.3)

<br>

### Flask, WFT-Form, Jinja and Bootstrap 

[Flask 2.1 documentation](https://flask.palletsprojects.com/en/2.1.x/quickstart/)

[Jinja 3.0 documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)


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






### SQLite & SQL Alchemy
















