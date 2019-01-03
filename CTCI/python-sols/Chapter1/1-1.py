"""
1.1 Is Unique:
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""
import unittest

def is_unique1(string):
	# assume character set is ASCII
	if len(string) > 128:
		return False

	str_list = []
	for el in string:
		if el in str_list:
			return False
		
		else:
			str_list.append(el)

	return True

def is_unique2(string):
	# assume character set is ASCII
	if len(string) > 128:
		return False

	str_list = [False for el in range(128)]
	
	for el in string:
		unicode_val = ord(el)

		if str_list[unicode_val] == True:
			return False 

		str_list[unicode_val] = True

	return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique1(test_string)
            self.assertTrue(actual)
            
        # false check
        for test_string in self.dataF:
            actual = is_unique1(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()