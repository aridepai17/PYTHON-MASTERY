# LEETCODE 2520

# Given an integer num, return the number of digits in num that divide num evenly.
# An integer val divides num if num % val == 0.

def countDigits(num):
    count = 0
    for digit in str(num):
        if num % int(digit) == 0:
            count += 1
    return count

# Example usage:
num = 7
print(countDigits(num))  # Output: 1

# Example usage:
num = 121
print(countDigits(num))  # Output: 2

# Example usage:
num = 1248
print(countDigits(num))  # Output: 4

# Example usage:
num = 1012
print(countDigits(num))  # Output: 3

# Example usage:
num = 1111
print(countDigits(num))  # Output: 4

# Example usage:
num = 10000
print(countDigits(num))  # Output: 1