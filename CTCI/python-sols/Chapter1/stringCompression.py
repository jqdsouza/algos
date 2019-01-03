"""
1-6: String Compression:
Implement a method to perform basic string compression using the counts
of repeated characters. 

EXAMPLE: the string aabcccccaaa would become a2b1c5a3

If the "compressed" string is not smaller than the original string, return the original string.
Assume the string has only uppercase and lowercaser letters (a-z)
"""
import unittest

def string_compression(string):
	d = {}	
	ans = ""

	for el in string:
		if el in d:
			d[el] += 1
		else:
			d[el] = 1

	for key, val in d.items():
		temp = "{0}".format(key) + "{0}".format(val)
		ans += temp

	if len(ans) > len(string):
		return string

	else:
		return ans


class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()