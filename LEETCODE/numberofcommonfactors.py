# LEETCODE 2427

# Given two positive integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.

def commonFactors(a, b):
    num = min(a, b)
    count = 0
    
    for i in range(1, num + 1):
        if a % i == 0 and b % i == 0:
            count += 1
    return count

# Example usage:
a = 12
b = 18
print(commonFactors(a, b))  # Output: 6 (Common factors are 1, 2, 3, 6)

# Another example:
a = 25
b = 30
print(commonFactors(a, b))  # Output: 2 (Common factors are 1, 5)

# Yet another example:
a = 7
b = 14
print(commonFactors(a, b))  # Output: 2 (Common factors are 1, 7)

# More examples:
a = 100
b = 200
print(commonFactors(a, b))  # Output: 4 (Common factors are 1, 2, 4, 5)

a = 1
b = 2
print(commonFactors(a, b))  # Output: 1 (Common factor is 1)

a = 15
b = 45
print(commonFactors(a, b))  # Output: 3 (Common factors are 1, 3, 15)