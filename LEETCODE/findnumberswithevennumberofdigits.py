# LEETCODE 1295

# Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
    count = 0
    
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count

# Example usage
nums = [12, 345, 2, 6, 7896]
print(findNumbers(nums))  # Output: 2

# Example usage
nums = [555, 901, 482, 1771]
print(findNumbers(nums))  # Output: 1

# Example usage
nums = [1, 23, 4567, 89012]
print(findNumbers(nums))  # Output: 0

# Example usage
nums = [100, 2000, 30000, 400000]
print(findNumbers(nums))  # Output: 2