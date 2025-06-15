# LEETCODE 1281

# Given an integer n, return the difference between the product of its digits and the sum of its digits.

def subtractProductAndSum(n):
    product = 1
    total = 0
    
    digits = [ int(d) for d in str(n) ]
    
    for d in digits:
        product *= d
        total += d
    
    return product - total

# Example usage
n1 = 234
result1 = subtractProductAndSum(n1)
print(result1)  # Output: 15 (Product: 2 * 3 * 4 = 24, Sum: 2 + 3 + 4 = 9, Difference: 24 - 9 = 15)

# Additional examples
n2 = 4421
result2 = subtractProductAndSum(n2)
print(result2)  # Output: 21 (Product: 4 * 4 * 2 * 1 = 32, Sum: 4 + 4 + 2 + 1 = 11, Difference: 32 - 11 = 21)

n3 = 123
result3 = subtractProductAndSum(n3)
print(result3)  # Output: 0 (Product: 1 * 2 * 3 = 6, Sum: 1 + 2 + 3 = 6, Difference: 6 - 6 = 0)

n4 = 999
result4 = subtractProductAndSum(n4)
print(result4)  # Output: 0 (Product: 9 * 9 * 9 = 729, Sum: 9 + 9 + 9 = 27, Difference: 729 - 27 = 702)

n5 = 0
result5 = subtractProductAndSum(n5)
print(result5)  # Output: 0 (Product: 0, Sum: 0, Difference: 0 - 0 = 0)

n6 = 5
result6 = subtractProductAndSum(n6)
print(result6)  # Output: 0 (Product: 5, Sum: 5, Difference: 5 - 5 = 0)

n7 = 10
result7 = subtractProductAndSum(n7)
print(result7)  # Output: -1 (Product: 1 * 0 = 0, Sum: 1 + 0 = 1, Difference: 0 - 1 = -1)