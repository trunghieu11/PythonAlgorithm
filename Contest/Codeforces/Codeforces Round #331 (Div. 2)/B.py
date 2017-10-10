__author__ = 'trunghieu11'


def solve(n, A):
    answer = 0
    cur = 0
    for x in A:
        answer += abs(x - cur)
        cur = x
    return answer


if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split(" "))
    print solve(n, A)