__author__ = 'trunghieu11'


def solve(n, m, windows):
    answer = 0
    for i in range(n):
        for j in range(0, m, 2):
            answer += windows[i][j] or windows[i][j + 1]
    return answer


if __name__ == '__main__':
    n, m = map(int, raw_input().split(" "))
    m *= 2
    windows = []
    for i in range(n):
        windows.append(map(int, raw_input().split(" ")))
    print solve(n, m, windows)