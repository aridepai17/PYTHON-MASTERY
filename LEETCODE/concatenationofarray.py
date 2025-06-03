# LEETCODE 1929

'''
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i]
and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
'''

def getConcatenation(nums):
    return nums + nums

# Example usage:
nums = [1, 2, 1]
print(getConcatenation(nums))  # Output: [1, 2, 1, 1, 2, 1]

nums = [1, 3, 2, 1]
print(getConcatenation(nums))  # Output: [1, 3, 2, 1, 1, 3, 2, 1]

nums = [0, 0, 0]
print(getConcatenation(nums))  # Output: [0, 0, 0, 0, 0, 0]