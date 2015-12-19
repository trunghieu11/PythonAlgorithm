__author__ = 'trunghieu11'


def solve(n, A):
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    left[0] = 1
    for i in range(1, n):
        left[i] = min(left[i - 1] + 1, A[i])
    right[n - 1] = 1
    for i in range(n - 2, -1, -1):
        right[i] = min(right[i + 1] + 1, A[i])
    return max(min(left[i], right[i]) for i in range(n))


if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split(" "))
    print solve(n, A)