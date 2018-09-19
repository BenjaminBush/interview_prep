from classes.LinkedList import *

# def reverse(self):
# 	curr = self.head
# 	prev = None
# 	while curr is not None:
# 		next = curr.next
# 		curr.next = prev
# 		prev = curr
# 		curr = next
# 	self.head = prev

ll = randomLinkedList(10, 0, 20)
print(ll)
ll.reverse()
print(ll)