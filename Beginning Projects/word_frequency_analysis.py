#! python3
# word_frequency_analysis.py

import string, random
from ex12 import reverse_dict
from matplotlib import pyplot

def word_freq(text):
    word_list = text.split()
    word_dict = dict()
    for word in word_list:
        word.strip(string.punctuation + string.whitespace)
        word_dict.setdefault(word.lower(), 0)
        word_dict[word.lower()] += 1
    return word_dict


def analyze(file):
    with open(file) as file_obj:
        file_data = file_obj.read()
        word_data = word_freq(file_data)
        most_common(word_data)
        return word_data
    
def total_words(word_dict):
    w_sum = 0
    for freq in word_dict.values():
        w_sum += freq
    return w_sum
    
        
def most_common(word_dict, num = 0):
    word_tuple = tuple()
    for word, freq in word_dict.items():
        word_tuple = word_tuple + ((freq, word),)
    word_tuple = sorted(word_tuple, reverse = True)
    return word_tuple

def cum_search(word_dict, n):
    word_dict = reverse_dict(word_dict)
    k = word_dict[int(len(word_dict)/2)]
    
    if k == n:
        return word_dict[n]
    if k > n:
        return cum_search(word_dict[:k], n)
    if k < n:
        return cum_search(word_dict[k:], n)
    

def random_word(text):
    word_dict = word_freq(text)
    w_sum = 0
    for key in word_dict:
        w_sum += word_dict[key]
        word_dict[key] = w_sum
    rand = random.randint(1, w_sum)
    a = cum_search(word_dict, rand)
    return a

def make_graph(file):
    data = dict(most_common(analyze(file)))
    graph = pyplot.plot(range(1,len(data) + 1), list(data.keys()))
    pyplot.xlabel('Word Rank')
    pyplot.ylabel('Number of Words')
    pyplot.show()

def verify_zerf(file):
    data = dict(most_common(analyze(file)))
    graph = pyplot.plot(range(1,len(data) + 1), list(data.keys()))
    pyplot.xlabel('Word Rank')
    pyplot.ylabel('Number of Words')
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.show()
    
    

print(__name__)
