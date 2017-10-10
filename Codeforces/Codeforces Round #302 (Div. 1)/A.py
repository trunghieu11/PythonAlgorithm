__author__ = 'trunghieu11'

cache = {}


def calc(cur, n, remain, b, mod, bugs):
    key = (cur, remain, b)
    if key in cache:
        return cache.get(key)
    if cur == n:
        if remain <= 0 and b >= 0:
            return 1
        else:
            return 0
    answer = 0
    for i in range(0, remain + 1):
        if b - bugs[cur] * i >= 0:
            answer += calc(cur + 1, n, remain - i, b - bugs[cur] * i, mod, bugs)
            answer %= mod
        else:
            break
    cache[key] = answer
    return answer


def solve(n, m, b, mod, bugs):
    return calc(0, n, m, b, mod, bugs)


if __name__ == '__main__':
    n, m, b, mod = map(int, raw_input().split(" "))
    bugs = map(int, raw_input().split(" "))
    print solve(n, m, b, mod, bugs)
