# LEETCODE 3427

'''
You are given an integer array nums of size n. For each index i where 0 <= i < n, define a subarray nums[start ... i] where start = max(0, i - nums[i]).
Return the total sum of all elements from the subarray defined for each index in the array.
'''

def subarraySum(nums):
    total = 0
    n = len(nums)
    
    for i in range(n):
        start = max(0, i - nums[i])
        total += sum(nums[start: i + 1])
        
    return total

# Example usage:
nums = [1, 2, 3, 4]
print(subarraySum(nums))  # Output: 20

# Another example:
nums = [2, 3, 1]
print(subarraySum(nums))  # Output: 11

# Yet another example:
nums = [0, 1, 2]
print(subarraySum(nums))  # Output: 4