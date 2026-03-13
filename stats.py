def count_words(text):
    words = text.split()
    return len(words)


def count_unique_chars(text):
    lowercased = text.lower()
    chars = {}
    for char in lowercased:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars
