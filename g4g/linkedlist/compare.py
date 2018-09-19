from classes.LinkedList import *

def compare(l1, l2):
	p1 = l1.head
	p2 = l2.head

	while p1.next != None and p2.next != None:
		if p1.data != p2.data:
			return False
		p1 = p1.next
		p2 = p2.next

	if p1 != None and p2 != None:
		if p1.data != p2.data:
			return False

	if p1.next != None:
		return False

	if p2.next != None:
		return False

	return True

list1 = LinkedList()
list1.add_tail('g')
list1.add_tail('e')
list1.add_tail('e')
list1.add_tail('k')
list1.add_tail('s')
list1.add_tail('2')

list2 = LinkedList()
list2.add_tail('g')
list2.add_tail('e')
list2.add_tail('e')
list2.add_tail('k')
list2.add_tail('s')
list2.add_tail('2')

print("List 1 and List 2 are the same? : {}".format(compare(list1, list2)))