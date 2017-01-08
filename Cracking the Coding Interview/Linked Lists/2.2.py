#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:38:58 2017

@author: ben
"""

from classes.LinkedList import *

# 2.2 : Implement an algorithm to find the kth tolast element of a singly linked list
def kth_to_last(linkedlist, k):
    length = linkedlist.get_size()
    if k > length:
        return None
    if k == length:
        return linkedlist.head
    
    curr = linkedlist.head
    for i in range(length-k):
        curr = curr.next
    
    return curr.data
        
#-------------test--------------------------------#
ll1 = randomLinkedList(8, 1, 5)
print(ll1)
print(kth_to_last(ll1, 3))