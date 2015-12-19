__author__ = 'trunghieu11'


def solve(n, x1, x2):
    k = min(n, x1, x2)
    while True:
        left = 0
        right = k
        while right - left > 1:
            mid = (right + left) / 2
            if k * (k + 1) / 2 - mid * (mid + 1) / 2 > min(x1, x2):
                left = mid
            else:
                right = mid
        chooseLeft = k * (k + 1) / 2 - left * (left + 1) / 2
        chooseRight = k * (k + 1) / 2 - right * (right + 1) / 2
        if chooseLeft > 0 and chooseLeft <= min(x1, x2):
            x1 -= chooseLeft
            x2 -= chooseLeft
            k = min(x1, x2, left)
        elif chooseRight > 0 and chooseRight <= min(x1, x2):
            x1 -= chooseRight
            x2 -= chooseRight
            k = min(x1, x2, right)
        else:
            break
    return x1 + x2


if __name__ == '__main__':
    testCase = int(raw_input())
    for test in xrange(testCase):
        x1, x2, n = map(int, raw_input().split(" "))
        print solve(n, x1, x2)