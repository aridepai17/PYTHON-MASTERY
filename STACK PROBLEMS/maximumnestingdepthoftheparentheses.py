# LEETCODE 1614

# Given a valid parentheses string s, return the nesting depth of s.
# The nesting depth is the maximum number of nested parentheses.

def maxDepth(s):
    depth = 0
    maxdepth = 0
    
    for char in s:
        if char == '(':
            depth += 1
            maxdepth = max(maxdepth, depth)
        elif char == ')':
            depth -= 1
    return maxdepth

# Example usage:
print(maxDepth("()"))          # Output: 1
print(maxDepth("(())"))        # Output: 2
print(maxDepth("(()())"))      # Output: 2
print(maxDepth("((()))"))      # Output: 3
print(maxDepth("()()"))        # Output: 1
print(maxDepth("((((()))))"))  # Output: 4
print(maxDepth("()(()())"))    # Output: 2
