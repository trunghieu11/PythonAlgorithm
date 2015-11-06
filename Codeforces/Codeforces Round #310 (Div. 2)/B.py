__author__ = 'trunghieu11'

def main():
    n = int(raw_input())
    A = list(map(int, raw_input().split()))
    for i in range(2 * n):
        for j in range(n):
            if j % 2 == 0:
                A[j] += 1
            else:
                A[j] -= 1
            A[j] = (A[j] + n) % n
        if A == range(0, n):
            print "Yes"
            return
    for i in range(2 * n):
        for j in range(n):
            if j % 2 == 0:
                A[j] -= 1
            else:
                A[j] += 1
            A[j] = (A[j] + n) % n
        if A == range(0, n):
            print "Yes"
            return
    print "No"

if __name__ == '__main__':
    main()