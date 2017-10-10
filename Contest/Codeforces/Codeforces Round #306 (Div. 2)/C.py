__author__ = 'trunghieu11'

def main():
    s = raw_input()
    A = list(map(int, list(s)))
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if i == j == k and A[i] % 8 == 0:
                    print "YES"
                    print A[i]
                    return
                elif (i == j or j == k) and (A[i] * 10 + A[k]) % 8 == 0:
                    print "YES"
                    print A[i] * 10 + A[k]
                    return
                elif i != j != k and (A[i] * 100 + A[j] * 10 + A[k]) % 8 == 0:
                    print "YES"
                    print A[i] * 100 + A[j] * 10 + A[k]
                    return
    print "NO"

if __name__ == '__main__':
    main()