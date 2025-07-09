# LEETCODE 504

# Given an integer num, return a string of its base 7 representation.

def convertToBase7(num):
  if num == 0:
    return "0"
  
  negative = num < 0
  num = abs(num)
  base7 = ""
  
  while num > 0:
    base7 = str(num % 7) + base7
    num //= 7
  
  return "-" + base7 if negative else base7

# Example usage:
num1 = 100
print(convertToBase7(num1))  # Output: "202"

num2 = 0
print(convertToBase7(num2))  # Output: "0"

num3 = -7
print(convertToBase7(num3))  # Output: "-10"

num4 = 14
print(convertToBase7(num4))  # Output: "20"

num5 = 49
print(convertToBase7(num5))  # Output: "100"

num6 = 50
print(convertToBase7(num6))  # Output: "101"

num7 = -100
print(convertToBase7(num7))  # Output: "-202"

num8 = 1
print(convertToBase7(num8))  # Output: "1"

num9 = 6
print(convertToBase7(num9))  # Output: "6"

num10 = 8
print(convertToBase7(num10))  # Output: "11"

num11 = 343
print(convertToBase7(num11))  # Output: "1000"