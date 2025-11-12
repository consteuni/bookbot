def count_words(text):
    words = text.split()
    return len(words)


# contare occorrenze di ogni parola e carattere usando {'p': 6121, 'r': 20818, 'o': 25225, ...
def count_characters(text):
    char_occurrences = {}

    for char in text:
        char_lower = char.lower()
        if char_lower in char_occurrences:
            char_occurrences[char_lower] += 1
        else:
            char_occurrences[char_lower] = 1

    return char_occurrences


def sort_characters(char_dict):
    """
    Takes a dictionary of characters and their counts and returns a sorted list of dictionaries.
    Each dictionary has 'char' and 'num' keys, sorted by count from greatest to least.
    """

    # Helper function per il sorting
    def sort_on(dict_item):
        return dict_item["num"]

    # Converti il dizionario in una lista di dizionari
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    # Ordina la lista usando il metodo .sort() con la helper function
    char_list.sort(key=sort_on, reverse=True)

    return char_list
