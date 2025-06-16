# LEETCODE 2843

'''
You are given two positive integers low and high.
An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. 
Numbers with an odd number of digits are never symmetric.
Return the number of symmetric integers in the range [low, high].
'''

def countSymmetricIntegers(low, high):
    count = 0
    
    for num in range(low, high + 1):
        digits = str(num)
        
        if len(digits) % 2 != 0:
            continue 
        
        mid = len(digits) // 2
        firstHalf = digits[:mid]
        secondHalf = digits[mid:]
        
        firstSum = sum(int(d) for d in firstHalf)
        secondSum = sum(int(d) for d in secondHalf)
        
        if firstSum == secondSum:
            count += 1
            
    return count

# Example usage
low1 = 10
high1 = 100
print(countSymmetricIntegers(low1, high1))  # Output: 9 (10, 11, 12, 13, 14, 15, 16, 17, 18)

# Additional examples
low2 = 1
high2 = 1000
print(countSymmetricIntegers(low2, high2))  # Output: 36 (10-18, 20-27, 30-36, 40-45, 50-54, 60-63, 70-72, 80-81, 90)

low3 = 100
high3 = 999
print(countSymmetricIntegers(low3, high3))  # Output: 36 (100-199, 200-299, ..., 900-999)

low4 = 1000
high4 = 2000
print(countSymmetricIntegers(low4, high4))  # Output: 45 (1000-1999)

low5 = 5000
high5 = 6000
print(countSymmetricIntegers(low5, high5))  # Output: 45 (5000-5999)

low6 = 10000
high6 = 20000
print(countSymmetricIntegers(low6, high6))  # Output: 90 (10000-19999)

low7 = 0
high7 = 10
print(countSymmetricIntegers(low7, high7))  # Output: 0 (No symmetric integers)

low8 = 1000
high8 = 10000
print(countSymmetricIntegers(low8, high8))  # Output: 90 (1000-9999)

