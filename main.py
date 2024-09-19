def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

    count = get_word_count(text)
    print(count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    word_count = 0
    words = text.split()

    for word in words:
        word_count += 1    
    
    return word_count

main()