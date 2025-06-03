# LEETCODE 349

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
'''

def intersection1(nums1, nums2):
    return list(set(nums1) & set(nums2))

# Time Complexity: O(n)
# Space Complexity: O(n)

def intersection2(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    set1 = set(nums1)
    result = set()
    
    for num in nums2:
        if num in set1:
            result.add(num)
            
    return list(result)

# Time Complexity: O(n)
# Space Complexity: O(n)

# Example usage:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection1(nums1, nums2))  # Output: [2]

# Another example usage:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection1(nums1, nums2))  # Output: [9, 4]

# Yet another example usage:
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
print(intersection1(nums1, nums2))  # Output: []












