#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def au_entry():
    return 'hello world!'

@app.route('/article/<path:action>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def au_article(action):
    # get article config
    # get post put delete article
    return action

if __name__ == '__main__':
    app.run()
