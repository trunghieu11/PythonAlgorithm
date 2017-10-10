__author__ = 'trunghieu11'


def check(first, second):
    if first == second:
        return True
    if len(first) % 2 == 1:
        return False
    half = len(first) / 2
    return (check(first[:half], second[half:]) and check(first[half:], second[:half])) or (check(first[:half], second[:half]) and check(first[half:], second[half:]))


def solve(first, second):
    return "YES" if check(first, second) else "NO"


if __name__ == '__main__':
    first = raw_input()
    second = raw_input()
    print solve(first, second)