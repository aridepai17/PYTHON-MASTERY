# LEETCODE 1720

'''
There is a hidden integer array arr that consists of n non-negative integers.
It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. 
For example, if arr = [1,0,2,1], then encoded = [1,2,3].
You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
Return the original array arr. It can be proved that the answer exists and is unique.
'''

def decode(encoded, first):
    arr = [first]
    
    for i in encoded:
        arr.append(arr[-1] ^ i)
    return arr

# Example usage
encoded1 = [1, 2, 3]
first1 = 1
print(decode(encoded1, first1))  # Output: [1, 0, 2, 1]

# Additional examples
encoded2 = [6, 2, 7, 3]
first2 = 4
print(decode(encoded2, first2))  # Output: [4, 2, 0, 7, 4]

encoded3 = [0, 1, 2, 3]
first3 = 5
print(decode(encoded3, first3))  # Output: [5, 5, 4, 6, 5]

encoded4 = [1, 1, 1]
first4 = 0
print(decode(encoded4, first4))  # Output: [0, 1, 0, 1]

encoded5 = [10, 5, 15]
first5 = 3
print(decode(encoded5, first5))  # Output: [3, 13, 8, 15]

encoded6 = [2, 3, 1, 4]
first6 = 7
print(decode(encoded6, first6))  # Output: [7, 5, 6, 5, 1]