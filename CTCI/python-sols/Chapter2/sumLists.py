"""
2.5 Sum Lists: 
You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in reverse order, such that
the 1'st digit is at the ehad of the list. Write a function that adds the 
two numbers and returns the sum as a linked list.

EXAMPLE
input: (7->1->6) + (5->9->2). That is 617 + 295
Output: (2->1->9). That is, 912

FOLLOW UP 
Suppose the digits are stored in forward order. Repeat the above problem.

EXAMPLE
input (6->1->7) + (2->9->5). That is, 617 + 295
output: (9->1->2). That is, 912
"""



from LinkedList import *

def sum_lists(ll1, ll2):
    curr1 = ll1.head
    curr2 = ll2.head
    carry = 0

    sum_ll = LinkedList()
    
    while(curr1 or curr2):
    	if not curr1:
    		i = 0

    	else:
    		i = curr1.value

    	if not curr2:
    		j = 0

    	else:
    		j = curr2.value

    	sum_val = i + j + carry

    	if sum_val >= 10:
    		carry = 1
    		remainder = sum_val % 10
    		sum_ll.add(remainder)
    	else:
    		carry = 0
    		sum_ll.add(sum_val)

    	if curr1:
	    	curr1 = curr1.next
    	if curr2:
    		curr2 = curr2.next

    return sum_ll

def sum_lists_followup(ll1, ll2):
	pass

if __name__ == "__main__":
	ll_a = LinkedList()
	ll_a.generate(4, 0, 9)
	ll_b = LinkedList()
	ll_b.generate(3, 0, 9)
	print(ll_a)
	print(ll_b)
	print(sum_lists(ll_a, ll_b))