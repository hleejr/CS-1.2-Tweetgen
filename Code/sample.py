import sys
import random
import histogram2 as hi
import listogram as li

hist = hi.count_words(hi.quotes)

def probability(seq):
    # takes in a histogram of words and frequencies and then creates another histogram of with the word and its probability in comparison to total word tokens
    # this total will become the total number of word occurances within the given sequence
    total = 0
    prob = []
    for val in seq:
        count = val[1]
        total += count
        weight = count/total
        add = [val[0], weight]
        prob.append(add)
    return prob

def sample(seq):
    # randomly generates a number between 0 and 1 and selects a word from the sequence with matching probability
    total = sum(hist.values()) 
    rand = random.random() # number to beat to be selected
    accumulator = 0 # total accumulated value of weighted words
    
    for word, count in hist.items():
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
    
    arr = li.Listogram(" ".join(test_arr))
    return arr



if __name__ == '__main__':
    rand = sample(hist)
    # test = test(hist)
    print(rand)
