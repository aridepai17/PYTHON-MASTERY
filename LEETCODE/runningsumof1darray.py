# LEETCODE 1480

'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0] + nums[1] + ... + nums[i]).
Return the running sum of nums.
'''

def runningSum(nums):
    runningsum = []
    currentsum = 0
    
    for num in nums:
        currentsum += num
        runningsum.append(currentsum)
    return runningsum

# Example usage:
nums = [1,2,3,4]
print(runningSum(nums)) # Output: [1, 3, 6, 10]

# Example usage with an empty array
nums = []
print(runningSum(nums)) # Output: []

# Example usage with negative numbers
nums = [-1, 2, -3, 4]
print(runningSum(nums)) # Output: [-1, 1, -2, 2]

# Example usage with a single element
nums = [5]
print(runningSum(nums)) # Output: [5]