__author__ = 'trunghieu11'


def solve(n):
    return (n - 3) * 3 + (n - 4) * (n - 3) + 1


if __name__ == '__main__':
    n = int(raw_input())
    print solve(n)