__author__ = 'trunghieu11'


def solve(l, r, k):
    cur = 1
    answer = []
    while cur <= r:
        if l <= cur <= r:
            answer.append(cur)
        cur *= k
    if len(answer) == 0:
        return -1
    return ' '.join(str(x) for x in answer)


if __name__ == '__main__':
    l, r, k = map(int, raw_input().split(" "))
    print solve(l, r, k)