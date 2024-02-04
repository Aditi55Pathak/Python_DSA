def count_the_word(words):
    freq_dict = {}
    for i in words:
        freq_dict[i] = freq_dict.get(i, 0) + 1
    return freq_dict


words = ["apple", "orange", "banana", "apple", "orange", "apple"]
result = count_the_word(words)

print(result)
