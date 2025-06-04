# LEETCODE 2176

'''
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where
0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
'''

def countPairs(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1
    return count 

# Example usage:
nums = [1, 2, 3, 1, 2, 3]
k = 2
print(countPairs(nums))  # Output: 3

# Another example:
nums = [1, 1, 1, 1]
k = 1
print(countPairs(nums))  # Output: 6 

# Yet another example:
nums = [1, 2, 3, 4, 5]
k = 3
print(countPairs(nums))  # Output: 0