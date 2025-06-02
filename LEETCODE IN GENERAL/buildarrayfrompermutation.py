# LEETCODE 1920

'''
Given a zero-based permutation nums ( 0-indexed ), 
build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero based permutation nums in an array of distinct integers from 0 to nums.length - 1 (inclusive).
'''

def buildArray(nums):
    ans = [ nums[nums[i]] for i in range(len(nums)) ]
    return ans

# Example usage:
nums = [0, 2, 1, 5, 3, 4]
print(buildArray(nums))  # Output: [0, 1, 2, 4, 3, 5]

# Another example usage:
nums = [5, 0, 1, 2, 3, 4]
print(buildArray(nums))  # Output: [4, 5, 0, 1, 2, 3]

# Yet another example usage:
nums = [1, 2, 3, 4, 0]
print(buildArray(nums))  # Output: [2, 3, 4, 0, 1]