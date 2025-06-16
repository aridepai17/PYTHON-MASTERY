# LEETCODE 191

#Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

def hammingWeight(n):
    binaryOfn = bin(n)[2:]
    return binaryOfn.count('1')

# Example usage
n1 = 11  
print(hammingWeight(n1))  # Output: 3 (Binary: 1011)

n2 = 128
print(hammingWeight(n2))  # Output: 1 (Binary: 10000000)

# Additional examples
n3 = 0
print(hammingWeight(n3))  # Output: 0 (Binary: 0)

n4 = 1
print(hammingWeight(n4))  # Output: 1 (Binary: 1)

n5 = 2
print(hammingWeight(n5))  # Output: 1 (Binary: 10)

n6 = 3
print(hammingWeight(n6))  # Output: 2 (Binary: 11)

n7 = 16
print(hammingWeight(n7))  # Output: 1 (Binary: 10000)

n8 = 255
print(hammingWeight(n8))  # Output: 8 (Binary: 11111111)

n9 = 1024
print(hammingWeight(n9))  # Output: 1 (Binary: 10000000000)

n10 = 2048
print(hammingWeight(n10))  # Output: 1 (Binary: 100000000000)

n11 = 4095
print(hammingWeight(n11))  # Output: 12 (Binary: 111111111111)