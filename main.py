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
    
    print(letters)

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

print(count_letters("books/frank.txt"))

