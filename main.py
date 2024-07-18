from string import ascii_lowercase as alc

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    pprint(book_path=book_path, text=text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    text = text.lower()
    for i in alc:
        char_dict[i] = text.count(i)
    return char_dict

def sort_on(dict):
    return dict["num"]

def pprint(book_path, text):
    print(f"--- Begin report of {book_path}")
    print(f"{count_words(text)} words found in the document")
    char_dict = count_characters(text)
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    for i in sorted_dict:
        print(f"The '{i}' character was found {sorted_dict[i]} times")
    print("--- End report ---")


main()