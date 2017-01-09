#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:06:35 2017

@author: ben
"""


# 3.2 : Stack Min. Implement a function min() which returns the minimum element
# of the stack. This should operate in O(1) time
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 18:52:03 2017

@author: ben
"""
class StackNodeWithMin(object):
        def __init__(self, data, min_val, next):
            self.data = data
            self.min_val = min_val
            self.next = next

# Storage is an array with element 0 = data and the rest is a list of the rest of the stack --> keep track of the minimum at every "state" --> local min is storage in [1] [2] is next
class StackWithMin(object):
    def __init__(self, top):
        self.top = top
        
    def push(self, item):
        new_min = min(item, self.get_min())
        t = StackNodeWithMin(item, new_min, self.top)
        self.top = t
        
    def pop(self):
        item = self.top.data
        self.top = self.top.next
        return item

    
    def peek(self):
        return self.top.data
    
    def isEmpty(self):
        return self.top == None
        
    def get_min(self):
        return self.top.min_val
        
#--------------test-----------------------$
from random import randrange
top = StackNodeWithMin(101, 101, None)
S1 = StackWithMin(top)
test_list = [randrange(100) for x in range(10)]
for num in test_list:
	S1.push(num)

for i in range(len(test_list) - 1):
	print("new pop", S1.pop())
	print("new min", S1.get_min())