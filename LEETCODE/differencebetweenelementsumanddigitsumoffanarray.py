# LEETCODE 2535

'''
You are given a positive integer array nums.
The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.
Note that the absolute difference between two integers x and y is defined as |x - y|.
'''

def diffrenceOfSum(nums):
    sumnums = sum(nums)
    sumdigits = 0
    
    for num in nums:
        while num > 0:
            sumdigits += num % 10
            num //= 10
    return abs(sumnums - sumdigits)

# Example usage:
nums = [1,15,6,3]
print(diffrenceOfSum(nums)) # Output: 9

# Another example:
nums = [1,2,3,4]
print(diffrenceOfSum(nums)) # Output: 0

# Yet another example:
nums = [23, 3, 24, 67, 12, 14, 13]
print(diffrenceOfSum(nums)) # Output: 117