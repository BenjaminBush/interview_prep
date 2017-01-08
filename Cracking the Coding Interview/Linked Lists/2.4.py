#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:56:42 2017

@author: ben
"""

from classes.LinkedList import *

# 2.4 : Partition. Write code to partition a linked list around a value x such that all nodes less than x come
# before all nodes greater than or equal to X. 

def partition(linkedlist, x):
    left = LinkedList(None)
    right = LinkedList(None)
    
    curr = linkedlist.head
    
    while curr.next != None:
        if curr.data < x:
            left.insert(curr)
        else:
            right.insert(curr)
        curr = curr.next
    
    right.insert(left)
    return right
    
        
    
    

#----------------test-----------------
L = randomLinkedList(10, 0, 50)
x = 25

print(L, " , x=25")
ret = partition(L, x)
print(ret)

