"""
1.7 Rotate Matrix
Given an image represented by an NxN matrix, where each pixel is the 
image in 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
"""
import unittest

# def rotate_matrix1(matrix):
# 	rotated = zip(*matrix[::-1])

# 	return rotated

def rotate_matrix2(matrix):
	n = len(matrix)
	
	for layer in range(n//2):
		first = layer 
		last = n - layer - 1

		for i in range(first, last):
			# save top
			top = matrix[layer][i]

			# top = left
			matrix[layer][i] = matrix[-i-1][layer]

			# left = bottom
			matrix[-i-1][layer] = matrix[-layer-1][i-1]

			# bottom = right
			matrix[-layer-1][-i-1] = matrix[i][-layer-1]

			# right = top
			matrix[i][-layer-1] = top

class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix2(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
	unittest.main()