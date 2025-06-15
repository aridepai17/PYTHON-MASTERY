# LEETCODE 448

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(nums):
    present = set(nums)
    dissappeared = []
    
    for i in range(1, len(nums) + 1):
        if i not in present:
            dissappeared.append(i)
    return dissappeared

# Example usage
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums1))  # Output: [5, 6]

# Additional examples
nums2 = [1, 1, 2, 2]
print(findDisappearedNumbers(nums2))  # Output: [3, 4]

nums3 = [2, 2, 3, 3, 5, 5]
print(findDisappearedNumbers(nums3))  # Output: [1, 4, 6]

nums4 = [1, 2, 3, 4, 5]
print(findDisappearedNumbers(nums4))  # Output: []

nums5 = [5, 4, 3, 2, 1]
print(findDisappearedNumbers(nums5))  # Output: []

nums6 = [1, 2, 3, 5, 6, 7, 8]
print(findDisappearedNumbers(nums6))  # Output: [4]