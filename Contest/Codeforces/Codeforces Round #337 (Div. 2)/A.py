__author__ = 'trunghieu11'


def solve(n):
    if n % 2:
        return 0
    n /= 2
    return (n - 1) / 2


if __name__ == '__main__':
    n = int(raw_input())
    print solve(n)