# LEETCODE 1913 

'''
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
For example, the product difference between pairs (5, 6) and (2, 3) is (5 * 6) - (2 * 3) = 30 - 6 = 24.

Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference 
between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
Return the maximum such product difference.
'''

def maxProductDifference(nums):
    nums.sort()
    return (nums[-1] * nums[-2] - nums[0] * nums[1])

# Example usage:
nums = [5, 6, 2, 7, 4]
print(maxProductDifference(nums))  # Output: 34

# Another example:
nums = [4, 2, 5, 9, 7, 4, 8]
print(maxProductDifference(nums))  # Output: 64

# Yet another example:
nums = [1, 5, 2, 3]
print(maxProductDifference(nums))  # Output: 20