__author__ = 'trunghieu11'


def solve(start, end, t, d):
    if d == 0:
        return start * t
    answer = 0
    diff = abs(start - end)
    step = diff / d
    for i in range(step):
        answer += min(start, end) + i * d
    t -= step
    if diff % d != 0:
        answer += min(start, end) + diff % d
        t -= 1
    start = end = max(start, end)

    for i in range(t / 2):
        answer += 2 * (start + i * d)
    if t % 2 == 1:
        answer += start + t / 2 * d
    return answer

if __name__ == '__main__':
    start, end = map(int, raw_input().split(" "))
    t, d = map(int, raw_input().split(" "))
    print solve(start, end, t, d)