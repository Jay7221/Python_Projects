#! python3
# Problem_solving_Algo_Ch1.py

import timeit
from timeit import Timer

def anagram_solution1(s1, s2):
    '''Checks if s1 and s2 are anagrams.'''
    a_list = list(s2)
    pos1 = 0
    still_ok = True
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            a_list[pos2] = None
        else:
            still_ok = False

        pos1 += 1
    return still_ok

def anagram_sol2(s1, s2):
    '''Checks if s1 and s2 are anagrams.'''
    s1_list = list(s1)
    s2_list = list(s2)
    found = list()
    print(s1_list, s2_list)
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                s1_list[i] = 0
                s2_list[j] = 0
    try:
        return sum(s1_list) == 0 and sum(s2_list) == 0
    except TypeError:
        return False

def anagram_sol3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    still_ok = True
    j = 0
    while j < 26 and still_ok :
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False
    return still_ok

def test1():
    l = []
    for i in range(1000):
        l += [i]

t1 = Timer('test1()', 'from __main__ import test1')
print('time taken:', t1.timeit(number = 1000), 'milliseconds')
