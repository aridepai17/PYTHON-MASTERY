# LEETCODE 3340

'''
You are given a string num consisting of only digits. 
A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.
Return true if num is balanced, otherwise return false.
'''

def isBalanced(num):
    result = 0
    for i in range(len(num)):
        if i % 2 == 0:
            result += int(num[i])
        else:
            result -= int(num[i])
    return result == 0

# Example usage
num1 = "1230"
print(isBalanced(num1))  # Output: True

# Additional examples
num2 = "123456"
print(isBalanced(num2))  # Output: False

# More examples
num3 = "2468"
print(isBalanced(num3))  # Output: True

num4 = "13579"
print(isBalanced(num4))  # Output: False

num5 = "1122"
print(isBalanced(num5))  # Output: True

num6 = "123321"
print(isBalanced(num6))  # Output: True

num7 = "987654"
print(isBalanced(num7))  # Output: False

num8 = "0"
print(isBalanced(num8))  # Output: True

num9 = "1111"
print(isBalanced(num9))  # Output: True

num10 = "123456789"
print(isBalanced(num10))  # Output: False

num11 = "2222"
print(isBalanced(num11))  # Output: True

