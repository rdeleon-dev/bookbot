import sys

from stats import count_words, count_characters, sort_items

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}..")

    contents = get_book_text(book_path)
    num_words = count_words(contents)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    characters = count_characters(contents)
    sorted = sort_items(characters)

    print("--------- Character Count -------")
    for c in sorted:
        print( f"{c["char"]}: {c["num"]}" )

    print("============= END ===============")
main()