#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:25:03 2017

@author: ben
"""
from random import randint

class Node (object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    # Insert a node at the head of the list and return pointer to head
    def insert(self, data = None):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return self.head
        
    # Get the size of the list
    def get_size(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next
        return total
        
    # Find a given value if it is in the list and return the node with that value
    def find(self, data):
        curr = self.head
        while curr.next != None:
            if curr.data == data:
                return curr
            else:
                curr = curr.next
        return None
    
    # Remove a given value from the list and return pointer to head 
    def remove(self, data):
        curr = self.head
        if curr.data == data:
            self.head = self.head.next
        while curr.next != None:
            if curr.data == data:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
        return self.head
        
        
        
    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.data)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.data))
            return "LinkedList  [ " + "->".join(nodestore) + " ]"
        return "LinkedList  []"
    
def randomLinkedList(length, min, max):
    ll = LinkedList()
    for i in range(length):
        value = randint(min, max)
        ll.insert(value)
    return ll