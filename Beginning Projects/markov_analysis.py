#! python3
# markov_analysis.py

import string
import random

def markov(file, prefix_length = 2):
    with open(file) as file_obj:
        file_data = file_obj.read()
        file_data.strip(string.punctuation + string.whitespace + '\'' + '"')
        word_list = file_data.split()
        markov_dict = dict()
        prefix_list = list()
        for i in range(len(word_list) - prefix_length):
            prefix = ' '.join(word_list[i:i + prefix_length])
            prefix_list.append(prefix)
            markov_dict.setdefault(prefix, list())
            markov_dict[prefix].append(word_list[i + prefix_length])
        return markov_dict, prefix_list

def random_line(file, length = 10):
    markov_dict, prefix_list = markov(file)
    line = ''
    while len(line) < length:
        line = ''
        rand = random.randint(0,len(prefix_list))
        prefix = prefix_list[rand]
        print(prefix)
        line += prefix
        suffix_list = markov_dict[prefix]
        for suffix in suffix_list:
            for prefixes in markov_dict:
                if suffix == prefixes.split()[0]:
                    prefix = prefixes
    return line
    
    
    
    
