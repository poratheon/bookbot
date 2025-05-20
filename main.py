import sys
from stats import count_words 
from stats import count_letters
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        book_location = sys.argv[1] 
        intro_text = f"============ BOOKBOT ============\nAnalyzing book found at {book_location}..."
        print(intro_text)
        count = count_words(get_book_text(book_location))
        print(f"----------- Word Count ----------\nFound {count} total words")
        print("--------- Character Count -------")
        letter_counts = count_letters(get_book_text(book_location))
        sorted_letters = sort_dictionary(letter_counts)
        for item in sorted_letters:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
main()

