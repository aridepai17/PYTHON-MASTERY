# Write a function to find all pairs of an integer array whose sum is equal to a given number.
# Do not consider commutative pairs.

def pair_sum(myList, sum):
    result = []
    
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(f"{myList[i]}+{myList[j]}")
    return result

# Example usage:
myList = [1, 2, 3, 4, 5]
sum_value = 5
result = pair_sum(myList, sum_value)
print(result) # Output: ['1+4', '2+3']

# Another example usage:
myList2 = [-5, -2, 0, 3, 5, 7]
sum_value2 = 5
result2 = pair_sum(myList2, sum_value2)
print(result2) # Output: ['-2+7', '0+5']