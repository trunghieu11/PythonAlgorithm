__author__ = 'trunghieu11'

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def solve(n):
    answer = 0
    for i in range(1, n + 1):
        answer += n / gcd(n, i)
    return answer

if __name__ == '__main__':
    testCase = int(raw_input())
    for test in range(testCase):
        n = int(raw_input())
        print solve(n)