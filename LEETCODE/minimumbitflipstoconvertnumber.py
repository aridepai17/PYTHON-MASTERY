# LEETCODE 2220

'''
A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.
For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. 
We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
'''

def minBitFlips(start, goal):
    xor = start ^ goal
    return bin(xor).count('1')

# Example usage
start = 10
goal = 7
print(minBitFlips(start, goal))  # Output: 3

# Additional examples
start2 = 5
goal2 = 2
print(minBitFlips(start2, goal2))  # Output: 3 (Binary: 101 -> 010)

start3 = 0
goal3 = 0
print(minBitFlips(start3, goal3))  # Output: 0 (No flips needed)

start4 = 15
goal4 = 0
print(minBitFlips(start4, goal4))  # Output: 4 (Binary: 1111 -> 0000)

start5 = 8
goal5 = 15
print(minBitFlips(start5, goal5))  # Output: 3 (Binary: 1000 -> 1111)

start6 = 1
goal6 = 2
print(minBitFlips(start6, goal6))  # Output: 2 (Binary: 01 -> 10)

start7 = 31
goal7 = 0
print(minBitFlips(start7, goal7))  # Output: 5 (Binary: 11111 -> 00000)

start8 = 255
goal8 = 0
print(minBitFlips(start8, goal8))  # Output: 8 (Binary: 11111111 -> 00000000)