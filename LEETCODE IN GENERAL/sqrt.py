# LEETCODE 69  
'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
'''
# Binary Search Optimal approach

def mySqrt(x):
    if x == 0:
        return 0
    l, r = 1, x
    while l <= r:
        mid = l + (r-l) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            l = mid + 1
        else:
            r = mid - 1 
    return r

# Example usage:
x = 8
print(mySqrt(x))  # Output: 2 (since sqrt(8) is approximately 2.828, rounded down to 2)

x = 16
print(mySqrt(x))  # Output: 4 (since sqrt(16) is exactly 4)

x = 0
print(mySqrt(x))  # Output: 0 (since sqrt(0) is 0)
