# LEETOCDE 3174

'''
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
1. Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.
Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.
'''

def clearDigits(s):
    stack = []
    
    for char in s:
        if char.isdigit():
            stack.pop()
        else:
            stack.append()
    return ''.join(stack)

# Example usage:
s = "a1b2c3d4"
print(clearDigits(s))  # Output: "abcd"

# Another example:
s2 = "abc"
print(clearDigits(s2))  # Output: "abc" (no digits to remove)

# Yet another example:
s3 = "12345"
print(clearDigits(s3))  # Output: "" (all digits, nothing left)

# Yet another example:
s4 = "a1b23cd"
print(clearDigits(s4))  # Output: "acd" (removes '1' and 'b', then '2' and 'c')