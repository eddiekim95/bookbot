def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_char_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"---Begin report of {book_path}")
    print(f"{num_words} words found in the document\n")
    
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"The {item["char"]} character was found {item["num"]} times")
    print("--- End Report ---")

def get_book_text(path):    #opens and returns the contents of a file
    with open(path)as f:
        return f.read()

def get_word_count(text):   #returns word count
    return len(text.split())

def get_char_count(text):    #returns dict of characters and count
    letters_count = {}
    text_lower = text.lower()
    for c in text_lower:
        if c in letters_count:
            letters_count[c] += 1
        else:
            letters_count[c] = 1
    return letters_count

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for c in chars_dict:
        sorted_list.append({"char": c, "num": chars_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

main()
