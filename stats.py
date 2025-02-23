def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(file):
    return len(file.split())

def get_chars_dict(file):
    characters = {}
    for ch in file.lower():
        if ch in characters:
            characters[ch] += 1
        else:
            characters[ch] = 1
    return characters

def to_list(dict):
    result = []
    for key in dict:
        result.append({"letter": key, "value": dict[key]})
    return result

def sort_on(dict):
    return dict["value"]

# def print_report(book_path, num_words, chars_dict):
#     list_chars = to_list(chars_dict)
#     list_chars.sort(reverse=True, key=sort_on)

#     print(f"--- Begin report of {book_path} ---")
#     print(f"{num_words} words found in the document")
#     print()
    
#     for ch in list_chars:
#         letter, value = ch["letter"], ch["value"]
#         if letter.isalpha():
#             print(f"The '{letter}' character was found {value} times")
#     print("--- End report ---")

def print_report(book_path, num_words, chars_dict):
    list_chars = to_list(chars_dict)
    list_chars.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for ch in list_chars:
        letter, value = ch["letter"], ch["value"]
        if letter.isalpha():
            print(f"{letter}: {value}")
    print("============= END ===============")
