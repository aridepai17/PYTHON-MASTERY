# LEETCODE 326

# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^x.

def isPowerOfThree(n):
    if n <= 0:
        return False
    else:
        if 3 ** 19 % n == 0:
            return True
        else:
            return False
        
# Example usage:
n = 27
print(isPowerOfThree(n))  # Output: True

# Another example usage:
n = 282649
print(isPowerOfThree(n))  # Output: False

# Yet another example usage:
n = 84638
print(isPowerOfThree(n))  # Output: False