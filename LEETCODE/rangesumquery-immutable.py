# LEETCODE 303

'''
Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''

class NumArray:
    def __init__(self, nums):
        n = len(nums)
        self.prefix = [0] * n
        self.prefix[0] = [0]
        
        for i in range(1, n):
            self.prefix[i] = self.prefix[i - 1] + nums[i]
    
    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
    
# Example usage:
nums = [1, 2, 3, 4]
numArray = NumArray(nums)
print(numArray.sumRange(0, 1)) # Output: 3
print(numArray.sumRange(1, 2)) # Output: 7

# Example usage:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2)) # Output: 1
print(numArray.sumRange(2, 5)) # Output: 3

# Example usage:
nums = [0]
numArray = NumArray(nums)
print(numArray.sumRange(0, 0)) # Output: 0