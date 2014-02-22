#-*- coding:utf-8 -*-
from aurora.model.base import Base

class Articles(Base):
    def __init__(self):
        self.connect()

    def get_ids(self, page = 1, count = 10):
        begin = (page - 1) * count
        end = (page * count) - 1
        ids = self.redis.lrange('article-id-list', begin, end)
        return ids

    def get_articles(self, page = 1, count = 10):
        ids = self.get_ids(page, count)
        keys = []
        articles = []
        for id in ids:
            keys.append('article:' + str(id))
        if (len(keys) == 0):
            return keys
        else:
            for data in self.redis.mget(*keys):
                articles.append(self.unpack_json(data))
            
        return articles

