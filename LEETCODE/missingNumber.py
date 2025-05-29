# LEETCODE 268 MISSING NUMBER

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(n, nums):
    n = len(nums)
    total = n * (n + 1) // 2
    sumarray = sum(nums)
    missing = total - sumarray
    return missing

# Example usage:
nums = [3, 0, 1]
n = 3
result = missingNumber(n, nums)
print(result)  # Output: 2

# Another example usage:
nums2 = [0, 1, 3, 2, 4, 6, 5, 7, 8, 9, 12, 11]
n2 = 12
result2 = missingNumber(n2, nums2)
print(result2)  # Output: 10