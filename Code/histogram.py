
def count_words(seq):
    hist = []

    for i in seq:
        word = i
        count = 0
        for j in seq:
            if i == j:
                seq.remove(j)
                count += 1
        hist.append([word, count])

    return hist

# if __name__ == '__main__':
#     count_words(quotes)