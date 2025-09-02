def number_of_words(content):
    words = content.split()
    return len(words)


def characters(content):
    lower_case = content.lower()
    letters = {}
    for char in lower_case:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters


def sorted_characters(content):
    sorted_letters = dict(sorted(content.items()))
    for key in sorted_letters:
        if key.isalpha():
            print(f"{key}: {sorted_letters[key]}")