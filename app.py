#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask
from flask import request, redirect, url_for, render_template
from aurora.app.article import Article

app = Flask(__name__)

@app.route('/')
def au_entry():
    a = Article()
    articles = a.get_articles()
    return render_template('article/index.html', articles=articles)

@app.route('/article/new', methods=['GET'])
def au_artile_new():
    return render_template('article/edit.html')

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
