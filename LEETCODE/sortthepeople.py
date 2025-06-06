# LEETCODE 2418

'''
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights.
'''

def sortPeople(names, heights):
    heighttoname = {}
    result = []
    
    for h, n in zip(heights, names):
        heighttoname[h] = n
    
    for h in reversed(sorted(heights)):
        result.append(heighttoname[h])
    return result

# Example usage:
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(sortPeople(names, heights))  # Output: ['Mary', 'Emma', 'John']

# Another example:
names = ["Alice", "Bob", "Charlie"]
heights = [170, 180, 175]
print(sortPeople(names, heights))  # Output: ['Bob', 'Charlie', 'Alice']

# Another example:
names = ["Zoe", "Liam", "Olivia"]
heights = [160, 185, 170]
print(sortPeople(names, heights))  # Output: ['Liam', 'Olivia', 'Zoe']