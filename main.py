from stats import *

def main():
    contents = get_book_text("./books/frankenstein.txt")
    word_no = get_count_words(contents)
    print(f"{word_no} words found in the document")

    char_count = get_char_counts(contents)
    print(char_count)

main()
