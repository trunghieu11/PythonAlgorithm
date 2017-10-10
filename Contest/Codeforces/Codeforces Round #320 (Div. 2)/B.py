__author__ = 'trunghieu11'


def solve(n, points):
    answer = [-1 for i in range(2 * n)]
    for k in range(n):
        maxIdx = [-1, -1]
        for j in range(2 * n - 1):
            for i in range(j, 2 * n - 1):
                if answer[i + 1] == -1 and answer[j] == -1 and (maxIdx == [-1, -1] or points[i][j] > points[maxIdx[0]][maxIdx[1]]):
                    maxIdx = [i, j]
        answer[maxIdx[0] + 1] = maxIdx[1] + 1
        answer[maxIdx[1]] = maxIdx[0] + 2
    return ' '.join(str(x) for x in answer)

if __name__ == '__main__':
    n = int(raw_input())
    points = []
    for i in range(2 * n - 1):
        points.append(map(int, raw_input().split()))
    print solve(n, points)