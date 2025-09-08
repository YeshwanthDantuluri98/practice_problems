# problem -1
# Define a function to count the frequency of words in a given list of words.
# Example:
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# count_word_frequency(words)
# Output:
#
#  {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    new_dict={}
    for word in words:
        new_dict[word] = new_dict.get(word,0) + 1
    return new_dict

print(count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))

