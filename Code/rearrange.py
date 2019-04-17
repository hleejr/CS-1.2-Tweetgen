import random
import sys

def rearrange():
    words = sys.argv[1:]
    newOrder = []
    length = len(words)
    
    for i in range(length):
        index = random.randint(0, len(words) - 1)
        newOrder.append(words[index])
        words.pop(index)

    print (*newOrder)

if __name__ == '__main__':
    rearrange()
