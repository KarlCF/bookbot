def main():
    books_folder = "books/"
    book_file = "frankenstein.txt"
    book_path = books_folder+book_file
    text = get_text(book_path)
    num_words = word_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in document.")
    character_count = char_count(text)
    sorted_char = chars_dict_to_sorted_list(character_count)
    for i in sorted_char:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times.")
    print("--- End of report ---")

def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    if type(text) is str:
        words = text.split()
        return len(words)
    elif type(text) is list():
        return len(text)

def char_count(text):
    text = text.lower()
    char_count = dict()
    for i in text:
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] += 1
    return char_count

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = list()
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
