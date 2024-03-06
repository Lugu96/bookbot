def main():
    from operator import itemgetter, attrgetter
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = [{"character":key, "count": value} for key, value in chars_dict.items() if key.isalpha()]
    sorted_list = sorted(chars_list, key=itemgetter("count"), reverse=True)
    i = 0
    print(f"--- Begin report of {book_path}---")
    print(f"{num_words} words found in the document")
    for item in sorted_list:
        
        print(f"the '{sorted_list[i]["character"]}' character was found {sorted_list[i]["count"]} times")
        i+=1
    print("end report")
def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()