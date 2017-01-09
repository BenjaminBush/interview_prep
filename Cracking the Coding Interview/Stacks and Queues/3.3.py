#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 20:17:06 2017

@author: ben
"""
from classes.Stack import *

class SetOfStacks(object):
    def __init__(self, capacity):
        self.capacity =  capacity
        self.stacks = []
        
    def push(self, value):
        # Check if we need to allocate another stack
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        
        # Append the new value to the last stack
        self.stacks[-1].append(value)
        
    def pop(self):
        if len(self.stacks) == 0:
            return None
        # Get the data
        data = self.stacks[-1].pop()
        # If the pop causes us to not need another stack, then pop that stack from the list
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        
        return data
    
    def popAt(self, index):
        if index < 1 or index > len(self.stacks) or len(self.stacks[index-1]) == 0:
            return None
        return self.stacks[index-1].pop()
#--------------test--------------------------------#

setofstacks = SetOfStacks(8)
for i in range(24):
    setofstacks.push(i)
    print(i, )
    
for i in range (5):
    print("Popped", setofstacks.pop())
    
print("test for popAt")

for i in range (5):
    for i in range(3):
        print("popped" , setofstacks.popAt(i+1))