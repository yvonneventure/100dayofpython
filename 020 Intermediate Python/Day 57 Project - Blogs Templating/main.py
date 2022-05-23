from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()

@app.route('/')
def home():
    data=post.data
    return render_template("index.html",data=data)


@app.route('/post/<num>')
def go_to_post(num):
    no=int(num)-1
    title = post.data[no]["title"]
    body = post.data[no]["body"]
    subtitle = post.data[no]["subtitle"]

    return render_template("post.html",title=title, body=body,subtitle=subtitle)


if __name__ == "__main__":
    app.run(debug=True)
