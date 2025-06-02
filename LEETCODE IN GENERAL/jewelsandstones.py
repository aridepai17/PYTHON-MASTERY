# LEETCODE 771

'''
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have.
Each character in stone is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a diffirent type of stone from "A".
'''

def numJewelsInStones(jewels, stones):
    singlejewel = set(jewels)
    count = 0
    
    for stone in stones:
        if stone in singlejewel:
            count += 1
    return count

# Example usage:
jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))  # Output: 3

# Another example usage:
jewels = "z"
stones = "ZZ"
print(numJewelsInStones(jewels, stones))  # Output: 0

# Yet another example usage:
jewels = "ab"
stones = "banana"
print(numJewelsInStones(jewels, stones))  # Output: 4