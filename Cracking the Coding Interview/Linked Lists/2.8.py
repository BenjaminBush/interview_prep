#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 17:07:23 2017

@author: ben
"""

from classes.LinkedList import *

# 2.8 : Loop Detection. Given a circular linked list, implement an algorithm that returns the node
# at the beginning of the loop


def detect_loop(linkedlist):
    fast_p = linkedlist.head
    slow_p = linkedlist.head
    
    while fast_p.next != None and fast_p != None and fast_p is not slow_p:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if fast_p == slow_p:
            break
    
    if fast_p is None or fast_p.next is None:
        return None
    
    # They are caught up and Loop Size - k nodes into the list
    
    # Move slow to head and advance them both slowly now
    slow_p = linkedlist.head
    while slow_p is not fast_p:
        slow_p = slow_p.next
        fast_p = fast_p.next
    
    return slow_p
    