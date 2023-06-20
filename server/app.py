#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/<string:username>')
def user(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(port=5555)