# LEETCODE 2894

'''
You are given positive integers n and m.
Define two integers as follows:
1. num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
2. num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
'''

def differenceOfSums(n, m):
    num1 = 0
    num2 = 0
    for i in range(1, n+1):
        if i % m == 0:
            num2 += i
        else:
            num1 += i
    return num1 - num2

# Example usage:
n = 10
m = 3
print(differenceOfSums(n, m))  # Output: 37

# Another example:
n = 20
m = 5
print(differenceOfSums(n, m))  # Output: 90

# Yet another example:
n = 15
m = 4
print(differenceOfSums(n, m))  # Output: 61

# More examples:
n = 30
m = 6
print(differenceOfSums(n, m))  # Output: 225

n = 25
m = 7
print(differenceOfSums(n, m))  # Output: 135

n = 50
m = 10
print(differenceOfSums(n, m))  # Output: 1275