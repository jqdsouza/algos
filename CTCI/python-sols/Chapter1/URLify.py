"""
1.3 URLify: Write a method to replace all spaces in a string with '%20'.

You may assume that the string has sufficient space at the end to hold the additional characters, and that you
are given the "true" length of the string.

EXAMPLE:
Input: "Mr John Smith      ", 13
Ouput: "Mr%20John%20Smith"
"""
import unittest

def urlify1(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    
    # do indexing based on length of string with spaces
    new_index = len(string)

    # loop over actual legnth
    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3

        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string


class Test(unittest.TestCase):
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify1(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()


