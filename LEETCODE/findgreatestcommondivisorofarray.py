# LEETCODE 1979

'''
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
'''

def findGCD(nums):
  largest = max(nums)
  smallest = min(nums)
  
  while largest != 0:
    smallest, largest = largest, smallest % largest
  return smallest

# Alternate solution using math.gcd()

import math
def findGCDAlternate(nums):
    largest = max(nums)
    smallest = min(nums)
    return math.gcd(smallest, largest)

# Example usage
nums1 = [2, 5, 6, 9, 10]
print(findGCD(nums1))  # Output: 2

# Additional examples
nums2 = [4, 8, 12, 16]
print(findGCD(nums2))  # Output: 4

nums3 = [3, 6, 9, 12]
print(findGCD(nums3))  # Output: 3

nums4 = [5, 10, 15, 20]
print(findGCD(nums4))  # Output: 5

nums5 = [7, 14, 21, 28]
print(findGCD(nums5))  # Output: 7

nums6 = [1, 2, 3, 4, 5]
print(findGCD(nums6))  # Output: 1

nums7 = [10, 20, 30, 40]
print(findGCD(nums7))  # Output: 10

nums8 = [11, 22, 33, 44]
print(findGCD(nums8))  # Output: 11

nums9 = [100, 200, 300]
print(findGCD(nums9))  # Output: 100

nums10 = [9, 27, 81]
print(findGCD(nums10))  # Output: 9
