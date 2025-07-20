def get_book_text(filepath):
    contents = None
    with open(filepath) as f:
        contents = f.read()
    return contents

def get_count_words(text):
    wordlist = text.split()
    return len(wordlist)

def get_char_counts(text):
    char_dict = {}

    text_lowercase = text.lower()
    for c in text_lowercase:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1

    return char_dict

def sort_char_count(char_count):
    sorted_dict = {k: v for k, v in sorted(char_count.items(), key = lambda item: item[1], reverse=True)}
    return sorted_dict
