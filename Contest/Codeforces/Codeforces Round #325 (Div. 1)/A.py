__author__ = 'trunghieu11'


def solve(n, children):
    answer = []
    idx = 0
    while idx < n:
        while idx < n and children[idx][2] < 0:
            idx += 1
        if idx >= n:
            break
        scream, runAway, confidence, index = children[idx]
        answer.append(index)
        total = scream
        runAway = 0
        for i in range(idx + 1, n):
            if children[i][2] >= 0:
                children[i][2] -= max(0, total) + runAway
                if children[i][2] < 0:
                    runAway += children[i][1]
                total -= 1
        idx += 1
    print len(answer)
    for x in answer:
        print (x + 1)


if __name__ == '__main__':
    n = int(raw_input())
    children = []
    for i in range(n):
        children.append(map(int, raw_input().split(" ")) + [i])
    solve(n, children)