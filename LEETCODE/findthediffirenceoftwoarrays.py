# LEETCODE 2215

'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
- answer[0] is a list of distinct integers present in nums1 but not in nums2.
- answer[1] is a list of distinct integers present in nums2 but not in nums1.

Note that the integers in the lists may be returned in any order.
'''

def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    onlyinset1 = list(set1 - set2)
    onlyinset2 = list(set2 - set1)
    
    return onlyinset1, onlyinset2

# Example usage:
nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 5, 6]
print(findDifference(nums1, nums2))  # Output: ([1, 2], [5, 6])

# Another example:
nums1 = [7, 8, 9]
nums2 = [9, 10, 11]
print(findDifference(nums1, nums2))  # Output: ([7, 8], [10, 11])

# Yet another example:
nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print(findDifference(nums1, nums2))  # Output: ([], [])

# Yet another example:
nums1 = [5, 6, 7]
nums2 = [6, 7, 8]
print(findDifference(nums1, nums2))  # Output: ([5], [8])