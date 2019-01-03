"""
1.2 Check Permutation:
Given two strings, write a method to decide if one is a permutation of the other
"""

import unittest
from collections import Counter

def check_permutation1(string1, string2):
	# string lengths must be same
	if len(string1) != len(string2):
		return False

	str_dict = {}

	for el in set(list(string1)):
		str_dict[el] = string1.count(el)

	for el in set(list(string2)):
		charCount = string2.count(el)

		if (el not in str_dict.keys()) or (charCount != str_dict[el]):
			return False

	return True

def check_permutation2(string1, string2):
	# string lengths must be same
	if len(string1) != len(string2):
		return False

	counter = Counter()

	for el in string1:
		counter[el]+=1

	for el in string2:
		if counter[el] == 0:
			return False

		counter[el] -= 1


	return True

class Test(unittest.TestCase):
	dataT = (
	    ('abcd', 'bacd'),
	    ('3563476', '7334566'),
	    ('wef34f', 'wffe34'),
	)
	dataF = (
		('123', '456'),
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

	def test_cp(self):
	    # true check
	    for test_strings in self.dataT:
	        result = check_permutation1(*test_strings)
	        self.assertTrue(result)

	    # false check
	    for test_strings in self.dataF:
	        result = check_permutation1(*test_strings)
	        self.assertFalse(result)

if __name__ == "__main__":
	unittest.main()
