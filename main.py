import os
import sys
from stats import count_words,count_letters
def get_book_text(path):
    with open(path) as fp:
        file_contents=fp.read()
    return file_contents

def print_screen(path,wc,char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for val in char_count:
        if val.isalpha():
            print(f"{val}: {char_count[val]}")
    print("============= END ===============")

def main():
    try:
        PATH=sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text=get_book_text(PATH)
    num_words=count_words(text)    
    letter_count=count_letters(text)
    print_screen(PATH,num_words,letter_count)


if __name__ == '__main__' :
    main()