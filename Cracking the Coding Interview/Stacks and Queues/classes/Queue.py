#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 18:57:17 2017

@author: ben
"""

class QueueNode(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class Queue(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def add(self, item):
        t = QueueNode(item)
        if self.last is None:
            self.last.next = t
        self.last = t
        if self.first is None:
            self.first = self.last
        
    def remove(self):
        if self.first is None:
            return None
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return data
        
    def peek(self):
        return self.first.data
    
    def isEmpty(self):
        return self.first is None