def count_words(path):
    count = 0
    with open(path) as f:
        file_cont = f.read()
        words = file_cont.split()
        for _ in words:
            count += 1
    return count

print(count_words("books/frank.txt"))

