# LEETCODE 258

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

def addDigits(num):
    if num < 10:
        return num  
    
    while num >= 10:
        total = 0
        for digit in str(num):
            total += int(digit)
        num = total
    return num

# Alternate digital modulo 9 approach
def addDigitsModulo(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

# Example usage
num1 = 38
print(addDigits(num1))  # Output: 2

num2 = 123
print(addDigits(num2))  # Output: 6

# Additional examples
num3 = 0
print(addDigits(num3))  # Output: 0 (Single digit)

num4 = 9
print(addDigits(num4))  # Output: 9 (Single digit)

num5 = 45
print(addDigits(num5))  # Output: 9 (4 + 5 = 9)

num6 = 99
print(addDigits(num6))  # Output: 9 (9 + 9 = 18 -> 1 + 8 = 9)

num7 = 1234
print(addDigits(num7))  # Output: 1 (1 + 2 + 3 + 4 = 10 -> 1 + 0 = 1)

num8 = 9876
print(addDigits(num8))  # Output: 3 (9 + 8 + 7 + 6 = 30 -> 3 + 0 = 3)

num9 = 1001
print(addDigits(num9))  # Output: 2 (1 + 0 + 0 + 1 = 2)

num10 = 99999
print(addDigits(num10))  # Output: 9 (9 + 9 + 9 + 9 + 9 = 45 -> 4 + 5 = 9)