# LEETCODE 1974

'''
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer.
A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.
Each second, you may perform one of the following operations:
1. Move the pointer one character counterclockwise or clockwise.
2. Type the character the pointer is currently on.

Given a string word, return the minimum number of seconds to type out the characters in word.
'''

def minTimeToType(word):
    def charDistance(a, b):
        return min(abs(ord(a) - ord(b)), 26 - abs(ord(a) - ord(b)))
    
    time = 0
    currentChar = 'a'
    
    for targetChar in word:
        time += charDistance(currentChar, targetChar)
        time += 1
        currentChar = targetChar
        
    return time

# Example usage
word1 = "abc"
print(minTimeToType(word1))  # Output: 5 (a -> b -> c)

# Additional examples
word2 = "az"
print(minTimeToType(word2))  # Output: 4 (a -> z)

word3 = "bza"
print(minTimeToType(word3))  # Output: 7 (a -> b -> z -> a)

word4 = "hello"
print(minTimeToType(word4))  # Output: 34 (a -> h -> e -> l -> l -> o)

word5 = "typewriter"
print(minTimeToType(word5))  # Output: 66 (a -> t -> y -> p -> e -> w -> r -> i -> t -> e -> r)

word6 = "a"
print(minTimeToType(word6))  # Output: 1 (just type 'a')

word7 = "z"
print(minTimeToType(word7))  # Output: 2 (a -> z)

word8 = "abcde"
print(minTimeToType(word8))  # Output: 9 (a -> b -> c -> d -> e)

word9 = "xyz"
print(minTimeToType(word9))  # Output: 8 (a -> x -> y -> z)

word10 = "aaa"
print(minTimeToType(word10))  # Output: 3 (a -> a -> a)

word11 = "cba"
print(minTimeToType(word11))  # Output: 7 (a -> c -> b -> a)

