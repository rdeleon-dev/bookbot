def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def main():
    contents = get_book_text('books/frankenstein.txt')
    num_words = count_words(contents)
    print(f"Found {num_words} total words")

main()