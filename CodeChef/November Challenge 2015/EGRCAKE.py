__author__ = 'trunghieu11'

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def solve(n, m):
    if n == 1:
        return 'Yes'
    if m == 0:
        return 'No 1'
    g = gcd(n, m)
    if g == 1:
        return 'Yes'
    else:
        return 'No ' + str(n / g)

if __name__ == '__main__':
    testCase = int(raw_input())
    for test in range(testCase):
        n, m = map(int, raw_input().split())
        print solve(n, m)