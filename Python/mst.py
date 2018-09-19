from collections import defaultdict
import sys

class minHeap(object):
	def __int__(self):
		self.array = []
		self.size = 0
		self.pos = []

	def newMinHeapNode(self, v, dist):
		minHeapNode = [v, dist]
		return minHeapNode

	def swapMinHeapNode(self, x, y):
		t = self.array[x]
		self.array[x] = self.array[y]
		self.array[y] = t

	def minHeapify(self, idx):
		smallest = idx
		left = idx*2
		right = (idx*2) + 1

		if left < self.size and self.array[left] < self.array[idx]:
			smallest = left
		if right < self.size and self.array[right] < self.array[smallest]:
			smallest = right

		if smallest != idx:
			self.pos[self.array[smallest][0]] = idx
			self.pos[self.array[idx][0]] = smallest
			self.swap(smallest, idx)
			self.minHeapify(smallest)

	def extractMin(self):
		if self.isEmpty():
			return

		root = self.array[0]
		lastNode = self.array[self.size -1]
		self.array[0] = lastNode

		self.pos[lastNode[0]] = 0
		self.pos[root[0]] = self.size -1

		self.size -=1
		self.minHeapify(0)

		return root

	def isEmpty(self):
		return self.size==0

	def decreaseKey(self, v, dist):
		i = self.pos[v]

		self.array[i][1] = dist

		while i > 0 and self.array[i][1] < self.array[(i-1)/2][1]:
			self.pos[self.array[i][0]] = (i-1)/2
			self.pos[self.array[(i-1)/2][0]] = i
			self.swapMinHeapNode(i, (i-1)/2)

			i = (i-1)/2

	def inMinHeap(self, v):
		return self.pos[v] < self.size

	