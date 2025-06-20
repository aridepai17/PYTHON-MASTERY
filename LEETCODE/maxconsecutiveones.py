# LEETCODE 485

# Given a binary array, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(nums):
    maxCount = 0
    currentCount = 0
    
    for num in nums:
        if num == 1:
            currentCount += 1
            maxCount = max(maxCount, currentCount)
        else:
            currentCount = 0
    
    return maxCount

# Example usage
nums1 = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums1))  # Output: 3

# Additional examples
nums2 = [1, 0, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums2))  # Output: 2

nums3 = [0, 0, 0, 0]
print(findMaxConsecutiveOnes(nums3))  # Output: 0

nums4 = [1, 1, 1, 1, 1]
print(findMaxConsecutiveOnes(nums4))  # Output: 5

nums5 = [0, 1, 1, 1, 0, 1, 1]
print(findMaxConsecutiveOnes(nums5))  # Output: 3

nums6 = [1, 0, 0, 1, 1, 1, 1, 0]
print(findMaxConsecutiveOnes(nums6))  # Output: 4

nums7 = [1, 1, 0, 0, 1, 1, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums7))  # Output: 4

nums8 = [0, 1, 0, 1, 0, 1, 0]
print(findMaxConsecutiveOnes(nums8))  # Output: 1

nums9 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums9))  # Output: 3

nums10 = [1, 0, 1, 0, 1, 0, 1, 0, 1]
print(findMaxConsecutiveOnes(nums10))  # Output: 1