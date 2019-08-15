# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:07:56 2019

@author: 10539
"""

'''
用数组存链表相当于额外开辟的存储冲突值的尾巴
233333

'''
class ListNode:
    def __init__(self, value, pnext=None):
        self.data = value
        self.next = pnext
        
class HashTable:

    def __init__(self, p):
        self.array = [None] * p
        self._div = p
        
    def hashFun(self, key):
        return key % self._div
    
    def insert(self, value):
        '''
        采用前插法将value作为结点插入到哈希表的链表中，
        若当前链表不存在，则创建一个链表再继续插入该结点
        :param value: 结点的值
        '''
        key = self.hashFun(value)
        if self.array[key] is None:
            self.array[key] = ListNode(None)
            node = ListNode(value)
            self.array[key].next = node
        else:
            node = ListNode(value)
            node.next = self.array[key].next
            self.array[key].next = node
    
    def showTable(self):
        for index in range(self._div):
            if self.array[index]:
                p = self.array[index].next
                print('%d：' % index)
                while p:
                    print(p.data,end='—>')
                    p = p.next
                print('\n')