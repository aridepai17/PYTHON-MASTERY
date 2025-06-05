# LEETCODE 3028

'''
An ant is on a boundary. It sometimes goes left and sometimes right.

You are given an array of non-zero integers nums. The ant starts reading nums from the first element of it to its end. At each step, it moves according to the value of the current element:
1. If nums[i] < 0, it moves left by -nums[i] units.
2. If nums[i] > 0, it moves right by nums[i] units.
Return the number of times the ant returns to the boundary.

Notes:
1. There is an infinite space on both sides of the boundary.
2.We check whether the ant is on the boundary only after it has moved |nums[i]| units. In other words, if the ant crosses the boundary during its movement, it does not count.
'''

def antOnBoundary(nums):
    position = 0
    count = 0
    
    for step in nums:
        position += step
        if position == 0:
            count += 1
    return count

# Example usage:
nums = [2, -2, 3, -3]
print(antOnBoundary(nums))  # Output: 2

# Another example:
nums = [-1, 1, -1, 1]
print(antOnBoundary(nums))  # Output: 2

# Yet another example:
nums = [1, -1, 3, -2, 2]
print(antOnBoundary(nums))  # Output: 1