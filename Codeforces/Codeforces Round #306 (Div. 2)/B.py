__author__ = 'trunghieu11'

import itertools

def main():
    n, l, r, x = map(int, raw_input().split())
    c = list(map(int, raw_input().split()))

    for i in range(1, len(c) + 1):
        for j in itertools.combinations(c, i):
            print j

if __name__ == '__main__':
    main()