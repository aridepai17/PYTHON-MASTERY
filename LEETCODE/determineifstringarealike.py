# LEETCODE 1704

'''
You are given a string s of even length. 
Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.
'''

def halvesAreAlike(s):
  vowels = set('aeiouAEIOU')
  n = len(s) // 2
  a, b = s[:n], s[n:]
  
  def countVowels(sub):
    return sum(1 for char in sub if char in vowels)
  
  return countVowels(a) == countVowels(b)

# Example usage:
s1 = "book"
print(halvesAreAlike(s1))  # Output: True

# Additional examples:
s2 = "textbook"
print(halvesAreAlike(s2))  # Output: False

s3 = "aabb"
print(halvesAreAlike(s3))  # Output: True

s4 = "AbCdEfGh"
print(halvesAreAlike(s4))  # Output: True

s5 = "xyzzzz"
print(halvesAreAlike(s5))  # Output: False

s6 = "AaEeIiOoUu"
print(halvesAreAlike(s6))  # Output: True

s7 = "abcdeefg"
print(halvesAreAlike(s7))  # Output: False

s8 = "aA"
print(halvesAreAlike(s8))  # Output: True

s9 = "oO"
print(halvesAreAlike(s9))  # Output: True

s10 = "helloHELLO"
print(halvesAreAlike(s10))  # Output: True