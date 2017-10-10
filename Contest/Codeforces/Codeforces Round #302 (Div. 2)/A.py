__author__ = 'trunghieu11'

import sys

def main():
    n = int(raw_input())
    s = raw_input()
    if len(set(s)) < n:
        print "NO"
        return

    sys.stdout.write("YES")
    visited = []
    for c in s:
        if c not in visited and n > 0:
            visited.append(c)
            n -= 1
            print ""
        sys.stdout.write(c)

if __name__ == '__main__':
    main()