__author__ = 'trunghieu11'

import sys

def main():
    n, island = map(int, raw_input().split())
    answer = ['S'] * n ** 2
    for i in range(0, n ** 2, 2):
        if island > 0:
            answer[i + ((n - 1) % 2) * (i / n) % 2] = 'L'
            island -= 1
    if island > 0:
        print "NO"
    else:
        sys.stdout.write("YES")
        for i in range(n ** 2):
            if i % n == 0:
                print ""
            sys.stdout.write(answer[i])

if __name__ == '__main__':
    main()