#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:48:59 2017

@author: ben
"""

from classes.LinkedList import *

# 2.3 : Delete Middle Node. Implement an algorithm to delete a node in the middle, given only access to that node

# We can't actually unlink that node from the linkedlist because we don't have previous pointers
# We can, however copy the value from the next node and unlink that node

def delete_middle_node(linkedlist, node):
    if node.next != None:
        node.value = node.next.data
        node.next = node.next.next
    else:
        node.value = None
        
#-----------test------------------------#        
L = randomLinkedList(5, 0, 100)
node = L.head.next         # Given access to the 3rd node
print(L)
print("After deleting the node")
delete_middle_node(L, node)
print(L)