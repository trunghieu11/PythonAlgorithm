__author__ = 'trunghieu11'


def solve(d):
    return min(d[0] + d[1] + d[2], 2 * (d[0] + d[1]), 2 * (d[0] + d[2]), 2 * (d[1] + d[2]))


if __name__ == '__main__':
    d = map(int, raw_input().split(" "))
    print solve(d)