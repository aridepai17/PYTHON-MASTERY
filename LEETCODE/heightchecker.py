# LEETCODE 1051

'''
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height.
Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
You are given an integer array heights representing the current order that the students are standing in. 
Each heights[i] is the height of the ith student in line (0-indexed).
Return the number of indices where heights[i] != expected[i].
'''

def heightChecker(heights):
    expected = sorted(heights)
    count = 0
    
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count

# Example usage
heights1 = [1, 1, 4, 2, 1, 3]
print(heightChecker(heights1))  # Output: 3

heights2 = [5, 1, 2, 3, 4]
print(heightChecker(heights2))  # Output: 5

heights3 = [1, 2, 3, 4, 5]
print(heightChecker(heights3))  # Output: 0

heights4 = [2, 2, 2, 2, 2]
print(heightChecker(heights4))  # Output: 0

heights5 = [3, 3, 3, 3, 3, 3]
print(heightChecker(heights5))  # Output: 0

heights6 = [1, 3, 2, 4, 5]
print(heightChecker(heights6))  # Output: 2