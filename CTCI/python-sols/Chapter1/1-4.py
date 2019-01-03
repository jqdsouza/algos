"""
1.4 Palindrome Permutation: Given a string, write a function to check
if it's a permutation of a palindrome. The palindrome does not need to
be limited to just dictionary words.
"""
import unittest
from collections import Counter

# Time complexity = Space Complexity = O(n)

def palindrome_permutation(string):
	# preprocess string
	string = string.replace(" ", "")
	string = string.lower()

	# can use property of symmetry to determine if string is palindrome
	d = {}

	for el in string:
		if el in d:
			d[el]+=1
		else:
			d[el] = 1

	odd_count = 0
	for keys, values in d.items():
		if values % 2 != 0 and odd_count == 0:
			odd_count += 1
		elif values % 2 != 0 and odd_count != 0:
			return False

	return True

class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = palindrome_permutation(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()