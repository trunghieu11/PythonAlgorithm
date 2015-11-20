__author__ = 'trunghieu11'


def calc(x, b):
    two = 2
    answer = 10**20
    two = x / b
    two -= two % 2
    if two > 0:
        answer = 1.0 * x / two
    return answer


def solve(a, b):
    answer = min(calc(a + b, b), calc(a - b, b))
    return -1 if answer == 10**20 else answer


if __name__ == '__main__':
    a, b = map(int, raw_input().split(" "))
    print solve(a, b)