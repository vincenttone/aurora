# -*- coding:utf-8 -*-
from flask import render_template
from aurora.model.article import Article as ArticleModel
from aurora.lib.ticket import Ticket
from aurora.model.articles import Articles as ArticlesModel

class Article():
    def new(self):
        return render_template('article/edit.html')

    def get_article_by_id(self, id):
        article = ArticleModel()
        if article.set_id(id).get():
            return article
        else:
            return None

    def get_articles(self, page=1, count=10):
        am = ArticlesModel()
        articles = am.get_articles(page, count)
        return articles

    def create(self,title,alias,content):
        id = Ticket().get_ticket()
        acticle = ArticleModel()
        acticle.set_article( {'id':id,'title':title,'alias':alias,'content':content})
        return acticle.save()
