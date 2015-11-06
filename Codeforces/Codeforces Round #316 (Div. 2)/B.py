__author__ = 'trunghieu11'

def main():
    n, k = map(int, raw_input().split())
    if n / 2 >= k:
        print min(k + 1, n)
    else:
        print max(1, k - 1)

if __name__ == '__main__':
    main()