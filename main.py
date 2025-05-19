from stats import count_words 
from stats import count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # print(get_book_text("./books/frankenstein.txt"))
    count = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{count} words found in the document")
    letter_counts = count_letters(get_book_text("./books/frankenstein.txt"))
    print(letter_counts)

main()
