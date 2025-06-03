# LEETCODE 169

'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than n / 2 times. 
You may assume that the majority element always exists in the array.
'''

# Boyer-Moore Voting Algorithm Optimal approach

def majorityElement(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
        
    return candidate

# Example usage:
nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))  # Output: 2

nums = [1, 1, 2, 2, 2, 3, 3]
print(majorityElement(nums))  # Output: 2

nums = [5, 5, 5, 1, 2, 3]
print(majorityElement(nums))  # Output: 5