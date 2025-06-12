# LEETCODE 3423

# Given a circular array nums, find the maximum absolute difference between adjacent elements.
# Note - In a circular array, the first and last elements are adjacent.

def maxAdjacentDistance(nums):
    n = len(nums)
    nums.append(nums[0])  # Append the first element to the end to handle circularity
    
    return max(abs(nums[i] - nums[i + 1]) for i in range(n))

# Example usage:
nums = [1, 2, 3, 4, 5]
print(maxAdjacentDistance(nums))  # Output: 4 (|1 - 5| = 4)

# Another example:
nums = [5, 3, 8, 6, 2]
print(maxAdjacentDistance(nums))  # Output: 6 (|2 - 8| = 6)

# Yet another example:
nums = [10, 20, 30, 40, 50]
print(maxAdjacentDistance(nums))  # Output: 40 (|10 - 50| = 40)

# Test with negative numbers:
nums = [-5, 3, -8, 6, -2]
print(maxAdjacentDistance(nums))  # Output: 14 (|-8 - 6| = 14)

# Test with single element (edge case):
nums = [7]
print(maxAdjacentDistance(nums))  # Output: 0 (|7 - 7| = 0)

# Test with two elements:
nums = [100, -100]
print(maxAdjacentDistance(nums))  # Output: 200 (|100 - (-100)| = 200)

# Test with repeated numbers:
nums = [5, 5, 5, 5, 5]
print(maxAdjacentDistance(nums))  # Output: 0 (|5 - 5| = 0)

# Test with large numbers:
nums = [1000, 2000, 3000, 4000, 5000]
print(maxAdjacentDistance(nums))  # Output: 4000 (|1000 - 5000| = 4000)