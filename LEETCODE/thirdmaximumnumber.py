# LEETCODE 414

# Given an integer array nums, return the third distinct maximum number in this array. 
# If the third maximum does not exist, return the maximum number.

def thirdMax(nums):
    distinctNums = set(nums)
    if len(distinctNums) < 3:
        return max(distinctNums)
    return sorted(distinctNums, reverse=True)[2]

# Example usage:
nums = [3, 2, 1]
print(thirdMax(nums))  # Output: 1

# Example usage:
nums = [1, 2]
print(thirdMax(nums))  # Output: 2

# Example usage:
nums = [2, 2, 3, 1]
print(thirdMax(nums))  # Output: 1

# Example usage:
nums = [5, 2, 4, 1, 3]
print(thirdMax(nums))  # Output: 3