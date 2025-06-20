# LEETCODE 1304

# Give an integer n, return any array containing n unique integers such that they add up to 0.

def sumZero(n):
    half = n // 2
    result = [i for i in range(-half, half + 1)]
    if n % 2 == 0:
        result.remove(0)
    return result

# Example usage
n1 = 5
print(sumZero(n1))  # Output: [-3, -2, -1, 0, 1, 2, 3]

n2 = 4
print(sumZero(n2))  # Output: [-2, -1, 1, 2]

# Additional examples
n3 = 1
print(sumZero(n3))  # Output: [0]

n4 = 2
print(sumZero(n4))  # Output: [-1, 1]

n5 = 3
print(sumZero(n5))  # Output: [-1, 0, 1]

n6 = 6
print(sumZero(n6))  # Output: [-3, -2, -1, 1, 2, 3]

n7 = 7
print(sumZero(n7))  # Output: [-3, -2, -1, 0, 1, 2, 3]

n8 = 8
print(sumZero(n8))  # Output: [-4, -3, -2, -1, 1, 2, 3, 4]

n9 = 9
print(sumZero(n9))  # Output: [-4, -3, -2, -1, 0, 1, 2, 3, 4]

n10 = 10
print(sumZero(n10))  # Output: [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]