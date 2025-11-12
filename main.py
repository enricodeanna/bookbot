import sys
from stats import words_count
from stats import characters_count
from stats import dic_list_sorted

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    num_words = words_count(file_contents)
    print("============ BOOKBOT ============\nAnalyzing book found at ...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    characters_dictionary = (characters_count(file_contents))
    sorted = (dic_list_sorted(characters_dictionary))
    for char in sorted:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
        
main()

