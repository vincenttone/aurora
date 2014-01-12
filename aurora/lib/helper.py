# -*- coding:utf-8 -*-

def singleton(klass, *args, **kw):
    instances = {}
    def _wraper():
        if klass not in instances:
            instances[klass] = klass(*args, **kw)
        return instances[klass]
    return _wraper
