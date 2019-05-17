import re
with open("quotes.txt") as word_file:
    quotes = set(word.strip().lower() for word in word_file)

lines = [line.rstrip('\n').strip(' ') for line in open('quotes.txt')]
words = []

for line in lines:
    line = str(line)
    words_in_line = line.split()
    for word in words_in_line:
        word = ''.join(c for c in word if c not in '["-_*:,;]')
        words.append(word) 
