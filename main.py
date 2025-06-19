import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    count = get_num_characters(text)
    sorted_count = sort_chars(count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for char in sorted_count:
        print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")

main()