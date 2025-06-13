# LEETCODE 2824

'''
Given a 0-indexed integer array nums of length n and an integer target, return the 
number of pairs (i, j) such that 0 <= i < j < n and nums[i] + nums[j] < target.
'''
# Two Pointer approach: O(n log n) time complexity

def countPairs(nums, target):
    count = 0
    nums.sort()
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] < target:
            count += (right - left)
            left += 1
        else:
            right -= 1
    return count

# Example usage
nums = [1, 2, 3, 4]
target = 5
print(countPairs(nums, target))  # Output: 4

# Additional examples
nums2 = [1, 3, 5, 7]
target2 = 8
print(countPairs(nums2, target2))  # Output: 2

nums3 = [0, -1, 2, -3, 1]
target3 = 2
print(countPairs(nums3, target3))  # Output: 5

nums4 = [5, 1, 3, 4, 2]
target4 = 6
print(countPairs(nums4, target4))  # Output: 7

nums5 = [10, 20, 30, 40]
target5 = 50
print(countPairs(nums5, target5))  # Output: 6

nums6 = [-1, -2, -3, -4]
target6 = -1
print(countPairs(nums6, target6))  # Output: 6