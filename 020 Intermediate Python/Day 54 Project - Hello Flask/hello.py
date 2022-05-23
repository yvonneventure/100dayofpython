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

