import sys
import random
import histogram2 as hi

def probability(seq):
    # takes in a histogram of words and frequencies and then creates another histogram of with the word and its probability in comparison to total word tokens
    # this total will become the total number of word occurances within the given sequence
    total = sum(seq.values())
    prob = {}
    for word, count in seq.items():
        weight = count/total
        prob[word] = weight
    return prob

def sample(seq):
    # randomly generates a number between 0 and 1 and selects a word from the sequence with matching probability
    total = sum(seq.values()) 
    rand = random.random() # number to beat to be selected
    accumulator = 0 # total accumulated value of weighted words
    
    for word, count in seq.items():
        accumulator += count/total 
        if accumulator > rand: 
            return word
           

def test(seq):
    # test if word occurances matches with the probabilty of word
    counter = 10000
    test_arr = []

    while counter > 0:
        rand = sample(seq)
        test_arr.append(rand)
        counter -= 1
    
    test_hist = hi.count_words(test_arr)
    return test_hist



if __name__ == '__main__':
    data = ["one",'fish','two','fish','red','fish','blue', 'fish']
    hist = hi.count_words(data)
    # hist = hi.count_words(hi.words)
    print(probability(hist))
    print(test(hist))

