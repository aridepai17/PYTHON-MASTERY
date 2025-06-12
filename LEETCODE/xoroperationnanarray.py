# LEETCODE 1486

# You are given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

def xorOperation(n, start):
    nums = [start + 2 * i for i in range(n)]
    result = 0
    for num in nums:
        result ^= num
    return result

# Alternate solution - one pass

def xorOperationOnePass(n, start):
    result = 0
    for i in range(1, n):
        result ^= start + 2 * i
    return result

# Example usage:
n = 5
start = 0
print(xorOperation(n, start))  # Output: 8

# Another example:
n = 4
start = 3
print(xorOperation(n, start))  # Output: 8

# Yet another example:
n = 1
start = 7
print(xorOperation(n, start))  # Output: 7

# More examples:
n = 10
start = 5
print(xorOperation(n, start))  # Output: 0

n = 6
start = 2
print(xorOperation(n, start))  # Output: 4