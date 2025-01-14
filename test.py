def find_word_index(word_to_find: str, words: list) -> int:
    try:
        # Try to find the index of the word in the list
        return words.index(word_to_find)
    except ValueError:
        # If the word is not found it will return -1
        return -1
    
words_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Word found in the list
print(find_word_index('cherry', words_list))  # Output: 2

# Word not found in the list
print(find_word_index('fig', words_list))  # Output: -1