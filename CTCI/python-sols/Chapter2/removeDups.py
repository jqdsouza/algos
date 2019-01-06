"""
2.1 Remove Dups

Write code to remove duplicates from an unsorted linked list

FOLLOW UP: 
How would you solve this problem if a temporary buffer is not allowed?
"""
from LinkedList import *

def remove_dups(ll):
	if ll.head is None:
		return
	
	curr = ll.head
	vals_seen = set([curr.value])

	while curr.next:
		if curr.next.value in vals_seen:
			curr.next = curr.next.next

		else:
			vals_seen.add(curr.next.value)
			curr = curr.next
		
	return ll

def remove_dups_followup(ll):
	if ll.head is None:
		return

	curr = ll.head

	while curr:
		runner = curr

		while runner.next:
			if runner.next.value == curr.value:
				runner.next = runner.next.next 
			else:
				runner = runner.next 
		
		curr = curr.next

	return ll.head

if __name__ == "__main__":
	ll = LinkedList()
	ll.generate(10, 0, 9)
	print(ll)
	remove_dups(ll)
	print(ll)

	ll.generate(10, 0, 9)
	print(ll)
	remove_dups_followup(ll)
	print(ll)
