# LEETCODE 1389

'''
Given two arrays of integers nums and index. Your task is to create target array under the following rules:
1. Initially target array is empty.
2. From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
3. Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid.
'''

def createTargetArray(nums, index):
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target

# Example usage
nums1 = [0, 1, 2, 3, 4]
index1 = [0, 1, 2, 2, 1]
print(createTargetArray(nums1, index1))  # Output: [0, 4, 1, 3, 2]

# Additional examples
nums2 = [1, 2, 3, 4, 0]
index2 = [0, 1, 2, 3, 0]
print(createTargetArray(nums2, index2))  # Output: [0, 1, 2, 3, 4]

nums3 = [1, 3, 2, 0]
index3 = [0, 1, 2, 1]
print(createTargetArray(nums3, index3))  # Output: [1, 0, 3, 2]

nums4 = [5, 6, 7]
index4 = [0, 0, 0]
print(createTargetArray(nums4, index4))  # Output: [7, 6, 5]

nums5 = [10, 20, 30]
index5 = [0, 0, 0]
print(createTargetArray(nums5, index5))  # Output: [30, 20, 10]

nums6 = [4, 3, 2, 1]
index6 = [0, 0, 0, 0]
print(createTargetArray(nums6, index6))  # Output: [1, 2, 3, 4]