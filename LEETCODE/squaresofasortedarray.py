# LEETCODE 977

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    squares = []
    
    while left <= right:
        if abs(nums[left]) <= abs(nums[right]):
            squares.append(nums[right] * nums[right])
            right -= 1
        else:
            squares.append(nums[left] * nums[left])
            left += 1
            
    return squares[::-1]

# Example usage
nums1 = [-4, -1, 0, 3, 10]
print(sortedSquares(nums1))  # Output: [0, 1, 9, 16, 100]

nums2 = [-7, -3, 2, 3, 11]
print(sortedSquares(nums2))  # Output: [4, 9, 9, 49, 121]

nums3 = [-5, -2, 0, 1, 2]
print(sortedSquares(nums3))  # Output: [0, 1, 4, 25, 16]

nums4 = [-1, 1, 2, 2, 3]
print(sortedSquares(nums4))  # Output: [1, 1, 4, 4, 9]

nums5 = [0, 0, 0, 0]
print(sortedSquares(nums5))  # Output: [0, 0, 0, 0]