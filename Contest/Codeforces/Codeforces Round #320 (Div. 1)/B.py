__author__ = 'trunghieu11'


def solve(n, k, x, A):
    if n == 1:
        return A[0] * x**k

    prefix = [0 for i in range(n)]
    suffix = [0 for i in range(n)]
    prefix[0] = A[0]
    suffix[n - 1] = A[n - 1]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] | A[i]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] | A[i]
    answer = max((A[0] * x**k) | suffix[1], (A[n - 1] * x**k) | prefix[n - 2])
    for i in range(1, n - 1):
        answer = max(answer, prefix[i - 1] | (A[i] * x**k) | suffix[i + 1])
    return answer


if __name__ == '__main__':
    n, k, x = map(int, raw_input().split(" "))
    A = map(int, raw_input().split(" "))
    print solve(n, k, x, A)