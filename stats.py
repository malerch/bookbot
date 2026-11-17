import re

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents

def get_num_words(file_contents):
    words = re.split(r'[ \s]+', file_contents)
    num_words = len(words)

    return num_words

def count_characters(file_contents):
    character_count = {}

    for character in file_contents.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

def sort_on(items):
    return items["num"]

def sort_character_count(character_count):
    sorted_character_count = []

    for character in character_count:
        character_entry = {}
        character_entry["char"] = character
        character_entry["num"] = character_count[character]

        sorted_character_count.append(character_entry)

    sorted_character_count.sort(reverse=True, key=sort_on)

    return sorted_character_count