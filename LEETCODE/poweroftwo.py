# LEETCODE 231

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

def isPowerOfTwo(n):
    if n <= 0:
        return False
    else:
        if 2 ** 31 % n == 0:
            return True
        else:
            return False
        
# Example usage:
n = 16
print(isPowerOfTwo(n))  # Output: True

# Another example usage:
n = 18
print(isPowerOfTwo(n))  # Output: False

n = 512
print(isPowerOfTwo(n))  # Output: True