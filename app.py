#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask
from flask import request, redirect, url_for
from aurora.app.article import Article
from aurora.app.listBox import ListBox

app = Flask(__name__)

@app.route('/')
def au_entry():
    return '项目首页'

#首页入口文件
@app.route('/listBox/index',methods=['GET'])
def au_listBox_entry():
    listbox = ListBox
    return listbox.new()

@app.route('/article/new', methods=['GET'])
def au_artile_new():
    article = Article()
    return article.new()

@app.route('/article/<id>', methods=['GET'])
def au_article_get_by_id(id):
    article = Article()
    a = article.get_article_by_id(id)
    if a is None:
        abort(404)
    else:
        return a.content

@app.route('/article/create', methods=['POST'])
def au_artile_create():
    title = request.form['title']
    alias = request.form['alias']
    content = request.form['content']
    article = Article()
    a = article.create(title,alias,content)
    return redirect(url_for('au_article_get_by_id', id=a.get_id()))

if __name__ == '__main__':
app.run(debug=True)
