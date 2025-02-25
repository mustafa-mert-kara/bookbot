import os
from stats import count_words
def get_book_text(path):
    with open(path) as fp:
        file_contents=fp.read()
    return file_contents

def main():
    text=get_book_text("books/frankenstein.txt")
    num_words=count_words(text)
    print(f"{num_words} words found in the document")

if __name__ == '__main__' :
    main()