__author__ = 'trunghieu11'


def solve(solvedTime, tryTime, hackedTime):
    answer = 0
    for i in range(5):
        answer += max(3 * 50 * (i + 1), (500 - 2 * solvedTime[i]) * (i + 1) - 50 * tryTime[i])
    return answer + hackedTime[0] * 100 - hackedTime[1] * 50


if __name__ == '__main__':
    solvedTime = map(int, raw_input().split(" "))
    tryTime = map(int, raw_input().split(" "))
    hackedTime = map(int, raw_input().split(" "))
    print solve(solvedTime, tryTime, hackedTime)