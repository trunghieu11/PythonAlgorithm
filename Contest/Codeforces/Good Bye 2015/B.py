__author__ = 'trunghieu11'


def solve(begin, end, correctNumber):
    answer = 0;
    for x in correctNumber:
        if begin <= x <= end:
            answer += 1
    return answer


if __name__ == '__main__':
    correctNumber = []
    for i in range(1, 65):
        val = (1 << i) - 1
        for j in range(i - 1):
            correctNumber.append(val - (1 << j))
    correctNumber = sorted(correctNumber)
    begin, end = map(int, raw_input().split(" "))
    print solve(begin, end, correctNumber)