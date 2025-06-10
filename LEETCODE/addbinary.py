# LEETCODE 67

# Given two binary strings a and b, return their sum as a binary string

def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# Example usage:
a = "1010"
b = "1101"
print(addBinary(a, b))  # Output: "10111"

a2 = "111"
b2 = "1"
print(addBinary(a2, b2))  # Output: "1000"

a3 = "0"
b3 = "0"
print(addBinary(a3, b3))  # Output: "0"

a4 = "1"
b4 = "1"
print(addBinary(a4, b4))  # Output: "10"

a5 = "110"
b5 = "101"
print(addBinary(a5, b5))  # Output: "1011"