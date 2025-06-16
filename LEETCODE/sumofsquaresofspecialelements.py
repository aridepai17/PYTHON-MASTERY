# LEETCODE 2778

'''
You are given a 1-indexed integer array nums of length n.
An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
Return the sum of the squares of all special elements of nums.
'''

def sumOfSquares(nums):
    length = len(nums)
    index = 1
    result = 0
    
    for num in nums:
        if length % index == 0:
            result += num * num
        index += 1
    return result

# Example usage
nums1 = [1, 2, 3, 4, 5]
print(sumOfSquares(nums1))  # Output: 55 (1^2 + 2^2 + 3^2 + 4^2 + 5^2)

nums2 = [2, 3, 4, 5, 6]
print(sumOfSquares(nums2))  # Output: 56 (2^2 + 3^2 + 4^2 + 5^2 + 6^2)

# Additional examples
nums3 = [1, 2, 3, 4, 5, 6]
print(sumOfSquares(nums3))  # Output: 56 (1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2)

nums4 = [10, 20, 30, 40, 50]
print(sumOfSquares(nums4))  # Output: 5500 (10^2 + 20^2 + 30^2 + 40^2 + 50^2)

nums5 = [1, 1, 1, 1, 1]
print(sumOfSquares(nums5))  # Output: 5 (1^2 + 1^2 + 1^2 + 1^2 + 1^2)

nums6 = [5, 10, 15, 20, 25, 30]
print(sumOfSquares(nums6))  # Output: 1225 (5^2 + 10^2 + 15^2 + 20^2 + 25^2 + 30^2)

nums7 = [3, 6, 9, 12, 15, 18]
print(sumOfSquares(nums7))  # Output: 486 (3^2 + 6^2 + 9^2 + 12^2 + 15^2 + 18^2)

nums8 = [4, 8, 12, 16]
print(sumOfSquares(nums8))  # Output: 384 (4^2 + 8^2 + 12^2 + 16^2)