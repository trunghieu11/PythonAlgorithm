__author__ = 'trunghieu11'

import string

def solve(n, k, s, changes):
    index = {}
    for c in string.ascii_lowercase:
        index[c] = c
    for x in changes:
        for c in string.ascii_lowercase:
            if index[c] == x[0]:
                index[c] = x[1]
            elif index[c] == x[1]:
                index[c] = x[0]
    answer = ""
    for c in s:
        answer += index[c]
    return answer



if __name__ == '__main__':
    n, k = map(int, raw_input().split(" "))
    s = raw_input()
    changes = []
    for i in range(k):
        changes.append(raw_input().split(" "))
    print solve(n, k, s, changes)