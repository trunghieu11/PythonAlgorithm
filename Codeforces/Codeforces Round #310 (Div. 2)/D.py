__author__ = 'trunghieu11'

def getIdx(x, bridges):
    left = 0
    right = len(bridges) - 1
    while right - left > 1:
        mid = (right + left) >> 1
        if bridges[mid][0] >= x[1]:
            right = mid
        else:
            left = mid
    if bridges[right][0] <= x[1] and bridges[right][0] >= x[0]:
        return bridges[right]
    elif bridges[left][0] <= x[1] and bridges[left][0] >= x[0]:
        return bridges[left]
    return [-1, -1]

def main():
    n, m = map(int, raw_input().split())
    islands = []
    for i in range(n):
        islands.append(list(map(int, raw_input().split())))
    bridges = []
    for x in list(map(int, raw_input().split())):
        bridges.append([x, len(bridges)])

    distance = []
    for i in range(1, n):
        distance.append([islands[i][0] - islands[i - 1][1], islands[i][1] - islands[i - 1][0], i - 1])

    distance.sort()
    bridges.sort()

    answer = []
    i = 0
    j = 0
    for x in distance:
        idx = getIdx(x, bridges)
        if idx == [-1, -1]:
            print "No"
            return
        bridges.remove(idx)
        answer.append([x[2], idx[1]])

    print "Yes"
    answer.sort()
    print ' '.join(str(x[1] + 1) for x in answer)


if __name__ == '__main__':
    main()