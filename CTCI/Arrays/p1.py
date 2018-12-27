# Implement an algorithm to determine if a string has all unique characters without using additional data structures

def isunique(s):
    seen = []
    for char in s:
        if char in seen:
            return False
        else:
            seen.append(char)

def unique(s):
    s = sorted(s)
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            return False
        i+=1
    return True

print(unique("ben"))