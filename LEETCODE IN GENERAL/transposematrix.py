# LEETCODE 867

'''
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the row and column indices of the matrix.
'''

def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    transpose = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(matrix[j][i])
        transpose.append(temp)
    return transpose

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose(matrix)
print(result)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Another example usage:
matrix2 = [[1, 2], [3, 4], [5, 6]]
result2 = transpose(matrix2)
print(result2)  # Output: [[1, 3, 5], [2, 4, 6]]

# Yet another example usage:
matrix3 = [[23, 45, 67], [89, 12, 34]]
result3 = transpose(matrix3)
print(result3)  # Output: [[23, 89], [45, 12], [67, 34]]