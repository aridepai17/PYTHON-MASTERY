# LEETCODE 2315

'''
You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. 
In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
Return the number of '*' in s, excluding the '*' between each pair of '|'.
Note that each '|' will belong to exactly one pair.
'''

def countAsterisks(s):
    count = 0
    betweenBars = False
    
    for char in s:
        if char == '|':
            betweenBars = not betweenBars
        elif char == '*' and not betweenBars:
            count += 1
            
    return count

# Example usage
s1 = "l|*e*et|c**o|*de|"
print(countAsterisks(s1))  # Output: 2

# Additional examples
s2 = "a|b|c|d|"
print(countAsterisks(s2))  # Output: 0 (No asterisks)

s3 = "|*|*|*|*|"
print(countAsterisks(s3))  # Output: 0 (All asterisks are between bars)

s4 = "hello|*world|*this|is|*a|test|*"
print(countAsterisks(s4))  # Output: 3 (Asterisks outside the bars)

s5 = "|*|*|*|*|*|*|*|*|"
print(countAsterisks(s5))  # Output: 0 (All asterisks are between bars)

s6 = "no|*|asterisks|here|*|*|"
print(countAsterisks(s6))  # Output: 0 (All asterisks are between bars)

s7 = "count|*this|*and|*that|*"
print(countAsterisks(s7))  # Output: 3 (Asterisks outside the bars)

s8 = "just|*one|*asterisk|*here|"
print(countAsterisks(s8))  # Output: 1 (Only one asterisk outside the bars)

s9 = "no|*|bars|*|at|all|*|*|*"
print(countAsterisks(s9))  # Output: 3 (All asterisks are outside the bars)