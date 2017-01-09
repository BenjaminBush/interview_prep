#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:02:26 2017

@author: ben
"""

# 3.1 : Three in One. Describe how you could use a single array to implement three stacks

#==============================================================================
# We could implement this using fixed size stacks. For example, given an array of size n
# we allocate the first n/3 elements for the first stack, the next n/3 elements for the second stack,
# and the last n/3 elements for the third stack. We would need to maintain one array of all of the collective
# values, and also an array of the the sizes of each of the stacks so that we could tell the index of the top
# of the stack
#==============================================================================
