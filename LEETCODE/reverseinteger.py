# LEETCODE 7

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

def reverse(x):
    intmin, intmax = -2**31, 2**31 - 1
    
    if x < 0:
        reversedx = int("-" + str(abs(x))[::-1])
    else:
        reversedx = int(str(x)[::-1])
        
    if reversedx < intmin or reversedx > intmax:
        return 0 
    
    return reversedx

# Example usage:
x = 123
print(reverse(x))  # Output: 321

# Another example usage:
x = -123
print(reverse(x))  # Output: -321

# Yet another example usage:
x = 1534236469
print(reverse(x))  # Output: 0 (since it overflows the 32-bit signed integer range)

# Edge case usage:
x = 0
print(reverse(x))  # Output: 0 (reversing zero should still return zero)

# Example usage with leading zeros:
x = 120
print(reverse(x))  # Output: 21 (leading zeros are removed in the reversed integer)