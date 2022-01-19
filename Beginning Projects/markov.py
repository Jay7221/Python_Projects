#! python3
# markov.py

import sys
import string
import random

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    '''Reads a file and performs Markov analysis.'''
    with open(filename) as file:
        skip_gutenberg_header(file)
        for line in file:
            if line.startswith('*** END OF'):
                break

            for word in line:
                process_word(word, order)

def skip_gutenberh_header(file):
    '''Reads file until it meets line that is header.'''
    for line in file:
        if line.startswith('*** START OF'):
            break

def process_word(word, order = 2):
    '''Processes each word.'''
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)

def shift(prefix, word):
    '''Returns a new tuple by removing the first word and adding word to the end.'''
    return prefix[1:] + (word,)

def random_text(n = 100):
    '''Generates random text of length n.'''
    start = random.choice(list(suffix_map.keys()))

    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            random_text(n - i)
            return
        #Choose random suffix
        word = random.choice(suffixes)
        print(word, end = ' ')
        start = shift(start, word)

