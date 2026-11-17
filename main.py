from stats import get_num_words, get_book_text, count_characters, sort_character_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    num_words = get_num_words(file_contents)

    character_count = count_characters(file_contents)
    sorted_character_count = sort_character_count(character_count)

    message = f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
"""

    for character_entry in sorted_character_count:
        if character_entry['char'].isalpha():
            message += f"{character_entry['char']}: {character_entry['num']}\n"

    message += "============= END ==============="
    
    print(message)


main()