__author__ = 'trunghieu11'


def solve(n):
    return (3**(3 * n) - 7**n) % 1000000007


if __name__ == '__main__':
    n = int(raw_input())
    print solve(n)