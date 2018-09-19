import math
import heapq

class minHeap(object):
	def __init__(self, A=None):
		self.heap = A if A is not None else []

	def swap(self, x, y):
		temp = self.heap[x]
		self.heap[x] = self.heap[y]
		self.heap[y] = temp

	def heapify(self, i):
		left_idx = 2*i
		right_idx = (2*i) + 1
		smallest = i

		if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[i]:
			smallest = left_idx

		if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[smallest]:
			smallest = right_idx

		if smallest != i:
			self.swap(i, smallest)
			self.heapify(smallest)


	def build_heap(self):
		for i in reversed(range(0, len(self.heap)//2)):
			self.heapify(i)

	def insert(self, val):
		self.heap.append(val)

		# Bubble up
		curr = len(self.heap) - 1
		while curr > 0:
			parent = (curr-1)//2
			if self.heap[curr] < self.heap[parent]:
				self.swap(curr, parent)
				curr = parent
			else:
				break

	def extract_min(self):
		min_val = self.heap.pop(0)
		self.swap(0, len(self.heap)-1)
		self.heapify(0)
		return min_val

	def __repr__(self):
		return str(self.heap)


arr = [1, 3, 2, 10, 5, 2]
heap = minHeap(arr)
heap.build_heap()

print(heap)
heap.insert(0)
print(heap)
heap.insert(22)
print(heap)
ret = heap.extract_min()
print("returned {}".format(ret))
print(heap)

