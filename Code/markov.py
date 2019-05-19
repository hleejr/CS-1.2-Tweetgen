import random
from dictogram import Dictogram
from sample import sample
from corpus import words

def higher_markov(seq):
    # tracks the pairs that start and end sentences
    model = Dictogram(['START', 'END'])
    model['START'] = {}
    model['END'] = {}
 
    for index in range(len(seq)-2):
        # create the pair to store in the model
        pair = ( seq[index], seq[index + 1] )
        next_word = seq[index + 2]
        model[pair] = {}
        # check to see if pair belongs as START or STOP token
        if pair[0].islower() is False and pair[0].endswith('.') is False:
            # check if pair is already stored as a token, if so increase frequency
            if pair in model['START']:
                model['START'][pair] += 1
            else:
                model['START'][pair] = 1
        if pair[1].islower() is True and pair[1].endswith('.') is True:
            # check if pair is already stored as a token, if so increase frequency
            if pair in model['END']:
                model['END'][pair] += 1
            else: 
                model['END'][pair] = 1
        # # store the word that follows the pair and it's frequency
        if next_word in model[pair]:
            model[pair][next_word] += 1
        else:
            model[pair][next_word] = 1

    return model

def markov_sentence(seq):
    markov = higher_markov(seq)
    sentence = []
    start = random.choice(list(markov['START'].keys()))
    sentence.extend(start)
    index = 1
    current = start

    while current not in markov['END']:

        next_word = sample(markov[current])
        sentence.insert(index, next_word)
        current = (current[1] , next_word)
        index += 1
    
    return " ".join(sentence[:-1])

if __name__ == '__main__':
    # print(higher_markov(words))
    print(markov_sentence(words))

