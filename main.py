import sys
from stats import get_num_words, get_num_chars, sort_char_dict

def get_book_text(f_path):
    with open(f_path) as f:
        f_content = f.read()
    
    return f_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    x = get_book_text(book_path) # add bookpath here 
    
    num_words = get_num_words(x)

    sorted_char_dict = sort_char_dict(get_num_chars(x))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_dict:
        if not char["char"].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")


main()
