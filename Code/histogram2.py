def count_words(seq):
    hist = {}

    for word in seq:
        if word in hist:
            hist[word] += 1 
        else:
            hist[word] = 1

    return hist