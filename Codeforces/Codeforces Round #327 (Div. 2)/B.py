__author__ = 'trunghieu11'

import string

def solve(n, k, s, change):
    val = {}
    for c in string.ascii_lowercase:
        val[c] = c
    for x in change:
        idx1 = val.values().index(x[0])
        idx2 = val.values().index(x[1])
        val[idx1], val[idx2] = x[1], x[0]
    return ''.join(str(val[x]) for x in s)


if __name__ == '__main__':
    n, k = map(int, raw_input().split(" "))
    s = raw_input()
    change = []
    for i in range(k):
        f, t = raw_input().split(" ")
        change.append([f, t])
    print solve(n, k, list(s), change)