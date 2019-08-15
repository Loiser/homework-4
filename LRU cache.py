# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:28:07 2019

@author: 10539
"""
'''借助keys来记录时间顺序'''
class LRUcache:
    def __init__(self, size):
        self.cache = {}
        self.keys = []
        self.size = size

    def get(self, key):
        if key in self.cache:#现有的提到前面
            self.keys.remove(key)
            self.keys.insert(0, key)
            return self.cache[key]
        else:
            return None

    def set(self, key, value):
        if key in self.cache:#现有的提到前面
            self.keys.remove(key)
            self.keys.insert(0, key)
            self.cache[key] = value
        elif len(self.keys) == self.size:#满了就去除末尾前面加上新的
            old = self.keys.pop()
            self.cache.pop(old)
            self.keys.insert(0, key)
            self.cache[key] = value
        else:#
            self.keys.insert(0, key)
            self.cache[key] = value

if __name__ == '__main__':
    test = LRUcache(4)
    test.set('a',2)
    test.set('b',2)
    test.set('c',2)
    test.set('d',2)
    test.set('e',2)
    test.set('f',2)
    print(test.get('c'))
    print(test.get('b'))
    print(test.get('a'))
