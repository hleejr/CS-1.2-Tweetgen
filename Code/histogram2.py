with open("quotes.txt") as word_file:
    quotes = set(word.strip().lower() for word in word_file)

lines = [line.rstrip('\n').strip(' ') for line in open('quotes.txt')]
words = []

for line in lines:
    line = str(line)
    words_in_line = line.split()
    for word in words_in_line:
        words.append(word) 

def count_words(seq):
    hist = {}

    for word in seq:
        if word in hist:
            hist[word] += 1 
        else:
            hist[word] = 1

    return hist

if __name__ == '__main__':
    print(count_words(words))