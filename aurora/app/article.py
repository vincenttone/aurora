# -*- coding:utf-8 -*-
from aurora.model.article import Article as ArticleModel
class Article:
    def get_article_by_id(self, id):
        article = ArticleModel()
        return article.set_id(id).get_content()

    def get_articles(self, page=1, count=10):
        acticles = AtcileModel()
        return articles

    def create_article(self):
        a = ArtilceModel()
        a.title = aaa
        a.content =aaa
        a.save()
        
