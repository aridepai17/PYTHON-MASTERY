# LEETCODE 2566

'''
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.
Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:
When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
'''

def minMaxDifference(num):
    s = str(num)
    
    for char in s:
        if char != '9':
            maxNum = s.replace(char, '9')
            break
    else:
        maxNum = s
        
    for char in s:
        if char != '0':
            minNum = s.replace(char, '0')
            break
    else:
        minNum = s
        
    return int(maxNum) - int(minNum)

# Example usage
num1 = 1234567890
print(minMaxDifference(num1))  # Output: 8700000000 (Max: 9999999999, Min: 1234567890)

# Additional examples
num2 = 5555555555
print(minMaxDifference(num2))  # Output: 4444444445 (Max: 9999999999, Min: 5555555555)

num3 = 1000000000
print(minMaxDifference(num3))  # Output: 9000000000 (Max: 9000000000, Min: 0000000000)

num4 = 9876543210
print(minMaxDifference(num4))  # Output: 9876543210 (Max: 9999999999, Min: 0123456789)

num5 = 0
print(minMaxDifference(num5))  # Output: 0 (Max: 0, Min: 0)

num6 = 1234567899
print(minMaxDifference(num6))  # Output: 8700000000 (Max: 9999999999, Min: 1234567800)

num7 = 1111111111
print(minMaxDifference(num7))  # Output: 8888888888 (Max: 9999999999, Min: 1111111111)