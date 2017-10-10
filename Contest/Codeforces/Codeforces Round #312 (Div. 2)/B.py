__author__ = 'trunghieu11'


def solve(n, A):
    start = {}
    end = {}
    total = {}
    for i in range(n):
        if A[i] not in start:
            start[A[i]] = i
        end[A[i]] = i
        total[A[i]] = total[A[i]] + 1 if A[i] in total else 1
    maxVal = max(total.values())

    answer = -1
    for x in A:
        if total[x] >= maxVal and (answer == -1 or end[x] - start[x] + 1 < end[answer] - start[answer] + 1):
            answer = x
    return str(start[answer] + 1) + " " + str(end[answer] + 1)

if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split(" "))
    print solve(n, A)