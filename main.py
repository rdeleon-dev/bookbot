from stats import count_words, count_characters, sort_items

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    contents = get_book_text('books/frankenstein.txt')
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