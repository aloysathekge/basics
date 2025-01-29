def word_counter(sentence):
    words_count = {}

    for word in sentence.split():
        words_count[word] = words_count.get(word, 0) + 1

    sorted_words = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_words


result = word_counter(
    "the quick brown fox jumps over the lazy dog and the dog jumps over the fox"
)
print(result)

# # What I learned

# 1. dict.items() returns dictionary
# 2. key in sorted function is used to determine how we sort
# 3. word_counts[word] = word_counts.get(word, 0) + 1 =>
