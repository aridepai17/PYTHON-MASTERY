# LEETCODE 2032

'''
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all
the values that are present in at least two out of the three arrays. 
You may return the values in any order.
'''

def twoOutOfThree(nums1, nums2, nums3):
    set1 = set(nums1)
    set2 = set(nums2)
    set3 = set(nums3)
    
    result = ( set1 & set2 ) | ( set2 & set3 ) | ( set1 & set3)
    return list(result)

# Example usage:
nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]
print(twoOutOfThree(nums1, nums2, nums3))  # Output: [2, 3]

# Another example:
nums1 = [3, 1]
nums2 = [2, 3]
nums3 = [1, 2]
print(twoOutOfThree(nums1, nums2, nums3))  # Output: [1, 2, 3]

# Yet another example:
nums1 = [1, 2, 2]
nums2 = [4, 3, 3]
nums3 = [5]
print(twoOutOfThree(nums1, nums2, nums3))  # Output: []