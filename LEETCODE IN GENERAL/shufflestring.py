# LEETCODE 1528 

'''
You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.
'''

def restoreString(s, indices):
    result = [''] * len(s)
    
    for orgindex, targetindex in enumerate(indices):
        result[targetindex] = s[orgindex]
        
    return ''.join(result)


# Example usage:
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))  # Output: "leetcode"

# Another example usage:
s = "abc"
indices = [2,0,1]
print(restoreString(s, indices))  # Output: "cab"

# Yet another example usage:
s = "aiohn"
indices = [3,1,4,2,0]
print(restoreString(s, indices))  # Output: "nihao"