from stats import count_words, count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    contents = get_book_text('books/frankenstein.txt')
    num_words = count_words(contents)
    print(f"Found {num_words} total words")

    characters = count_characters(contents)
    print(characters)

main()