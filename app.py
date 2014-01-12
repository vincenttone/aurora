#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask
from flask import request
from aurora.app.article import Article

app = Flask(__name__)

@app.route('/')
def au_entry():
    return '项目首页'

@app.route('/article/<action>')
def au_article(action):
    if request.method == 'GET':
        article = Article()
        aid = action
        return article.get_article_by_id(aid)
    else:
        return action

if __name__ == '__main__':
    app.run(debug=True)
