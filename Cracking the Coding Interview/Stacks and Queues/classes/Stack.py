#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 18:52:03 2017

@author: ben
"""
class StackNode(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack(object):
    def __init__(self, top):
        self.top = top
        
    def pop(self):
        item = self.top.data
        self.top = self.top.next
        return item
    
    def push(self, item):
        t = StackNode(item)
        t.next = self.top
        self.top = t
    
    def peek(self):
        return self.top.data
    
    def isEmpty(self):
        return self.top == None
        