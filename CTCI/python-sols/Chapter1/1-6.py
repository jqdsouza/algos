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
	count = 0
	ans = []
	for i in range(len(string)):
		if i != 0 and string[i] != string[i-1]:
			ans.append(string[i-1] + str(count))
			count = 0
		count+=1
		
	ans.append(string[-1] + str(count))

	return min(string, ''.join(ans), key = len)

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