# LEETCODE 2011

'''
There is a programming language with only four operations and one variable X:
1. "++X" increments the value of X by 1.
2. "X++" increments the value of X by 1.
3. "--X" decrements the value of X by 1.
4. "X--" decrements the value of X by 1.
Initially, the value of X is 0.
Given an array of strings operations containing a list of operations, 
return the final value of X after performing all the operations.
'''

def finalValueAfterOperations(operations):
    x = 0
    for word in operations:
        if '+' in word:
            x += 1
        else:
            x -= 1
    return x

# Example usage:
operations = ["--X", "X++", "X++"]
print(finalValueAfterOperations(operations))  # Output: 1

# Another example:
operations = ["++X", "++X", "X++"]
print(finalValueAfterOperations(operations))  # Output: 3

# Yet another example:
operations = ["X++", "++X", "--X", "X--"]
print(finalValueAfterOperations(operations))  # Output: 0