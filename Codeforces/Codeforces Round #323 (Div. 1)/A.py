__author__ = 'trunghieu11'


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def solve(n, A):
    total = {}
    for x in A:
        total[x] = (total[x] if x in total else 0) + 1
    answer = []
    for i in range(n):
        maxVal = max(list(total.keys()))
        total[maxVal] -= 1
        if total[maxVal] <= 0:
            total.pop(maxVal)
        for x in answer:
            val = gcd(maxVal, x)
            total[val] -= 2
            if total[val] <= 0:
                total.pop(val)
        answer.append(maxVal)
    return ' '.join(str(x) for x in answer)


if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split(" "))
    print solve(n, A)