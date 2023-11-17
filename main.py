with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

def word_count():
    number_of_words = 0
    words = file_contents.split()
    for word in words:
        number_of_words += 1
    return number_of_words

print(f'There are {word_count()} words in this book.')