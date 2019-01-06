"""
2.3 Delete Middle Node

Implement an algo to delete a node in the middle (i.e. any node but the first
and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node.

EXAMPLE
input: the node c from the linked list a->b->c->d->e->f
result: nothing is returned, but new linked list looks like a->b->e->f
"""

from LinkedList import *

def delete_middle_node(node):
	node.value = node.next.value
	node.next = node.next.next



if __name__ == "__main__":
	ll = LinkedList()
	ll.add_multiple([1, 2, 3, 4])
	middle_node = ll.add(5)
	ll.add_multiple([7, 8, 9])

	print(ll)
	print("Middle node to delete: ", middle_node)
	delete_middle_node(middle_node)
	print(ll)