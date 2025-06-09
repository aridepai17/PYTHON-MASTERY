# LEETCODE 1221

'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it into some number of substrings such that:
Each substring is balanced.
Return the maximum number of balanced strings you can obtain.
'''

def balancedStringSplit(s):
    count = 0
    balanced = 0
    
    for char in s:
        if char == 'L':
            balanced += 1
        else:
            balanced -= 1
            
        if balanced == 0:
            count += 1
    
    return count

# Example usage:
s = "RLRRLLRLRL"
result = balancedStringSplit(s)
print(result) # Output: 4

s2 = "RLLLLRRRLR"
result2 = balancedStringSplit(s2)
print(result2) # Output: 3

s3 = "LLLLRRRR"
result3 = balancedStringSplit(s3)
print(result3) # Output: 1

s4 = "RLRRRLLRLL"
result4 = balancedStringSplit(s4)
print(result4) # Output: 2

s5 = "RLRLRLRL"
result5 = balancedStringSplit(s5)
print(result5) # Output: 2