# LEETCODE 1

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(i, j)
            
            
# Example usage:
nums = [1,2,3,4,5,6,7,8,9]
target = 9
result = twoSum(nums, target) # Output: (0 7), (1 6), (2 5), (3 4)

# Another example usage:
nums2 = [3, 2, 4, 6, 5, 1]
target2 = 9
result2 = twoSum(nums2, target2) # Output: (0 3), (2 4)

        