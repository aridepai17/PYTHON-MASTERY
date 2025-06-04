# LEETCODE 3190

# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
# Return the minimum number of operations to make all elements of nums divisible by 3.

def minimumOperations(nums):
    count = 0
    for num in nums:
        if num % 3 != 0:
            count += 1
    return count 

# Example usage:
nums = [1, 2, 3, 4, 5]
print(minimumOperations(nums))  # Output: 4

# Another example:
nums = [3, 6, 9]
print(minimumOperations(nums))  # Output: 0

# Yet another example:
nums = [10, 11, 12]
print(minimumOperations(nums))  # Output: 2