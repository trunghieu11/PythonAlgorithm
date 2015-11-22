__author__ = 'trunghieu11'


def solve(n, first, second, cross):
    answer = [cross[0] + sum(second)]
    total = 0
    decrease = 0
    for i in range(len(first)):
        total += first[i]
        decrease -= second[i]
        answer.append(total + cross[i + 1] + sum(second) + decrease)

    answer.sort()
    return answer[0] + answer[1]

if __name__ == '__main__':
    n = int(raw_input())
    first = map(int, raw_input().split(" "))
    second = map(int, raw_input().split(" "))
    cross = map(int, raw_input().split(" "))
    print solve(n, first, second, cross)