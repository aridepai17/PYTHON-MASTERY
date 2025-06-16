# LEETCODE 1859

'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.
A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
'''

def sortSentence(s):
    words = s.split()
    result = [] * len(words)
    
    for word in words:
        index = int(word[-1]) - 1
        result[index] = word[:-1]
        
    return ' '.join(result)

# Example usage
s1 = "sentence4 a3 is2 This1"
print(sortSentence(s1))  # Output: "This is a sentence"

# Additional examples
s2 = "is2 sentence4 This1 a3"
print(sortSentence(s2))  # Output: "This is a sentence"

s3 = "word3 another1 example2"
print(sortSentence(s3))  # Output: "another example word"

s4 = "apple1 banana2 cherry3"
print(sortSentence(s4))  # Output: "apple banana cherry"

s5 = "dog3 cat1 mouse2"
print(sortSentence(s5))  # Output: "cat mouse dog"

s6 = "hello1 world2"
print(sortSentence(s6))  # Output: "hello world"

s7 = "one1 two2 three3 four4"
print(sortSentence(s7))  # Output: "one two three four"
    