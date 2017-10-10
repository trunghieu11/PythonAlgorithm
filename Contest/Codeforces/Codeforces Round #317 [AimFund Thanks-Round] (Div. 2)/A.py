__author__ = 'trunghieu11'

def main():
    lenA, lenB = map(int, raw_input().split())
    k, m = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())

    maxA = A[k - 1]
    i = 0
    while i < lenB and B[i] <= maxA:
        i += 1
    print "YES" if lenB - i >= m else "NO"

if __name__ == '__main__':
    main()