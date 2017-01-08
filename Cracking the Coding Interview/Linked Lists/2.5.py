#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:34:27 2017

@author: ben
"""

from classes.LinkedList import *

# 2.5 : Sum Lists. Two numbers represented by a linked list. Digits are stored in reverse order in a each node (7 -> 1 -> 6 = 617)
# Write a function that sums the two numbers and returns the total as a linked list (that is also in reverse order!)

def sum_lists(list1, list2):
    p1 = list1.head
    p2 = list2.head
  
    total1 = 0
    total2 = 0
    
    tens = 0
    
    # List1 walk
    while p1 != None:
        total1 += p1.data*(10**tens)
        tens += 1
        p1 = p1.next

    tens = 0
    
    # List2 walk
    while p2 != None:
        total2 += p2.data*(10**tens)
        tens += 1
        p2 = p2.next
    
    total = total1 + total2
    
    total = str(total)
    
    ret = LinkedList(None)
    
    for i in range(0, len(total)):
        ret.insert(total[i])
    
    return ret

#----------test---------------------------#
l1 = randomLinkedList(3, 0, 9)
l2 = randomLinkedList(3, 0, 9)

print(l1)
print()
print(l2)
print()
print("sum lists is " + str(sum_lists(l1, l2)))