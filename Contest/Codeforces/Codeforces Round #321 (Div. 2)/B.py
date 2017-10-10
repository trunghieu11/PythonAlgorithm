__author__ = 'trunghieu11'


def findIdx(x, left, right, friends):
    while right - left > 1:
        mid = (right + left) / 2
        if friends[mid][0] >= x:
            right = mid
        else:
            left = mid
    return right if friends[right][0] < x else left


def solve(n, minDiff, friends):
    friends.sort(key=lambda friend:friend[0])
    total = [0 for i in range(n)]
    for i in range(n):
        if i == 0:
            total[i] = friends[i][1]
        else:
            total[i] = total[i - 1] + friends[i][1]

    answer = 0
    for i in range(n):
        idx = findIdx(friends[i][0] + minDiff, i, n - 1, friends)
        curAnswer = total[idx] - (total[i - 1] if i - 1 >= 0 else 0)
        answer = max(answer, curAnswer)
    return answer


if __name__ == '__main__':
    n, minDiff = map(int, raw_input().split(" "))
    friends = []
    for i in range(n):
        friends.append(tuple(map(int, raw_input().split(" "))))
    print solve(n, minDiff, friends)