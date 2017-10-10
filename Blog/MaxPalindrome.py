__author__ = 'trunghieu11'


def maxPalindrome(A):
    n = len(A)
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = 1

    answer = 0
    for l in range(2, n + 1):
        for i in range(0, n + 1 - l):
            j = i + l - 1
            if A[i] == A[j]:
                dp[i][j] = max(dp[i + 1][j - 1] + 2, dp[i][j])
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], dp[i][j])
            answer = max(answer, dp[i][j])

    return answer


if __name__ == '__main__':
    A = [1,2,4,4,1]
    print maxPalindrome(A)