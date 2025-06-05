# LEETCODE 3432

'''
You are given an integer array nums of length n.
A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:
Left subarray contains indices [0, i].
Right subarray contains indices [i + 1, n - 1].
Return the number of partitions where the difference between the sum of the left and right subarrays is even.
'''

def countPartitions(nums):
    total = sum(nums)
    n = len(nums)
    count = 0
    
    for i in range(n - 1):
        leftsum += nums[i]
        rightsum = total - leftsum
        if abs(leftsum - rightsum) % 2 == 0:
            count += 1
    return count 

# Example usage:
nums = [1, 2, 3, 4]
print(countPartitions(nums))  # Output: 3

# Another example:
nums = [1, 2, 3]
print(countPartitions(nums))  # Output: 0

# Yet another example:
nums = [1, 2, 3, 4, 5]
print(countPartitions(nums))  # Output: 4

# Yet another example:
nums = [2, 4, 6, 8]
print(countPartitions(nums))  # Output: 3


