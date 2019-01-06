"""
1.9 String Rotation

Assume you have a method isSubstring which checks if one word is
a substring of another. Given two strings, s1 and s2, write code
to check if s2 is a rotation of s1 using only one call to isSubstring.

EXAMPLE:
"waterbottle" is a rotation of "erbottlewat"
"""
import string
import unittest

def is_substring(string, substring):
	return string.find(substring) != -1

def string_rotation(s1, s2):
	if len(s1) != len(s2):
		return False

	s1 = s1.lower()
	s2 = s2.lower()

	d1 = dict.fromkeys(list(string.ascii_lowercase), 0)
	d2 = dict.fromkeys(list(string.ascii_lowercase), 0)

	for i in range(len(s1)):
		d1[s1[i]] += 1
		d2[s2[i]] += 1 

	return d1 == d2


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()