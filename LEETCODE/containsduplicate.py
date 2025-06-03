# LEETCODE 217

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# Example usage:
nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # Output: True

# Another example usage:
nums = [1, 2, 3, 4]
print(containsDuplicate(nums))  # Output: False

# Yet another example usage:
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums))  # Output: True