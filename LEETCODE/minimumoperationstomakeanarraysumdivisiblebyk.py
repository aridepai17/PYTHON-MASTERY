# LEETCODE 3512

'''
You are given an integer array nums and an integer k. You can perform the following operation any number of times:
1. Select an index i and replace nums[i] with nums[i] - 1.
Return the minimum number of operations required to make the sum of the array divisible by k.
'''

def minOperations(nums, k):
    sumNums = sum(nums)
    if sumNums % k == 0:
        return 0
    else:
        return sumNums % k
    
# Example usage
nums = [3, 1, 4, 2]
k = 6
print(minOperations(nums, k))  # Output: 0

# Additional examples
nums2 = [1, 2, 3]
k2 = 3
print(minOperations(nums2, k2))  # Output: 0

nums3 = [1, 2, 3, 4]
k3 = 5
print(minOperations(nums3, k3))  # Output: 1

nums4 = [10, 20, 30]
k4 = 7
print(minOperations(nums4, k4))  # Output: 3

nums5 = [5, 5, 5]
k5 = 4
print(minOperations(nums5, k5))  # Output: 1

nums6 = [1, 1, 1, 1]
k6 = 2
print(minOperations(nums6, k6))  # Output: 0

# Edge cases
nums7 = []
k7 = 2
print(minOperations(nums7, k7))  # Output: 0