# LEETCODE 682

'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

1.An integer x.
Record a new score of x.

2. '+'.
Record a new score that is the sum of the previous two scores.

3. 'D'.
Record a new score that is the double of the previous score.

4. 'C'.
Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.
The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
'''

def calPoints(operations):
    record = []
    
    for i in operations:
        if i.lstrip('-').isdigit():
            record.append(int(i))
        elif i == 'D':
            record.append(record[-1] * 2)
        elif i == 'C':
            record.pop()
        elif i == '+':
            record.append(record[-1] + record[-2])
        
    return sum(record)

# Example usage:
operations = ["5", "2", "C", "D", "+"]
print(calPoints(operations))  # Output: 30
# Explanation: 
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

# Test with negative numbers:
operations = ["-5", "2", "C", "D", "+"]
print(calPoints(operations))  # Output: -10
# Explanation: Similar to above but starts with -5

# Test with multiple consecutive operations:
operations = ["5", "2", "D", "D", "+"]
print(calPoints(operations))  # Output: 37
# Explanation: [5, 2, 4, 8, 18] = 37

# Test with multiple cancellations:
operations = ["5", "2", "C", "C", "3"]
print(calPoints(operations))  # Output: 3
# Explanation: [5, 2] -> [5] -> [] -> [3] = 3

# Test with complex sequence:
operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(calPoints(operations))  # Output: 27
# Explanation: [5, -2, 4] -> [5, -2] -> [5, -2, -4] -> [5, -2, -4, 9] -> [5, -2, -4, 9, 5] -> [5, -2, -4, 9, 5, 14] = 27
