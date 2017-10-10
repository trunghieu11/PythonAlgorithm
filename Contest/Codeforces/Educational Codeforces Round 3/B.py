__author__ = 'trunghieu11'


def solve(n, m, books):
    counter = {}
    for x in books:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1
    total = 0
    for x in counter:
        total += counter[x]

    answer = 0
    for x in counter:
        total -= counter[x]
        answer += counter[x] * total
    return answer


if __name__ == '__main__':
    n, m = map(int, raw_input().split(" "))
    books = map(int, raw_input().split(" "))
    print solve(n, m, books)