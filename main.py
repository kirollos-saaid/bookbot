from stats import count_unique_chars, count_words, sort_chars


def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    unique_char_count = count_unique_chars(book_text)
    sorted_chars = sort_chars(unique_char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count -------")
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()
