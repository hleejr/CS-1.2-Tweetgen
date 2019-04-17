from pprint import pprint

def get_words(filename):
    '''Open file and return list of all words'''
    all_words_list = []
    with open(filename) as f:
        for line in f:
            words_list = line.split()
            for word in words_list:
                all_words_list.append(word)
    return all_words_list

def count_words(arr):
    '''Count occurances of word in given list and return that data structure'''
    word_counts = {}
    for word in arr:
        if word in word_counts:
            word_counts[word] += 1 
        else:
            word_counts[word] = 1

    return word_counts

def print_table(word_counts):
    '''Print out table of words and respective count'''
    print('Word | Count')
    print('------------')
    for word in word_counts:
        count = word_counts[word]
        print(f'{word} | {count}')
    total_count = sum(word_counts.values())
    print(f'Total: {total_count}')
    for word, count in word_counts.items():
        print(f'{word} | {count}')
word_list = get_words('animals.txt')
counts = count_words(word_list)
print_table(counts)
# pprint(count_words(word_list))

