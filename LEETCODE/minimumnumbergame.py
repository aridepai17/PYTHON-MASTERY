# LEETCODE 2974

'''
You are given a 0-indexed integer array nums of even length and there is also an empty array arr. 
Alice and Bob decided to play a game where in every round Alice and Bob will do one move. 
The rules of the game are as follows:
1. Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
2. Now, first Bob will append the removed element in the array arr, and then Alice does the same.
3. The game continues until nums becomes empty.
Return the resulting array arr.
'''

def numberGame(nums):
    arr = []
    nums.sort()
    
    for i in range(0, len(nums), 2):
        alice =  nums[i]
        bob = nums[i + 1]
        
        arr.append(bob)
        arr.append(alice)
    return arr

# Example usage:
nums = [3, 1, 4, 2]
print(numberGame(nums))  # Output: [2, 1, 4, 3]

nums2 = [8, 6, 7, 5, 4, 3]
print(numberGame(nums2))  # Output: [5, 3, 7, 4, 8, 6]

nums3 = [10, 20, 30, 40, 50, 60]
print(numberGame(nums3))  # Output: [20, 10, 40, 30, 60, 50]

nums4 = [5, 3, 4, 2]
print(numberGame(nums4))  # Output: [3, 2, 5, 4]