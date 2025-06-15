# LEETCODE 1572

'''
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
'''

def diagonalSum(mat):
    n = len(mat)
    primarySum = 0
    secondarySum = 0
    
    for i in range(n):
        primarySum += mat[i][i]
        secondarySum += mat[i][n - 1 - i]
    
    total = primarySum + secondarySum
    
    if n % 2 == 1:
        total -= mat[n // 2][n // 2]
    return total

# Example usage
mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonalSum(mat1))  # Output: 25

# Additional examples
mat2 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
print(diagonalSum(mat2))  # Output: 8 (4 from primary + 4 from secondary)

mat3 = [[5]]
print(diagonalSum(mat3))  # Output: 5 (Only one element)

mat4 = [[1, 2], [3, 4]]
print(diagonalSum(mat4))  # Output: 10 (1 + 4 + 2 + 3)

mat5 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(diagonalSum(mat5))  # Output: 68 (1 + 6 + 11 + 16 + 4 + 7 + 10 + 13)

mat6 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(diagonalSum(mat6))  # Output: 3 (1 + 1 + 1)