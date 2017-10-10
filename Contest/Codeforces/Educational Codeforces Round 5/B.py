__author__ = 'trunghieu11'


def solve(n, m, table):
    return max(min(x) for x in table)


if __name__ == '__main__':
    n, m = map(int, raw_input().split(" "))
    table = []
    for i in range(n):
        table.append(map(int, raw_input().split(" ")))
    print solve(n, m, table)