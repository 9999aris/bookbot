def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)

main()

def num_words():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        words = f.read()
        word_count = len(words.split())
    return word_count

print(f"{num_words} words found in the document")