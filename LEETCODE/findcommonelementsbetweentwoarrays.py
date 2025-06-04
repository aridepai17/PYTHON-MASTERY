# LEETCODE 2956

'''
You are given two integer arrays nums1 and nums2 of sizes n and m respectively.
Calculate the following values:
answer1: the number of indices i such that nums1[i] exists in nums2.
answer2: the number of indices i such that nums2[i] exists in nums1.
Return the values as a list [answer1, answer2].
'''

def findIntersectionValues(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    answer1 = sum(1 for num in nums1 if num in set2)
    answer2 = sum(1 for num in nums2 if num in set1)
    
    return [answer1, answer2]

# Example usage:
nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 5, 6]
print(findIntersectionValues(nums1, nums2))  # Output: [2, 2]

# Another example:
nums1 = [7, 8, 9]
nums2 = [9, 10, 11]
print(findIntersectionValues(nums1, nums2))  # Output: [1, 1]

# Yet another example:
nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print(findIntersectionValues(nums1, nums2))  # Output: [3, 3]

# Yet another example:
nums1 = [5, 6, 7]
nums2 = [6, 8] 
print(findIntersectionValues(nums1, nums2))  # Output: [1, 1]