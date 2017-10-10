__author__ = 'trunghieu11'

MOD = 10**9 + 7
cache = {}

def calc(top, idx, visited, n, s):
    key = (idx, top)
    if key in cache:
        return cache.get(key)
    if idx >= n - 1:
        return 1
    answer = 0
    if s[idx] == 'G':
        for i in range(top + 1, n):
            if not visited[i]:
                visited[i] = True
                answer += calc(i, idx + 1, visited, n, s)
                if answer > MOD:
                    answer -= MOD
                visited[i] = False
    else:
        for i in range(top - 1, -1, -1):
            if not visited[i]:
                visited[i] = True
                answer += calc(i, idx + 1, visited, n, s)
                if answer > MOD:
                    answer -= MOD
                visited[i] = False
    cache[key] = answer
    return answer


def solve(n, MOD, s):
    visited = [False for i in range(n)]
    
    answer = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer += calc(i, 0, visited, n, s)
            if answer > MOD:
                answer -= MOD
            visited[i] = False
    return answer


if __name__ == '__main__':
    n, MOD = map(int, raw_input().split(" "))
    s = raw_input()
    print solve(n, MOD, s)