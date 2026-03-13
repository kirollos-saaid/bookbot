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


def sort_on(item):
    return item["num"]


def sort_chars(chars):
    sorted_list = []
    for char, count in chars.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
