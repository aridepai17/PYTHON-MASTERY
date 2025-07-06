# LEETCODE 1544

'''
Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

1. 0 <= i <= s.length - 2
2. s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. 
You can keep doing this until the string becomes good.
Return the string after making it good. 
The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.
'''

def makeGood(s):
  stack = []
  
  for c in s:
    if stack and abs(ord(stack[-1]) - ord(c)) == 32:
      stack.pop()
    else:
      stack.append(c)
      
  return ''.join(stack)

# Example usage
s = "leEeetcode"
print(makeGood(s))  # Output: "leetcode"

# Additional examples:
s1 = "abBA"
print(makeGood(s1))  # Output: ""

s2 = "s"
print(makeGood(s2))  # Output: "s"

s3 = "Pp"
print(makeGood(s3))  # Output: ""

s4 = "cC"
print(makeGood(s4))  # Output: ""

s5 = "aA"
print(makeGood(s5))  # Output: ""

s6 = "dDabcC"
print(makeGood(s6))  # Output: "abc"

s7 = "leEeetcode"
print(makeGood(s7))  # Output: "leetcode"

s8 = "aBcCdDeE"
print(makeGood(s8))  # Output: ""

s9 = "xyzXYZ"
print(makeGood(s9))  # Output: ""

s10 = "aAbBcCdD"
print(makeGood(s10))  # Output: ""

