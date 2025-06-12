# LEETCODE 2413

# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

def smallestEvenMultiple(n):
    if n % 2 == 0:
        return n
    else:
        return n * 2
    
# Example usage:
n = 5
print(smallestEvenMultiple(n))  # Output: 10

# Another example:
n = 6
print(smallestEvenMultiple(n))  # Output: 6

# Yet another example: 
n = 1
print(smallestEvenMultiple(n))  # Output: 2

# More examples:
n = 3
print(smallestEvenMultiple(n))  # Output: 6

n = 7
print(smallestEvenMultiple(n))  # Output: 14

n = 4
print(smallestEvenMultiple(n))  # Output: 4

n = 9
print(smallestEvenMultiple(n))  # Output: 18

n = 10
print(smallestEvenMultiple(n))  # Output: 10