def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)

    count = get_word_count(text)
    #print(count)

    char_count = count_characters(text)
    #print(char_count)

    print("\n--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")

    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_char_count:
        print(f"The {char} character was found {count} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    word_count = 0
    words = text.split()

    for word in words:
        word_count += 1    
    
    return word_count

def count_characters(text):

    character_count = {}
    for char in text.lower():
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

    return character_count

main()