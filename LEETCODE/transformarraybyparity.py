# LEETCODE 3467

'''
You are given an integer array nums.
Transform nums by performing the following operations in the exact order specified:
1. Replace each even number with 0.
2. Replace each odd number with 1..
3. Sort the modified array in the non-decreasing order.
Return the resulting array after performing the above operations.
'''

def transformArray(nums):
    even, odd = 0, 0
    answer = []
    
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    
    answer = ([0] * even) + ([1] * odd)
    return answer

# Time Complexity: O(n)
# Space Complexity: O(n)

# Another approach:

def transformArray(nums):
    return sorted([0 if num % 2 == 0 else 1 for num in nums])

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Example usage:
nums = [3,1,2,4]
print(transformArray(nums)) # Output: [0, 0, 1, 1]

# Another usage:
nums = [8, 3, 2, 1, 6, 4, 7, 5]
print(transformArray(nums)) # Output: [0, 0, 0, 0, 1, 1, 1, 1]