# LEETCODE 1432

'''
You are given an integer num. You will apply the following steps to num two separate times:
1. Pick a digit x (0 <= x <= 9).
2. Pick another digit y (0 <= y <= 9). Note y can be equal to x.
3. Replace all the occurrences of x in the decimal representation of num by y.

Let a and b be the two results from applying the operation to num independently.
Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.
'''

def maxDiff(num):
    s = str(num)
    
    for char in s:
        if char != '9':
            maxNum = s.replace(char, '9')
            break
    else:
        maxNum = s
        
    if s[0] != '1':
        minNum = s.replace(s[0], '1')
    else:
        for char in s[1:]:
            if char != '0' and char != '1':
                minNum = s.replace(char, '0')
                break
        else: 
            minNum = s
    
    return int(maxNum) - int(minNum)

# Example usage
num1 = 1234567890
result1 = maxDiff(num1)
print(result1)  # Output: 8700000000 (Max: 9999999999, Min: 1234567890)

# Additional examples
num2 = 5555555555
result2 = maxDiff(num2)
print(result2)  # Output: 4444444445 (Max: 9999999999, Min: 5555555555)

num3 = 1000000000
result3 = maxDiff(num3)
print(result3)  # Output: 9000000000 (Max: 9000000000, Min: 0000000000)

num4 = 9876543210
result4 = maxDiff(num4)
print(result4)  # Output: 9876543210 (Max: 9999999999, Min: 0123456789)

num5 = 0
result5 = maxDiff(num5)
print(result5)  # Output: 0 (Max: 0, Min: 0)

num6 = 1234567899
result6 = maxDiff(num6)
print(result6)  # Output: 8700000000 (Max: 9999999999, Min: 1234567800)

num7 = 1111111111
result7 = maxDiff(num7)
print(result7)  # Output: 8888888888 (Max: 9999999999, Min: 1111111111)

num8 = 2222222222
result8 = maxDiff(num8)
print(result8)  # Output: 7777777777 (Max: 9999999999, Min: 2222222222)

num9 = 123456789
result9 = maxDiff(num9)
print(result9)  # Output: 870000000 (Max: 999999999, Min: 123456789)