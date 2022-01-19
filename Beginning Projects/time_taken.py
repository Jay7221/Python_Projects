#! python3
# time_taken.py

import os

def ettime():
    '''See how much user and system time this process has used so far and return the sum.'''
    user, sys, chuser, chsys, real = os.times()
    return user + sys

def time_cons(f, n):
    '''Returns the time taken by the function f, given the input n.'''
    a = ettime()
    f(n)
    b = ettime()
    return b - a
