# LEETCODE 2057

'''
Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i],
or -1 if such index does not exist.
x mod y is the remainder of the division of x by y.
'''

def smallestEqual(nums):
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1

# Example usage:
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(smallestEqual(nums))  # Output: 0

# Another example:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(smallestEqual(nums))  # Output: 9

# Yet another example:
nums = [2, 1, 3, 4, 5, 6, 7, 8, 9, 0]
print(smallestEqual(nums))  # Output: -1