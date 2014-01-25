#-*- coding:utf-8 -*-
from base import Base
from base import render_template

class Content(Base):
    prefix = 'content'
    key = None
    id = None
    title = ''
    content = ''
    img = ''
    time = ''
    

    def __init__(self, article = None):
        self.connect()
        if article is not None:
            self.set_article(article)

     def set_img(self, img):
        self.img = img
        return self

    def set_title(self, title):
        self.title = title
        return self

    def set_content(self, content):
        self.content = content
        return self

    def set_centent(self, content):
        self.set_title(content['title'])
        self.set_img(content['img'])
        self.set_content(content['content'])
        return self

    def save(self):
        content = {
            'title': self.title,
            'img': self.alias,
            'content' : self.content
        }
        data = self.pack_json(content)
        self.redis.set(self.key, data)
        return self

    def get(self):
        data = self.redis.mget(self.key)
        if data is not None:
            article = self.unpack_json(data[0])
            self.set_content(article)
            return True
        else:
            return False

    def get_title(self):
        return 'This is the first post'

    def get_img(self):
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
    print x
    print article.content
