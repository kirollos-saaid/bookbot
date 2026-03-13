from stats import count_unique_chars, count_words


def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    unique_char_count = count_unique_chars(book_text)

    print(f"Found {word_count} total words")
    print(unique_char_count)


main()
