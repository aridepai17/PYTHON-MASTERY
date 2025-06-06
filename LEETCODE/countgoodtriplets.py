# LEETCODE 1534

'''
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.
Return the number of good triplets.
'''

def countGoodTriplets(arr, a, b, c):
    goodtriplets = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        goodtriplets += 1
    return goodtriplets

# Example usage:
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
print(countGoodTriplets(arr, a, b, c))  # Output: 4

# Another example:
arr = [1, 1, 2, 2, 3]
a = 1
b = 3
c = 4
print(countGoodTriplets(arr, a, b, c))  # Output: 12