__author__ = 'trunghieu11'

MOD = 10**9 + 7


def dfs(n, total, d, haveGreater, dp):
    if total == 0:
        return haveGreater
    if dp[total][haveGreater] >= 0:
        return dp[total][haveGreater]
    answer = 0
    for i in range(n):
        if total >= i + 1:
            answer += dfs(n, total - i - 1, d, haveGreater or (i + 1 >= d), dp)
            answer %= MOD
    dp[total][haveGreater] = answer
    return answer


def solve(n, total, d):
    dp = [[-1, -1] for i in range(total + 1)]
    return dfs(n, total, d, False, dp) % MOD


if __name__ == '__main__':
    total, n, d = map(int, raw_input().split(" "))
    print solve(n, total, d)