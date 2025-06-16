# LEETCODE 2016

'''
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
Return the maximum difference. If no such i and j exists, return -1.
'''

def maximumDifference(nums):
    minValue = nums[0]
    maxiDiff = -1
    
    for num in nums:
        if num > minValue:
            maxiDiff = max(maxiDiff, num - minValue)
        else:
            minValue = num
    return maxiDiff

# Example usage
nums1 = [7, 1, 5, 4]
print(maximumDifference(nums1))  # Output: 4

# Additional examples
nums2 = [9, 4, 3, 2]
print(maximumDifference(nums2))  # Output: -1 (No valid i and j exist)

nums3 = [1, 2, 3, 4, 5]
print(maximumDifference(nums3))  # Output: 4 (Max difference is 5 - 1)

nums4 = [5, 3, 6, 2, 8]
print(maximumDifference(nums4))  # Output: 6 (Max difference is 8 - 2)

nums5 = [1, 1, 1, 1]
print(maximumDifference(nums5))  # Output: -1 (No valid i and j exist)

nums6 = [3, 2, 5, 1, 7]
print(maximumDifference(nums6))  # Output: 6 (Max difference is 7 - 1)

nums7 = [10, 20, 30, 40, 50]
print(maximumDifference(nums7))  # Output: 40 (Max difference is 50 - 10)