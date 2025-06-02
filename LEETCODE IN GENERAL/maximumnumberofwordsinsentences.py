# LEETCODE 2114

'''
A sentence is a list of words that are separated by single space wuth no leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words that appear in the sentence.
'''

def mostWordsFound(sentences):
    return max(len(sentence.split()) for sentence in sentences)