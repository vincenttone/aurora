#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def au_entry():
    return '项目首页'

@app.route('/article/<path:action>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def au_article(action):
    # get article config
    # get post put delete article
    return action

if __name__ == '__main__':
    app.run()
