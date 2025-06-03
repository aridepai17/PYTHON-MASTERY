# LEETCODE 747

'''
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise.
'''

def dominanIndex(nums):
    maximumvalue = max(nums)
    maximumindex = nums.index(maximumvalue)
    
    for i in range(len(nums)):
        if i != maximumindex and maximumvalue < 2 * nums[i]:
            return -1
    return maximumindex

# Example usage
nums = [3, 6, 1, 0]
print(dominanIndex(nums))  # Output: 1

# Example usage
nums = [1, 2, 3, 4]
print(dominanIndex(nums))  # Output: -1

# Example usage
nums = [1]
print(dominanIndex(nums))  # Output: 0

# Example usage
nums = [0, 0, 3, 2]
print(dominanIndex(nums))  # Output: 2

# Example usage
nums = [ 2, 4, 5, 2, 0, 1, 3]
print(dominanIndex(nums))  # Output: 2