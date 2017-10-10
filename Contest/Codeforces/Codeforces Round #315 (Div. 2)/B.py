__author__ = 'trunghieu11'

def main():
    n = int(raw_input())
    A = map(int, raw_input().split())
    s = set()
    idx = 1
    for i in range(n):
        if A[i] > n or A[i] in s:
            while idx in s:
                idx += 1
            A[i] = idx
        s.add(A[i])
    print ' '.join(map(str, A))

if __name__ == '__main__':
    main()