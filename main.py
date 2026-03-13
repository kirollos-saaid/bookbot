def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")


main()
