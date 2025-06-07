# LEETCODE 766

# Given an m x n matrix mat, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

def isToeplitzMatrix(matrix):
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] != matrix[i - 1][j -1]:
                return False
    return True

# Example usage:
matrix1 = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
print(isToeplitzMatrix(matrix1))  # Output: True

matrix2 = [[1, 2], [2, 2]]
print(isToeplitzMatrix(matrix2))  # Output: False

matrix3 = [[1, 2, 3], [4, 1, 2], [5, 4, 1]]
print(isToeplitzMatrix(matrix3))  # Output: True

matrix4 = [[1, 2, 3], [2, 1, 2], [3, 2, 1]]
print(isToeplitzMatrix(matrix4))  # Output: False

matrix5 = [[1]]
print(isToeplitzMatrix(matrix5))  # Output: True