from flask import Flask, render_template
import datetime
import random
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    random_num=random.randint(0,10)
    today=datetime.date.today().year
    return render_template('index.html',num=random_num,curr_year=today)

@app.route('/<name>')
def username(name):
    cname = name.capitalize()
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    return render_template('guess.html',cname=cname,gender=gender,age=age )

@app.route('/blog/<num>')
def get_blog(num):
    posts= requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template('blog.html',posts=posts)

if __name__ == '__main__':
    app.run(debug=True)









