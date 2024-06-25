def count_chars(word):
    dict_string = {}

    for char in word:
        if char in dict_string:
            dict_string[char] += 1
        else:
            dict_string[char] = 1
    return dict_string


word = 'Happiness'
print(count_chars(word))
