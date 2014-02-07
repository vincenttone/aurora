#-*- coding:utf-8 -*-
from aurora.model.base import Base

class Article(Base):
    prefix = 'article'
    key = None
    id = None
    alias = ''
    title = ''
    content = ''
    def __init__(self, article = None):
        self.connect()
        if article is not None:
            self.set_article(article)

    def set_id(self, id):
        self.id = id
        self.key = self.prefix+':' + str(id)
        return self

    def set_alias(self, alias):
        self.alias = alias
        return self

    def set_title(self, title):
        self.title = title
        return self

    def set_content(self, content):
        self.content = content
        return self

    def set_article(self, article):
        self.set_id(article['id'])
        self.set_title(article['title'])
        self.set_alias(article['alias'])
        self.set_content(article['content'])
        return self

    def save(self):
        article = {
            'id': self.id,
            'title': self.title,
            'alias': self.alias,
            'content' : self.content
        }
        data = self.pack_json(article)
        self.redis.set(self.key, data)
        self.redis.rpush('article-id-list', str(self.id))
        return self

    def get(self):
        data = self.redis.mget(self.key)
        if data is not None:
            article = self.unpack_json(data[0])
            self.set_article(article)
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def get_title(self):
        return 'This is the first post'

    def get_alias(self):
        return 'the-first-post'

    def get_content(self):
        return 'hello, this is the content'


if __name__ == '__main__':
    a  = {
        'id' : 1,
        'title' : 'test',
        'alias' : 'test-alias',
        'content' : 'this is a content'
    }
    article = Article(a).save()
    x = article.get()
    print(x)
    print(article.content)
