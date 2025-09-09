# problem -1
# Define a function to count the frequency of words in a given list of words.
# Example:
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# count_word_frequency(words)
# Output:
#  {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    new_dict={}
    for word in words:
        new_dict[word] = new_dict.get(word,0) + 1
    return new_dict

print(count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))

# problem -2

# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
# Example:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# merge_dicts(dict1, dict2)
# Output:
# {'a': 1, 'b': 5, 'c': 7, 'd': 5}

#method-1
def merged_dicts1(dict1,dict2):
    merged = dict1.copy()
    for key,value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value

    return merged

print(merged_dicts1({'a':1, 'b':2, 'c':3},{'b':3, 'c':4, 'd':5}))

#method-2
def merged_dicts2(dict1,dict2):
    merged = dict1.copy()
    for key,value in dict2.items():
        merged[key] = merged.get(key,0) + value
    return merged

print(merged_dicts2({'a':1, 'b':2, 'c':3},{'b':3, 'c':4, 'd':5}))

#Problem -3
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.
#
# Example:
# my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict))
# Output:
# b
def max_value_key(my_dict):
    return max(my_dict, key= my_dict.get)

print(max_value_key({'a':5,'b':9,'c':2}))


# Problem -4
# Reverse Key-Value Pairs
# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.
#
# Example:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# reverse_dict(my_dict)
# Output:
# {1: 'a', 2: 'b', 3: 'c'}

def reverse_dict(my_dict):
    new_dict = dict()
    for key,value in my_dict.items():
        new_dict[value] = key
    return new_dict

print(reverse_dict({'a':1, 'b':2, 'c':3}))
