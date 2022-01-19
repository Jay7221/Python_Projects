# python3
# exercises6.py

def is_power(a, b):
    if a == b:
        return True
    if a % b == 0 and  is_power(a/b, b):
        return True
    else:
        return False

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)
