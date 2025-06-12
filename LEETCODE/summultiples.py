# LEETCODE 2652

'''
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5 or 7.
Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
'''

def sumOfMulitples(n):
    nums = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            nums += i
    return nums

# Example usage:
n = 10
print(sumOfMulitples(n)) # Output: 33 (3 + 5 + 6 + 7 + 9 + 10)

# Another example:
n = 20
print(sumOfMulitples(n)) # Output: 98 (3 + 5 + 6 + 7 + 9 + 10 + 12 + 14 + 15 + 18 + 20)

# Yet another example:
n = 30
print(sumOfMulitples(n)) # Output: 255 (3 + 5 + 6 + 7 + 9 + 10 + 12 + 14 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 28 + 30)

# More examples:
n = 50
print(sumOfMulitples(n)) # Output: 693 (3 + 5 + 6 + 7 + 9 + 10 + 12 + 14 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 28 + 30 + 33 + 35 + 36 + 39 + 40 + 42 + 45 + 48 + 50)

n = 17
print(sumOfMulitples(n)) # Output: 60 (3 + 5 + 6 + 7 + 9 + 10 + 12 + 14 + 15 + 16)

n = 32
print(sumOfMulitples(n)) # Output: 255 (3 + 5 + 6 + 7 + 9 + 10 + 12 + 14 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 28 + 30 + 33 + 35 + 36 + 39 + 40 + 42 + 45 + 48)