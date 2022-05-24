# Advanced Level Python (Day 58 - Day 80)

<br>

### Bootstrap 5.1.3

All notes can be found [here]().

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




















