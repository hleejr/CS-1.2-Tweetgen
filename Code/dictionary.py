import sys
import random
with open("quotes.txt") as word_file:

    dictionary = list(set(word.strip().replace("“", "").replace("”", "").replace('"', "") for word in word_file))
    lines = [line.rstrip('\n').strip(' ') for line in dictionary]
    words = []
    
    for line in lines:
        line = str(line)
        words_in_line = line.split()

        for word in words_in_line:
            words.append(word) 

length = input('Enter the number of words you want in the sentence: ')

def random_sentence():

    sentence = []

    while len(sentence) < int(length):

        index = random.randint(0, len(dictionary) - 1)
        sentence.append(words[index])

    return " ".join(sentence)

if __name__ == '__main__':
    
    print(random_sentence())
    