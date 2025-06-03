# LEETCODE 136

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor

# Example usage:
nums = [2, 2, 1]
print(singleNumber(nums))  # Output: 1

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4

nums = [2, 2, 3, 3, 6, 8, 7, 4, 4, 6, 7]
print(singleNumber(nums))  # Output: 8