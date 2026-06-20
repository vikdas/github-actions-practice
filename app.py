# This code is from https://github.com/LondheShubham153/flask-app-ecs/tree/main
# this have been copied from londheshubham153 repo
from flask import Flask, render_template
app = Flask(__name__)

error introduced


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
