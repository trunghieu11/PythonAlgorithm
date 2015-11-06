__author__ = 'trunghieu11'

def main():
    n, query = map(int, raw_input().split())
    A = list(map(int, raw_input().split()))
    sum = [0] * (n + 1)
    for i in range(1, n + 1):
        sum[i] = sum[i - 1] + A[i - 1]
    for q in range(query):
        fr, to = map(int, raw_input().split())
        if abs(sum[to] - sum[fr - 1]) % 2 == 0:
            print 'Even'
        else:
            print 'Odd'

if __name__ == '__main__':
    main()