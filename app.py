#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask
from flask import request
from aurora.app.article import Article

app = Flask(__name__)

@app.route('/')
def au_entry():
    return '项目首页'

@app.route('/article/new')
def au_artile():
    article = Article()
    return article.new()

if __name__ == '__main__':
    app.run(debug=True)
