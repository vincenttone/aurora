#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask
from flask import request
from aurora.app.article import Article

app = Flask(__name__)

@app.route('/')
def au_entry():
    return '项目首页'

@app.route('/article/new', methods=['GET'])
def au_artile_new():
    article = Article()
    return article.new()

@app.route('/article/create', methods=['POST'])
def au_artile_create():
    title = request.form['title']
    alias = request.form['alias']
    content = request.form['content']
    return content
    

if __name__ == '__main__':
    app.run(debug=True)
