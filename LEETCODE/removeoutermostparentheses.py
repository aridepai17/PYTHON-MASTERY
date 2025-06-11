# LEETCODE 1021

'''
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
'''

def removeOuterParentheses(s):
    count = 0
    result = []
    
    for char in s:
        if char == '(' and count > 0:
            result.append(char)
        if char == ')' and count > 1:
            result.append(char)
        if char == '(':
            count += 1
        else:
            count -= 1
    return ''.join(result)

# Example usage:
s1 = "(()())(())"
print(removeOuterParentheses(s1))  # Output: "()()()"

s2 = "(()())(())(()(()))"
print(removeOuterParentheses(s2))  # Output: "()()()()(())"

s3 = "()()"
print(removeOuterParentheses(s3))  # Output: ""

s4 = "(()())"
print(removeOuterParentheses(s4))  # Output: "()()"

s5 = "((()))"
print(removeOuterParentheses(s5))  # Output: "()()"

s6 = "(((())))"
print(removeOuterParentheses(s6))  # Output: "()(())"