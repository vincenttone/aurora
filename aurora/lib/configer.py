# -*- coding:utf-8 -*-
from helper import singleton

@singleton
class Configer:
    a = 0
    def make_redis_config(self, config):
        a = config
        pass

if __name__ == '__main__':
    c1 = Configer()
    c1.a = 10
    print c1.a

    c2 = Configer()
    print c2.a
