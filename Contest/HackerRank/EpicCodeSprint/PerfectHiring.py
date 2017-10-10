__author__ = 'trunghieu11'

def main():
    n, p, x = map(int, raw_input().split())
    A = list(map(int, raw_input().split()))
    maxIdx = -1
    maxVal = -10**20
    for i in range(n):
        if maxIdx == -1 or A[i] * p > maxVal:
            maxIdx = i
            maxVal = A[i] * p
        p -= x
    print maxIdx + 1

if __name__ == '__main__':
    main()