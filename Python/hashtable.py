#!/usr/bin/python3
import math
import random
import string

class hashtable(object):
    '''
    Hash table implementation using open addressed hashing and some load balancing
    '''
    def __init__(self, max_size=None):
        if max_size is None:
            self.max_size = 2
        else:
            self.max_size = None
        self.hashtable = [None]*self.max_size
        self.loadfactor = 0
        self.num_records = 0

    def toHashKey(self, s):
        A = 1952786893
        B = 367257
        v = B

        for j in range(len(s)):
            c = s[j]
            v = A*(v+ord(c)+j)+B
        if v < 0:
            v = -v
        return v

    def baseHash(self, key):
        A = (math.sqrt(5)-1)/2
        return int(math.floor(len(self.hashtable)*(key*A - math.floor(key*A))))

    def stepHash(self, key):
        e =  math.exp(1)
        A = e/4
        stepHashValue = int(math.floor(len(self.hashtable)*(key*A - math.floor(key*A))))
        if stepHashValue % 2 == 0:
            stepHashValue += 1
        return stepHashValue

    def insert(self, key, value):
        if self.loadfactor >= 0.5:
            self.rehash()

        i = 0

        slot = self.baseHash(self.toHashKey(key))
        stepVal = self.stepHash(self.toHashKey(key))

        while (self.hashtable[slot] is not None and not self.hashtable[slot] == "deleted" and i < len(self.hashtable)):
            slot += stepVal
            slot = slot % len(self.hashtable)
            i += 1

        if i < len(self.hashtable):
            self.hashtable[slot] = [key, value]
            self.num_records += 1
            self.loadfactor = self.num_records/len(self.hashtable)
            return True
        else:
            return False


    def rehash(self):
        old_table = self.hashtable

        self.max_size = self.max_size*2
        self.hashtable = [None]*self.max_size
        self.num_records = 0

        for slot in old_table:
            if slot is not None and not slot[0] == "deleted":
                self.insert(slot[0], slot[1])

    def find(self, key):
        i = 0
        hashkey = self.toHashKey(key)

        base = self.baseHash(hashkey)
        stepVal = self.stepHash(hashkey)

        slot = base % len(self.hashtable)

        while i < len(self.hashtable) and self.hashtable[slot] is not None:
            if self.hashtable[slot][0] == key:
                return self.hashtable[slot]
            slot += stepVal
            slot = slot % len(self.hashtable)
            i += 1
        return None

    def remove(self, key):
        i = 0
        hashkey = self.toHashKey(key)
        base = self.baseHash(hashkey)
        stepVal = self.stepHash(hashkey)

        slot = base % len(self.hashtable)

        while i < len(self.hashtable) and self.hashtable[slot] is not None:
            if self.hashtable[slot][0] == key:
                self.hashtable[slot][0] = "deleted"
                return True
            slot += stepVal
            slot = slot % len(self.hashtable)
            i += 1
        return False



if __name__=='__main__':
	# Basic functionality testing
    key1 = "hello"
    value1 = 1

    key2 = "world"
    value2 = 2

    stringtable = hashtable()
    stringtable.insert(key1, value1)
    stringtable.insert(key2, value2)

    ret = stringtable.find(key1)
    print(ret)

    ret2 = stringtable.remove(key1)
    print(ret2)

    ret = stringtable.find(key1)
    print(ret)

    # Have some fun
    max_num = 100000
    for i in range(max_num):
        random_len = random.randint(1, 20)
        random_key = ''.join(random.choice(string.ascii_lowercase) for i in range(random_len))
        random_value = random.randint(0, max_num)
        stringtable.insert(random_key, random_value)
        if i % 1000 == 0:
            print('Processed {} requests'.format(i))

        # Plot rehash as a function of number of requests for validation