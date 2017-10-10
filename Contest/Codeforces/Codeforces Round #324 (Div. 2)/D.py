__author__ = 'trunghieu11'


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in xrange(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

def solve(n):
    x = n
    while not isPrime(x):
        x -= 1
    if x == n:
        return "1\n" + str(x)
    diff = n - x
    if isPrime(diff):
        return "2\n" + str(diff) + " " + str(x)
    for i in xrange(2, diff):
        if isPrime(i) and isPrime(diff - i):
            return "3\n" + str(x) + " " + str(i) + " " + str(diff - i)
    return "0"

if __name__ == '__main__':
    n = int(raw_input())
    print solve(n)