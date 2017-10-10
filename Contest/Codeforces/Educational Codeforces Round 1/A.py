__author__ = 'trunghieu11'


def solve(n):
    total = n * (n + 1) / 2
    twoMinus = 1
    while twoMinus <= n:
        twoMinus *= 2
    return total - 2 * (twoMinus - 1)


if __name__ == '__main__':
    testCase = int(raw_input())
    for test in range(testCase):
        n = int(raw_input())
        print solve(n)