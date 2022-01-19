#! python3
# ex10.py

def is_anagram(w1, w2):
    '''Two words are anagrams if they can be constructed from the same set of words.'''
    t1 = list(w1)
    t2 = list(w2)
    t1.sort()
    t2.sort()
    if t1 == t2:
        return True
    else:
        return False

def is_duplicate(t):
    for element in t:
        flag = 0
        for a in t:
            if a == element:
                flag += 1
        if flag > 1:
            return True
            
    else:
        return False
