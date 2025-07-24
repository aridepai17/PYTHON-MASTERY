# LEETCODE 26

'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.
'''

def removeDuplicates(nums):
  if not nums:
    return 0
  
  left = 0
  for right in range(1, len(nums)):
    if nums[right] != nums[left]:
      left += 1
      nums[left] = nums[right]
      
  return left + 1


# Example usage 
nums1 = [1, 1, 2]
print(removeDuplicates(nums1)) # Output: 2

nums2 = [0, 0, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums2)) # Output: 5

nums3 = [1, 2, 2, 3, 4, 4, 5]
print(removeDuplicates(nums3)) # Output: 5

nums4 = [1, 1, 1, 1, 1]
print(removeDuplicates(nums4)) # Output: 1

nums5 = [2, 2, 2, 3, 4, 5, 5]
print(removeDuplicates(nums5)) # Output: 5

nums6 = [5, 5, 5, 5, 5, 5]
print(removeDuplicates(nums6)) # Output: 1

nums7 = []
print(removeDuplicates(nums7)) # Output: 0

nums8 = [1]
print(removeDuplicates(nums8)) # Output: 1

nums9 = [1, 2, 3, 4, 5]
print(removeDuplicates(nums9)) # Output: 5

nums10 = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8] 
print(removeDuplicates(nums10)) # Output: 6