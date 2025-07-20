import sys

from stats import *

def print_char_count(char_count):
    for k in char_count:
        if(k.isalpha()):
            print(f"{k}: {char_count[k]}")
    pass

def main():
    arg_count = len(sys.argv)
    if(arg_count != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    contents = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {filepath}...")

    word_no = get_count_words(contents)
    print("----------- Word Count ----------")
    print(f"Found {word_no} total words")

    char_count = get_char_counts(contents)
    char_count = sort_char_count(char_count)
    print("--------- Character Count -------")
    print_char_count(char_count)

    print("============= END ===============")

main()
