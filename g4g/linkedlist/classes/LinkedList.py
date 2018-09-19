from random import randint

class Node(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def set_data(self, new_val):
		self.data = new_val

	def get_data(self):
		return self.data

	def set_next(self, new_node):
		self.next = new_node

	def get_next(self):
		return self.next

	def __str__(self):
		return str(self.data)


class LinkedList(object):
	def __init__(self):
		self.head = Node()
		self.size = 0

	def get_head(self):
		return self.head

	def add_front(self, data):
		node = Node(data)
		if self.size == 0:
			self.head.next = node
			self.size += 1
		else:
			temp = self.head.next
			self.head.next = node
			node.next = temp
			self.size += 1

	def add_tail(self, data):
		node = Node(data)
		curr = self.head
		while curr.next != None:
			curr = curr.next

		curr.next = node
		self.size += 1

	def delete_pos(self, pos):
		i = 0
		curr = self.head
		while i < pos:
			curr = curr.next
			i+=1

		temp = curr.next.next
		del(curr.next)
		curr.next = temp
		self.size -= 1

	def get_size(self):
		return self.size

	def find(self, data):
		curr = self.head
		while curr.next != None:
			if curr.get_data() == data:
				return curr
			else:
				curr = curr.next
		return None

	def __str__(self):
	    index = self.head
	    if index.data == None:
	    	nodestore = []
	    else:
	    	nodestore = [str(index.data)]
	    while index.next != None:
	        index = index.next
	        nodestore.append(str(index.data))
	    return "LinkedList  [ " + "->".join(nodestore) + " ]"

def randomLinkedList(length, min, max):
	ll = LinkedList()
	for i in range(length):
		value = randint(min, max)
		ll.add_tail((value))
	return ll

