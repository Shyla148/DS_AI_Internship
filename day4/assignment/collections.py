from collections import Counter

def get_top_frequent_words(words, top_n=2):
    """Returns the most common words and their counts using Counter."""
    counts = Counter(words)
    return counts.most_common(top_n)

# Program execution
word_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print("Most Frequent Words:", get_top_frequent_words(word_list))