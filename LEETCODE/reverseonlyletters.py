# LEETCODE 917

'''
Given a string s, reverse the string according to the following rules:
1. All the characters that are not English letters remain in the same position.
2. All the English letters (lowercase and uppercase) should be reversed.
Return s after reversing it.
'''

def reverseOnlyLetters(s):
  letters = [ char for char in s if char.isalpha() ]
  result = []
  
  for char in s:
    if char.isalpha():
      result.append(letters.pop())
    else:
      result.append(char)
  
  return ''.join(result)

# Example usage
s1 = "ab-cd"
print(reverseOnlyLetters(s1))  # Output: "dc-ba"

# New examples
s2 = "a-bC-dEf-ghIj"
print(reverseOnlyLetters(s2))  # Output: "j-Ih-gfE-dC-ba"

s3 = "Test1ng-Leet=code-Q!"
print(reverseOnlyLetters(s3))  # Output: "Qedo1ct-eeLg=ntse-T!"

s4 = ""
print(reverseOnlyLetters(s4))  # Output: ""

s5 = "7_28" 
print(reverseOnlyLetters(s5))  # Output: "7_28"

s6 = "ab-cd-ef-gh"
print(reverseOnlyLetters(s6))  # Output: "hg-fe-dc-ba"

s7 = "Hello-World!"
print(reverseOnlyLetters(s7))  # Output: "dlroW-olleH"

s8 = "123-456-789"
print(reverseOnlyLetters(s8))  # Output: "123-456-789"

s9 = "A man, a plan, a canal: Panama"
print(reverseOnlyLetters(s9))  # Output: "amanaP ,nalp ,nam A"

s10 = "Was it a car or a cat I saw?"
print(reverseOnlyLetters(s10))  # Output: "was it a car or a cat I saw?"