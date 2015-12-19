__author__ = 'trunghieu11'


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def solve(n, lines):
    uniqueLine = set()
    for line in lines:
        g = gcd(gcd(line[0], line[1]), line[2])
        uniqueLine.add((line[0] / g, line[1] / g, line[2] / g))
    parallel = {}
    answer = 0
    for line in uniqueLine:
        key = (line[0], line[1])
        value = set()
        if key in parallel:
            value = parallel[key]
        value.add((line[2], line[1]))
        parallel[key] = value
        answer = max(answer, len(parallel[key]))
    return answer

if __name__ == '__main__':
    testCase = int(raw_input())
    for test in xrange(testCase):
        n = int(raw_input())
        lines = []
        for i in xrange(n):
            lines.append(tuple(map(int, raw_input().split(" "))))
        print solve(n, lines)