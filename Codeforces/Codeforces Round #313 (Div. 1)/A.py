__author__ = 'trunghieu11'


def solve(edge):
    bigTriangle = edge[0] + edge[1] + edge[2]
    return bigTriangle**2 - edge[0]**2 - edge[2]**2 - edge[4]**2


if __name__ == '__main__':
    edge = list(map(int, raw_input().split()))
    print solve(edge)