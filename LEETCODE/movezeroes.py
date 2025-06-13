# LEETCODE 283

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''

def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
            
# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)  # Output: nums = [1, 3, 12, 0, 0]
print(nums)  # To see the result

# Additional examples
nums1 = [0, 0, 1]
moveZeroes(nums1)  # Output: nums1 = [1, 0, 0]
print(nums1)  # To see the result

nums2 = [1, 2, 3]
moveZeroes(nums2)  # Output: nums2 = [1, 2, 3]
print(nums2)  # To see the result

nums3 = [0, 0, 0, 0]
moveZeroes(nums3)  # Output: nums3 = [0, 0, 0, 0]
print(nums3)  # To see the result

nums4 = [1, 0, 2, 0, 3]
moveZeroes(nums4)  # Output: nums4 = [1, 2, 3, 0, 0]
print(nums4)  # To see the result