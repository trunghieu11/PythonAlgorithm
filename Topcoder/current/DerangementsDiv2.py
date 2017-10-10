import math

MOD = 1000000007

def generate_binomial_coefficients(n):
    C = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, n + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C

def factorial(n):
    answer = 1
    for i in range(n):
        answer *= (i + 1)
    return answer

class DerangementsDiv2:
    def count(self, n, m):
        answer = factorial(n + m)

        C = generate_binomial_coefficients(51)

        total = [0 for i in range(m + 1)]
        total[m] = factorial(n)
        for i in range(m - 1, 0, -1):
            total[i] = C[m][i] * factorial(n + m - i)
            for j in range(i + 1, m + 1):
                total[i] -= C[j][i] * total[j]

        # print total

        return (answer - sum(total)) % MOD

class Derangements1:
    def count(self, n, m):
        dp = [[0 for i in range(200)] for j in range(200)]

        for i in range(1, 200):
            dp[i][1] = factorial(i) - factorial(i - 1)

        for i in range(2, 100):
            for j in range(2, 100):
                dp[i][j] = dp[i + 1][j - 1] - dp[i][j - 1]

        return dp[n + 1][m]

def count2(arr, i):
    if i == -1:
        return 1

    sum = 0
    for k in range(len(arr)):
        if k not in arr and k != i:
            arr[i] = k
            sum += count2(arr[:], i - 1) % MOD

    return sum

class Derangements:
    def count(self, n, m):
        arr = [-1 for i in range(m+n)]

        s1 = count2(arr, m-1)
        return s1 * math.factorial(n) % MOD

if __name__ == '__main__':
    # for n in range(1, 10):
    #     for m in range(1, 10):
    #         solverHieu = DerangementsDiv2()
    #         solverTriet = Derangements()
    #         if solverHieu.count(n, m) != solverTriet.count(n, m):
    #             print n, m, solverHieu.count(n, m), solverTriet.count(n, m)

    solve = Derangements1()
    print solve.count(3, 5)

    # C = generate_binomial_coefficients(10)
    # print C[8][5] * 44
