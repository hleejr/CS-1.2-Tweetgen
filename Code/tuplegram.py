with open("quotes.txt") as word_file:
    quotes = set(word.strip().lower() for word in word_file)

def count_words(seq):
    hist = []
    lines = [line.rstrip('\n').strip(' ') for line in open('quotes.txt')]
    words = []

    for line in lines:
        line = str(line)
        words_in_line = line.split()

        for word in words_in_line:
            words.append(word) 

    for i in words:
        word = i
        count = 1
        for j in words:
            if i == j:
                words.remove(j)
                count += 1
        hist.append((word, count))

    return hist

if __name__ == '__main__':
    count_words(quotes)