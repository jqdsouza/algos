"""
2.2 Return kth to Last

Implement an algorithm to find the kth to last element of a singly linked list
"""

from LinkedList import *

def kth_to_last(ll, k):
	if ll.head is None:
		return None
		
	runner = curr = ll.head

	# set runner k nodes ahead
	for i in range(k):
		if runner is None:
			return None
		runner = runner.next

	while runner:
		curr = curr.next
		runner = runner.next
	
	return curr

if __name__ == "__main__":
	ll = LinkedList()
	ll.generate(10, 0, 9)
	print(ll)
	print(kth_to_last(ll, 3))
