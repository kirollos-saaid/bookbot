def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)


main()
