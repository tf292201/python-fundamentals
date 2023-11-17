def print_words(words, letters):
    """Given list of words, and a list of letters, print each in uppercase on a separate line that
    starts with the corresponding letter."""
    for word in words:
        for letter in letters:
            if letter == word[0]:
                print(word.upper())


print_words(["hi", "bye", "hello", "elevator", "enter", "goodbye"], ["e", "b"])
