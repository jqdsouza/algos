"""
1.5 One Away
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits)
away.

EXAMPLE
pale,  ple  -> true
pales, pale -> true
pale,  bale -> true
pale,  bake -> false
"""
import unittest

def is_one_away(string1, string2):
	"""
	Notice that any strings that output true have the property
	that there is at most only 1 char value that is different between the two.
	Solution constructed based on this observation.
	"""
	d = {}

	if len(string1) >= len(string2):
		for el in string1:
			if el in d:
				d[el] += 1
			else:
				d[el] = 1

		for el in string2:
			if el in string1:
				if el in d:
					d[el] -= 1
				else:
					d[el] = 1
	else:
		for el in string2:
			if el in d:
				d[el] += 1
			else:
				d[el] = 1

		for el in string1:
			if el in string2:
				if el in d:
					d[el] -= 1
				else:
					d[el] = 1

	tot = sum(list(d.values()))
	print("string 1: {0}, string 2: {1}".format(string1, string2))

	if tot == 1 or tot == 0:
		return True 
	else:
		return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = is_one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()