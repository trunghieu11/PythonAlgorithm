__author__ = 'trunghieu11'


def solve(n, topFloor, info):
    info = sorted(info, reverse = True)
    curTime = 0
    curFloor = topFloor
    answer = 0
    for x in info:
        answer += curFloor - x[0]
        curTime += curFloor - x[0]
        curFloor = x[0]
        if curTime < x[1]:
            answer += x[1] - curTime
            curTime = x[1]
    return answer + curFloor



if __name__ == '__main__':
    n, topFloor = map(int, raw_input().split(" "))
    info = []
    for i in range(n):
        info.append(map(int, raw_input().split(" ")))
    print solve(n, topFloor, info)