# LEETCODE 3099

# An integer is a Harshad number if it is divisible by the sum of its digits.
# You are given an integer x. Return the sum of the digits of x if it is a Harshad number, otherwise return -1.

def sumOfTheDigitsOfHarshadNumber(x):
    digitsum = sum(int(digit) for digit in str(x))
    if x % digitsum == 0:
        return digitsum
    else:
        return -1
    
# Example usage:
x = 18
print(sumOfTheDigitsOfHarshadNumber(x))  # Output: 9 (1 + 8 = 9, and 18 is divisible by 9)

# Another example usage:
x = 19
print(sumOfTheDigitsOfHarshadNumber(x))  # Output: -1 (1 + 9 = 10, and 19 is not divisible by 10)

# Yet another example usage:
x = 21
print(sumOfTheDigitsOfHarshadNumber(x))  # Output: 3 (2 + 1 = 3, and 21 is divisible by 3)