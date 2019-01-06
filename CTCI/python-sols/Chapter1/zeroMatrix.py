"""
1.8 Zero Matrix

Write an algo such that if an element in an MXN matrix is 0,
its entire row and column are set to 0
"""
import unittest

def zero_matrix(matrix):
	m = len(matrix)
	n = len(matrix[0])

	rows = []
	cols = []

	for x in range(m):
		for y in range(n):
			if matrix[x][y] == 0:
				rows.append(x)
				cols.append(y)

	for row in rows:
		for i in range(len(matrix[0])):
			matrix[row][i] = 0

	for col in cols:
		for i in range(len(matrix)):
			matrix[i][col] = 0

	return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()