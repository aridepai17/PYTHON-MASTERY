# LEETCODE 1342

'''
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''

def numberOfSteps(num):
  steps = 0
  
  while num > 0:
    if num % 2 == 0:
      num //= 2
    else:
      num -= 1
    steps += 1
  return steps

# Example usage
num1 = 14
print(numberOfSteps(num1))  # Output: 6

# Additional examples
num2 = 8
print(numberOfSteps(num2))  # Output: 4

num3 = 123
print(numberOfSteps(num3))  # Output: 12

num4 = 0
print(numberOfSteps(num4))  # Output: 0

num5 = 1
print(numberOfSteps(num5))  # Output: 1

num6 = 15
print(numberOfSteps(num6))  # Output: 6

num7 = 32
print(numberOfSteps(num7))  # Output: 6

num8 = 100
print(numberOfSteps(num8))  # Output: 9

num9 = 99
print(numberOfSteps(num9))  # Output: 10

num10 = 50
print(numberOfSteps(num10))  # Output: 7