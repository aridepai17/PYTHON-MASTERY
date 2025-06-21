# LEETCODE 70

'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

def climbStairs(n):
    if n <= 2:
        return n
    
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Example usage
n1 = 5
print(climbStairs(n1))  # Output: 8

n2 = 6
print(climbStairs(n2))  # Output: 13

n3 = 1
print(climbStairs(n3))  # Output: 1

n4 = 2
print(climbStairs(n4))  # Output: 2

n5 = 10
print(climbStairs(n5))  # Output: 89

n6 = 3
print(climbStairs(n6))  # Output: 3

n7 = 4
print(climbStairs(n7))  # Output: 5

n8 = 7
print(climbStairs(n8))  # Output: 21

n9 = 8
print(climbStairs(n9))  # Output: 34

n10 = 15
print(climbStairs(n10))  # Output: 987
