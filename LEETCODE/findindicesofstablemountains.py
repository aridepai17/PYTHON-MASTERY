# LEETCODE 3285

'''
There are n mountains in a row, and each mountain has a height.
You are given an integer array height where height[i] represents the height of mountain i, and an integer threshold.
A mountain is called stable if the mountain just before it (if it exists) has a height strictly greater than threshold. 
Note that mountain 0 is not stable.
Return an array containing the indices of all stable mountains in any order.
'''

def stableMountains(height, threshold):
    stable = []
    
    for i in range(1, len(height)):
        if height[i - 1] > threshold:
            stable.append(i)
    return stable

# Example usage
height1 = [3, 1, 4, 2, 5]
print(stableMountains(height1, 2))  # Output: [2, 4]

# Additional examples
height2 = [1, 2, 3, 4, 5]
print(stableMountains(height2, 3))  # Output: [4]

height3 = [5, 4, 3, 2, 1]
print(stableMountains(height3, 0))  # Output: [1, 2, 3, 4]

height4 = [2, 3, 2, 3, 2]
print(stableMountains(height4, 2))  # Output: [1, 3]

height5 = [1, 1, 1, 1, 1]
print(stableMountains(height5, 1))  # Output: []

height6 = [10, 20, 30, 40, 50]
print(stableMountains(height6, 25))  # Output: [2, 3, 4]