import dictionary as rans
import random

def make_model():
    lines = rans.lines
    model = {'START-':[], 'END-': []}
    start = model['START-']
    end = model['END-']
    new = {}

    for line in lines:
        words = line.split(' ')
        first = line.split(' ')[0].lower().replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace("…","")
        last = line.split(' ')[-1].lower().replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace("…","")
        start.append(first)
        end.append(last)
        for word in words:
            word = word.lower().replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace("…","")
            model[word] = []
    for word in start:
        for wrd in start:
            if wrd == word:
                start.remove(wrd)
    for word in end:
        for wrd in end:
            if word == wrd:
                end.remove(wrd)

    for key,value in model.items():
        if key not in new.items():
            new[key] = value
    
    return new

def check_pairs():
    pairs = make_model()
    lines = rans.lines
    arr = []
    index = 0

    for line in lines:
        line = line.split(' ')
        arr.append(line)

    while index < len(arr):
        line = arr[index]
        for i in range(len(line)):
            add = line[i].lower().replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace("…","")
            target = line[i - 1].lower().replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace("…","")
            if target in pairs:
                pairs[target].append(add)
        index = index + 1
    return pairs

def make_sentence():
    markov = check_pairs()
    start = markov['START-']
    # end = markov['END-']
    sentence = []
    sentence.insert(0, random.choice(start))
    # sentence.insert(1, random.choice(end))
    length = random.randint(10,20)
    index = 1

    while len(sentence) < length:
        sentence.insert(index, random.choice(markov[sentence[index-1]]))
        index = index + 1
    
    return " ".join(sentence)

if __name__ == '__main__':
    make_model()
    check_pairs()
    print(check_pairs())