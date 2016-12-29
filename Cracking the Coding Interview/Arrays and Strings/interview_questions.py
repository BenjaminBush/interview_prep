#!/usr/bin/python3.5

# 1.1 : Implement an algorithm to determine if a string has all unique characters
# What if you cannot use additional data structures?

def isUnique(string):
	used_chars = {}
	for char in string:
		if char in used_chars:
			return False
		else:
			used_chars[char] = 1
	return True


# 1.2 : Given two strings, write a method to decide if one is a permutation of the other
def isPermutation(str1, str2):
	char_count1 = {}
	for char in str1:
		if char in char_count1:
			char_count1[char] += 1
		else:
			char_count1[char] = 1
	for char in str2:
		if char not in char_count1 or char_count1[char] < 1:
			return False
		else:
			char_count1[char] = char_count1[char] - 1
	return True

# 1.3 : Write  amethod to replace all spaces in a string with '%20'
def urlify(string):
	return string.replace(' ', '%20')


# 1.4 : Given a string, write a function to check if it is a permutation of palindrome
from itertools import permutations
def palindromePermutation(string):
	string = string.lower().replace(' ', '')
	perms = permute(string)
	for perm in perms:
		if isPalindrome(perm):
			return True
	return False

def permute(string):
	return [''.join(p) for p in permutations(string)]

def isPalindrome(string):
	for i in range(0, len(string)/2):
		if string[i] != string[len(string) - i - 1]:
			return False
	return True

def secondSolution(string):
	bitVector = createBitVector(string)
	return bitVector == 0 or checkExactlyOneBitSet(bitVector)
def createBitVector(string):
	bitVector = 0
	for char in string:
		x = getCharNumber(char)
		bitVector = toggle(bitVector, x)

	return bitVector
def toggle(bitVector, index):
	if index < 0:
		return bitVector
	mask = 1 << index
	if bitVector & mask == 0:
		bitVector |= mask
	else:
		bitVector &= mask
	return bitVector
def getCharNumber(char):
	a = ord('a')
	z = ord('z')
	val = ord(char)
	if a <= val and val <= z:
		return val - a
	return -1
def checkExactlyOneBitSet(bitVector):
	return (bitVector & (bitVector - 1)) == 0

# 1.5 : There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to see if they are
# one or zero edits away
def editsAway(string1, string2, n):
	diff = len(string1) - len(string2)
	diff = abs(diff)
	# Accounts for all insert/replace cases
	if diff > n:
		return False

	# Get the shorter and longer string
	if len(string1) < len(string2):
		s1 = string1
		s2 = string2
	else:
		s1 = string2
		s2 = string1

	index1 = 0
	index2 = 0
	foudDifference =  False
	while index1 < len(s1) and index2 < len(s2):
		if s1[index1] != s2[index2]:
			if foudDifference:
				return False
			foudDifference = True

			# Equal length strings --> replace --> increment the shorter
			if len(s1) == len(s2):
				index1 += 1
		else:
			index1 += 1
		index2 += 1

	return True

# 1.6 : Implement a method to perform basic string compression using the counts
# of repeated characters. 
def strCompression(string):
	original_length = len(string)
	compressed = ""
	curr_count = 0
	for i in range(0, len(string) - 1):
		curr_count += 1
		if i == len(string) - 2:
			final_char = string[len(string) - 1]
			if string[i] == final_char:
				curr_count += 1
				compressed = compressed + string[i] + str(curr_count)
			else:
				compressed = compressed + string[i] + str(curr_count) + final_char + str(1)
			break
		if string[i] != string[i+1]:
			compressed = compressed + string[i] + str(curr_count)
			curr_count = 0

	final_length = len(compressed)
	if original_length < final_length:
		return string
	else:
		return compressed

