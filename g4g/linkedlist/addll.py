from classes.LinkedList import *

def add_lists(l1, l2):
	p1 = l1.head.next
	p2 = l2.head.next
	l1_data = []
	l2_data = []
	while p1.next != None and p2.next != None:
		l1_data.append(p1.data)
		l2_data.append(p2.data)
		p1=p1.next
		p2=p2.next

	if p1 != None and p2 != None:
		l1_data.append(p1.data)
		l2_data.append(p2.data)

	while p1.next != None:
		l1_data.append(p1.data)
		p1 = p1.next
	while p2.next != None:
		l2_data.append(p2.data)
		p2 = p2.next


	l1_data = reversed(l1_data)
	l2_data = reversed(l2_data)

	sum_ = 0
	i = 0

	for el in l1_data:
		sum_ += el*(10**i)
		i+=1
	i = 0
	for el in l2_data:
		sum_ += el*(10**i)
		i += 1

	return sum_

list1 = LinkedList()
list1.add_tail(1)
list1.add_tail(0)
list1.add_tail(0)
list1.add_tail(0)

list2 = LinkedList()
list2.add_tail(2)
list2.add_tail(4)

print(add_lists(list1, list2))


