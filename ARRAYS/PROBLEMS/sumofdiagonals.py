# Given a 2D list, calculate the sum of diagonal elements.

def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][j]
    return sum

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = diagonal_sum(matrix)
print(result) # Output: 15  (1 + 5 + 9)

# Another example usage:
matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
result2 = diagonal_sum(matrix2)
print(result2) # Output: 34 (1 + 6 + 11 + 16)