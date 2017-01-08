#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:50:44 2017

@author: ben
"""
from classes.LinkedList import *   

# 2.1 Write code to remove duplicates from an unsorted linked list
def remove_dups(linkedlist):
    curr = linkedlist.head
    if curr != None:
        dict = {curr.data : True}
        while curr.next != None:
            if curr.next.data in dict:
                curr.next = curr.next.next
            else:
                dict[curr.next.data] = True
                curr = curr.next
                
                
#------------test-----------------------#
ll = randomLinkedList(10, 1, 10)
print(ll)
remove_dups(ll)
print(ll)
ll2 = randomLinkedList(20, 3, 5)
print(ll2)
remove_dups(ll2)
print(ll2)
            