# LEETCODE 35

'''
Given a sorted array of idstinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = ( left + right ) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Example usage:
nums = [1, 3, 6, 8, 9]
target = 5
print(searchInsert(nums, target))  # Output: 3

# Another example usage:
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # Output: 2

# Yet another example usage:
nums = [3, 5, 6, 8, 9, 11, 14]
target = 10
print(searchInsert(nums, target))  # Output: 5