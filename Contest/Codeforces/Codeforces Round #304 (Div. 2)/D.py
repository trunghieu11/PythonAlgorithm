__author__ = 'trunghieu11'

from sys import stdin, stdout

def main():
    MAXN = 5000001
    divisor = [0] * MAXN
    totalDiv = [0] * MAXN
    sum = [0] * MAXN

    for i in range(2, MAXN):
        if divisor[i] == 0:
            divisor[i] = i
            for j in range(i * i, MAXN, i):
                divisor[j] = i

        val = i
        while (val > 1):
            if totalDiv[val] > 0:
                totalDiv[i] += totalDiv[val]
                break
            else:
                totalDiv[i] += 1
                val //= divisor[val]
        sum[i] = sum[i - 1] + totalDiv[i]

    read = iter(map(int, stdin.read().split()))
    test = next(read)
    answer = []
    for t in range(test):
        a, b = next(read), next(read)
        answer.append(str(sum[a] - sum[b]))
    stdout.write("\n".join(answer))
    stdout.write("\n")

if __name__ == "__main__":
    main()