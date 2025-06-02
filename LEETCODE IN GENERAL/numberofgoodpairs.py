# LEETCODE 1512

# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def numIdenticalPairs(nums):
    count = {}
    goodpairs = 0
    
    for num in nums:
        if num in count:
            goodpairs += count[num]
            count[num] += 1
        else:
            count[num] = 1
    return goodpairs

# Example usage:
nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))  # Output: 4 (good pairs are (0, 3), (0, 4), (3, 4), (2, 5))

# Another example usage:
nums = [1, 1, 1, 1]
print(numIdenticalPairs(nums))  # Output: 6 (good pairs are (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

# Yet another example usage:
nums = [1, 2, 3]
print(numIdenticalPairs(nums))  # Output: 0 (no good pairs)