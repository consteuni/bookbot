import sys
from stats import count_words, count_characters, sort_characters


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


# Main function
if __name__ == "__main__":
    # Controlla se ci sono abbastanza argomenti
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Usa il secondo argomento come path del libro
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    # Conta le parole
    word_count = count_words(book_text)

    # Conta i caratteri
    char_count = count_characters(book_text)

    # Ordina i caratteri
    sorted_chars = sort_characters(char_count)

    # Stampa il report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Stampa solo caratteri alfabetici
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
