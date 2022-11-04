from flask import Flask
import os
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


if __name__=='__main__':
    app.run()

