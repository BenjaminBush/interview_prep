#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:09:32 2017

@author: ben
"""

from classes.LinkedList import *

# 2.6 : Plaindrome. Implement a function to check if a linkedlist is a palindrome

def isPalindrome(linkedlist):
    stack = []

    fast = slow = linkedlist.head
    
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    
    # Odd number    
    if fast:
        slow = slow.next
        
    while slow != None:
        top = stack.pop()
        if slow.data != top:
            return False
        slow = slow.next
    return True
    

#-------------test----------------#
ll_true = LinkedList()
for i in range(1, 5, 1):
    ll_true.insert(i)
for i in range(5, 0, -1):
    ll_true.insert(i)
print(isPalindrome(ll_true))

ll_false = LinkedList()
ll_false.insert(5)
ll_false.insert(3)
ll_false.insert(1)

print(isPalindrome(ll_false))