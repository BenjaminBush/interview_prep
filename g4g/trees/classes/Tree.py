from classes.Node import *
from random import randint
import math
COUNT = 15
def generateTree():
	root = Node(randint(-5, 20))
	root.left = Node(randint(-5, 20))
	root.right = Node(randint(-5, 20))
	root.left.left = Node(randint(-5, 20))
	root.left.right = Node(randint(-5, 20))
	root.right.left = Node(randint(-5, 20))
	return root

def printTree(root):
	level0 = COUNT*" "
	print(level0 + "{}".format(root.data))
	level1 = (COUNT//2)*" "
	print(level1 + "{}".format(root.left.data) + level1 + level1 + "{}".format(root.right.data))
	level2 = ((COUNT//2)//2)*" "
	print(level2 + "{}".format(root.left.left.data) + level2 + level2 + "{}".format(root.left.right.data) + level2 + level2 + "{}".format(root.right.left.data))
  	


def printTree2(root):
	levels = getLevels(root)
	for i in range(levels):
		# get the count
		curr_count = COUNT
		curr_count//(math.pow(2, i))
		