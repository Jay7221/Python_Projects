#! python3
# ex12.py

def reverse_dict(d):
    reverse_d = dict()
    for key in d:
        reverse_d.setdefault(d[key], [])
        reverse_d[d[key]].append(key)

    return reverse_d




    
def most_frequent(text):
    '''Takes a text and prints letters in decreasing order of frequency.'''
    word_list = text.split()
    letter_dict = dict()
    for word in word_list:
        for letter in word:
            letter_dict.setdefault(letter, 0)
            letter_dict[letter] += 1
    letter_freq_dict = reverse_dict(letter_dict)
    letter_freq_list = []
    for i in letter_freq_dict:
        letter_freq_list.append(i)
    letter_freq_list.sort(reverse = True)
    for freq in letter_freq_list:
        for letter in letter_freq_dict[freq]:
            print(letter, freq)


def anagrams(text):
    '''Returns a list anagrams in text.'''
    word_list = text.split()
    word_dict = dict()
    for word in word_list:
        word_dict[word] = word_tuple(word)
    anagram_dict = reverse_dict(word_dict)
    return anagram_dict

def order_anagrams(text):
    anagram_dict = anagrams(text)
    ana_len_dict = dict()
    for ana_list in anagram_dict.values():
        ana_len_dict[tuple(ana_list)] = len(ana_list)
    ana_len_dict = reverse_dict(ana_len_dict)
    len_list = list()
    for i in ana_len_dict:
        len_list.append(i)
    len_list.sort(reverse = True)
    for a in len_list:
        for b in ana_len_dict[a]:
            print(list(b))
def word_tuple(word):
    '''Returns a tuple of letters that form the word.'''
    return tuple(sorted(tuple(word)))

def is_anagram(w1, w2):
    if len(w1) != len(w2):
        return False
    if word_tuple(w1) == word_tuple(w2):
        return True
    else:
        return False
def is_metathesis(w1, w2):
    if not is_anagram(w1, w2):
        return False
    flag = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            flag += 1
    if flag == 2:
        return True
    else:
        return False
