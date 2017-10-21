class StripePainter:
    def minStrokes(self, stripes):
        n = len(stripes)
        dp = [[50 for i in range(n)] for j in range(n)]

        # same idx result will be 1
        for i in range(n):
            dp[i][i] = 1

        # go from small length to large
        for l in range(1, n + 1):
            for i in range(n - l):
                # if equal, new result will be same as old result
                # examples: AB is 2, ABA is 2 too
                if stripes[i] == stripes[i + l]:
                    dp[i][i + l] = min(dp[i + 1][i + l], dp[i][i + l - 1])
                else:
                    # if not equal, find answer by using calculated result
                    # by split to two small string and find result
                    for j in range(i, i + l):
                        dp[i][i + l] = min(dp[i][i + l], dp[i][j] + dp[j + 1][i + l])

        return dp[0][n - 1]


if __name__ == '__main__':
    painter = StripePainter()
    print(painter.minStrokes("BECBBDDEEBABDCADEAAEABCACBDBEECDEDEACACCBEDABEDADD"))
