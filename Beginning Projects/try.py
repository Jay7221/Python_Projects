tree = [0] * 8
def sum_k(k):
    s = 0
    while k >= 1:
        s += tree[k - 1]
        k -= k & -k
    return s

def add(k, x):
    while(k <= len(tree)):
        tree[k - 1] += x
        k += k & -k
