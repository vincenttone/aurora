# -*- coding:utf-8 -*-
from aurora.model.article import Article as ArticleModel
class Article:
    def get_article_by_id(self, id):
        article = ArticleModel()
        return article.set_id(id).get_content()
