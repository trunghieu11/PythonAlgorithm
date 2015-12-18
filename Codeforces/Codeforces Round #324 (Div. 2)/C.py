import string

__author__ = 'trunghieu11'


def getDiff(a, b):
    for c in string.ascii_lowercase:
        if c != a and c != b:
            return c
    return a


def solve(n, k, a, b):
    same = sum(a[i] == b[i] for i in range(n))
    diff = sum(a[i] != b[i] for i in range(n))
    if diff / 2 + diff % 2 > k:
        return -1



if __name__ == '__main__':
    n, k = map(int, raw_input().split(" "))
    a = raw_input()
    b = raw_input()
    print solve(n, k, a, b)