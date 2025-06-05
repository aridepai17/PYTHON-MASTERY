# LEETOCODE 2848

'''
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.
Return the number of integer points on the line that are covered with any part of a car.
'''

def numberofPoints(nums):
    covered = set()
    
    for start, end in nums:
        for point in range(start, end + 1):
            covered.add(point)
            
    return len(covered)

# Example usage:
nums = [[1, 3], [2, 5], [6, 8]]
print(numberofPoints(nums))  # Output: 8

# Another example:
nums = [[0, 2], [3, 5], [1, 4]]
print(numberofPoints(nums))  # Output: 6

# Yet another example:
nums = [[1, 1], [2, 2], [3, 3]]
print(numberofPoints(nums))  # Output: 3