# Define a function to count the frequency of words in a given list of words.

def count_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Example usage
word_frequency = count_word_frequency(words)
print("Word Frequency:", word_frequency)
# Output: Word Frequency: {'apple': 3, 'banana': 2, 'orange': 1}



