# LEETCODE 1078

'''
Given two strings first and second, consider occurrences in some text of the form "first second third", 
where second comes immediately after first, and third comes immediately after second.
Return an array of all the words third for each occurrence of "first second third".
'''

def findOccurences(text, first, second):
  words = text.split
  result = []
  
  for i in range(len(words) - 2):
    if words[i] == first and words[i+1] == second:
      result.append(words[i+2])
  
  return result

# Example usage
text = "alice is a good girl she is a good student"
a = "good"
b = "student"
print(findOccurences(text, a, b)) # Output: ["girl", "student"]

# Additional examples:
text1 = "the quick brown fox jumps over the lazy dog"
a1 = "quick"
b1 = "brown"
print(findOccurences(text1, a1, b1)) # Output: ["fox"]

text2 = "hello world hello universe"
a2 = "hello"
b2 = "world"
print(findOccurences(text2, a2, b2)) # Output: ["hello"]

text3 = "I love programming programming is fun"
a3 = "programming"
b3 = "is"
print(findOccurences(text3, a3, b3)) # Output: ["fun"]

text4 = "the cat sat on the mat"
a4 = "the"
b4 = "cat"
print(findOccurences(text4, a4, b4)) # Output: ["sat"]

text5 = "this is a test this is only a test"
a5 = "this"
b5 = "is"
print(findOccurences(text5, a5, b5)) # Output: ["a", "only"]

text6 = "one two three one two three"
a6 = "one"
b6 = "two"
print(findOccurences(text6, a6, b6)) # Output: ["three", "three"]

text7 = "apple banana apple orange banana apple"
a7 = "apple"
b7 = "banana"
print(findOccurences(text7, a7, b7)) # Output: ["apple"]

text8 = "dog cat dog mouse cat dog"
a8 = "dog"
b8 = "cat"
print(findOccurences(text8, a8, b8)) # Output: ["dog"]

text9 = "sun moon sun stars moon sun"
a9 = "sun"
b9 = "moon"
print(findOccurences(text9, a9, b9)) # Output: ["sun"]