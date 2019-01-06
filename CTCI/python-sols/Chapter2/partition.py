"""
2.4 Partition

Write code to a parttion a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x.

If x is contained within the list, the values of x only need to be
after the elements less than x. 

The partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.

EXAMPLE:
input: 3->5->8->5->10->2->1 (partition = 5)
output: 3->1->2->10->5->5->8
"""

from LinkedList import *

def partition(ll, x):
    current = ll.tail = ll.head

    print("current: ", current)
    print("tail: ", ll.tail)
    print("head: ", ll.head)

    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
            print("new head: ", ll.head)
        else:
            ll.tail.next = current
            ll.tail = current
            print("new tail: ", ll.tail)
        current = nextNode
        
    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None

    return ll

if __name__ == "__main__":
	ll = LinkedList()
	ll.generate(3, 0, 99)
	print(ll)
	print(partition(ll, ll.head.value))