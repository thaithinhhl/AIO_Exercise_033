file_path = "E:\AIO.txt"


def count_words_in_file(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                word = ''.join(filter(str.isalpha, word))
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count


print(count_words_in_file(file_path))
