import sys
from stats import number_of_words
from stats import characters
from stats import sorted_characters


def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


file_path = sys.argv[1]
content = get_book_text(file_path)


#print("============ BOOKBOT =============")
#print(f"Analyzing book found at {file_path}...")

num_words = number_of_words(content)
#print("------------- Word Count --------------")
print(f"Found {num_words} total words")


letters = characters(content)
#print(letters)


#print("----------- Character Count -----------")
sorted_letters = sorted_characters(letters)
#print("================ END ==================")