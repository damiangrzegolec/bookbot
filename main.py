def count_letters(path):
    letters = {}

    with open(path) as f:
        file_cont = f.read()
        words = file_cont.split()
        for word in words:
            for l in word.lower():
                if l in letters:
                    letters[l] += 1
                else:
                    letters[l] = 1
    return letters


def print_words(path):
    with open(path) as f:
        file_cont = f.read()
        words = file_cont.split()
        print(words)


def count_words(path):
    count = 0
    with open(path) as f:
        file_cont = f.read()
        words = file_cont.split()
        for _ in words:
            count += 1
    return count


def report(path):
    letters = count_letters(path)
    report = {}
    for letter, num in letters.items():
        if letter.isalpha():
            report[letter] = num
    item_list = list(report.items())
    word_count = count_words(path)
    item_list.sort()

    print(f"Begin report of {path}")
    print(f"{word_count} words found in the document")
    print(f"\n\n")
    for item in item_list:
        print(f"The {item[0]} character was found {item[1]} times")
    print(f"\n\n")
    print(f"End report of {path}")



report("books/frank.txt")

