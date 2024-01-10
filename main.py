with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letter_occurence(text):
    char_dictionary = {}
    for char in text:
        char = char.lower()
        if char not in char_dictionary:
            char_dictionary.update({char: 1})
        else:
            char_dictionary[char] += 1
    return char_dictionary

def create_report(text):
    dict = count_letter_occurence(text)
    char_list = list(dict)
    sorted_list = char_list.copy()
    sorted_list.sort()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    for item in sorted_list:
        if item.isalpha():
            print(f"The '{item}' character was found {dict[item]} times")
    print("--- End report ---")

create_report(file_contents)

