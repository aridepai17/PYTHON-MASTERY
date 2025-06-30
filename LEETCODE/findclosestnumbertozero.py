# LEETCODE 2239

'''
Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
If there are multiple answers, return the number with the largest value.
'''

def findClosestNumber(nums):
  closest = nums[0]
  for num in nums:
    if abs(num) < abs(closest):
      closest = num
    elif abs(num) == abs(closest) and num > closest:
      closest = num
  return closest

# Example usage:
nums = [-4, -2, 1, 4, 8]
print(findClosestNumber(nums))  # Output: 1

# New examples
nums2 = [3, -1, 2, -3]
print(findClosestNumber(nums2))  # Output: -1

nums3 = [0, -1, 1]
print(findClosestNumber(nums3))  # Output: 1

nums4 = [5, 5, -5, -5]
print(findClosestNumber(nums4))  # Output: 5

nums5 = [-10, -20, 10, 20]
print(findClosestNumber(nums5))  # Output: 10

nums6 = [7, -7, 0]
print(findClosestNumber(nums6))  # Output: 0

nums7 = [1, 2, 3, 4]
print(findClosestNumber(nums7))  # Output: 1

nums8 = [-1, -2, -3, -4]
print(findClosestNumber(nums8))  # Output: -1

nums9 = [100, -100, 50, -50]
print(findClosestNumber(nums9))  # Output: 50

nums10 = [0]
print(findClosestNumber(nums10))  # Output: 0