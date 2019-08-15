# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:59:37 2019

@author: 10539
"""

class TrieNode(object):
    def __init__(self):
        self.data = {}
        self.is_word = False
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
            words=word+"_"
            node = self.root
            for letter in words:
                child = node.data.get(letter)#如果有则读
                if not child:
                    node.data[letter] = TrieNode()#如果没有则添加，使用类
                node = node.data[letter]
                node.is_word = True
    def search(self, word):
        node = self.root
        for letter in word+"_":
            node = node.data.get(letter)
            if not node:
                return False
        return node.is_word 
    def starts_with(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.data.get(letter)
            if not node:
                return False
        return True
    def get_start(self, prefix):
        def _get_key(pre, pre_node):
            words_list = []
            if pre_node.is_word:
                words_list.append(pre)
            for x in pre_node.data.keys():
                words_list.extend(_get_key(pre + str(x), pre_node.data.get(x)))
            return words_list
        words = []
        if not self.starts_with(prefix):
            return words
        if self.search(prefix):
            words.append(prefix)
            return words
        node = self.root
        for letter in prefix:
            node = node.data.get(letter)
            return _get_key(prefix, node)


if __name__ == "__main__":#主函数
    trie = Trie()
    wordsp=['and','if','how','an','apple']
    for word in wordsp:
        trie.insert(word)
    print(trie.search('anne'))

    
