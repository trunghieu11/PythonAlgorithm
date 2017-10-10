__author__ = 'trunghieu11'


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def solve(a, b, c, d):
    answer = 0
    for i in xrange(1, a + 1):
        for j in xrange(1, b + 1):
            for k in xrange(1, c + 1):
                for l in xrange(1, d + 1):
                    if abs(i - j) % 3 == 0 and (j + k) % 5 == 0 and (i * k) % 4 == 0 and gcd(i, l) == 1:
                        answer += 1
    return answer


if __name__ == '__main__':
    a, b, c, d = map(int, raw_input().split(" "))
    print solve(a, b, c, d)