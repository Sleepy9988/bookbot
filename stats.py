def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)


def get_num_chars(book_text):
    lower_case_text = book_text.lower()

    char_dict = dict()

    for char in lower_case_text:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict


def sort_on(char_count):
    return char_count["num"]

def sort_char_dict(char_dict):
    char_dict_list = []
    for key, value in char_dict.items():
        char_dict_list.append({"char": key, "num": value})
    
    char_dict_list.sort(reverse=True, key=sort_on)

    return char_dict_list


