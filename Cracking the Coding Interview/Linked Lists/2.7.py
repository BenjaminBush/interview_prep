#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:30:33 2017

@author: ben
"""

from classes.LinkedList import *

# 2.7 : Intersection. Given two singly linked lists determine if the two lists intersect and return the intersecting node

# nb : intersection is based on reference, not value

def intersection(list1, list2):
    length1 = list1.get_size()
    length2 = list2.get_size()
    
    if length1 > length2:
        longer = list1
        shorter = list2
    else:
        longer = list2
        shorter = list1
        
    
    longer_p = longer.head
    shorter_p = shorter.head
    
    for i in range(abs(length1-length2)):
        longer_p = longer_p.next
    
    while shorter_p is not longer_p:
        shorter_p = shorter_p.next
        longer_p = longer_p.next
    
    return longer_p
    
    
#---------test------------#

i1 = Node(5, None)
i2 = Node(7, None)
i3 = Node(1, None)


l1 = LinkedList()
l1.insert(i3)
l1.insert(i2)
l1.insert(i1)
l1.insert(9)
l1.insert(3)

l2 = LinkedList()
l2.insert(i3)
l2.insert(i2)
l2.insert(i1)
l2.insert(4)
l2.insert(3)

print(l1)
print(l2)

print(intersection(l1, l2))

