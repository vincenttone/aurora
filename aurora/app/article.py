#-*- coding:utf-8 -*-

class Article:
    id = None
    alias = ''
    title = ''
    content = ''
    def init(self, article = None):
        if article is not None:
            self.set_article(article)

    def set_id(self, id):
        self.id = id
        return self

    def set_alias(self, alias):
        self.alias = alias
        return self

    def set_title(self, title):
        self.title = title
        return self

    def set_content(self, title):
        self.content = content
        return self

    def set_article(self, article):
        self.id = article['id']
        self.title = article['title']
        self.alias = article['alias']
        self.content = article['content']
        return self

    def get_id(self):
        return self.id

    def get_title(self):
        return 'This is the first post'

    def get_alias(self):
        return 'the-first-post'

    def get_content(self):
        return 'hello, this is the content'
