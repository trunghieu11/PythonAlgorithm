__author__ = 'trunghieu11'

def build(n, k, create, expand, flowers, money, sprinklers):
    if sprinklers * create > money:
        return [-1]
    lstIdx = []
    canExpand = (money - sprinklers * create) / expand
    last = 0
    idx = -1
    for i in range(k):
        if flowers[i] - canExpand <= last:
            idx = flowers[i]
        elif idx >= 0:
            if sprinklers <= 0:
                return [-1]
            elif idx - canExpand <= last:
                last = idx + canExpand + 1
                lstIdx.append(idx + 1)
                idx = flowers[i]
                sprinklers -= 1
                if last >= n:
                    return [lstIdx, canExpand]
            else:
                return [-1]
        else:
            return [-1]
    if idx >= 0 and idx - canExpand <= last and idx + canExpand + 1 >= n and sprinklers > 0:
        lstIdx.append(idx + 1)
        return [lstIdx, canExpand]
    return [-1]

def canBuild(n, k, create, expand, flowers, money):
    for i in range(1, k + 1):
        answer = build(n, k, create, expand, flowers, money, i)
        if answer != [-1]:
            return answer
    return [-1]

def main():
    n, k, create, expand = map(int, raw_input().split())
    flowers = list(map(int, raw_input().split()))
    for i in range(k):
        flowers[i] -= 1
    left = 0
    right = 10**15
    while right - left > 1:
        mid = (right + left) >> 1
        if canBuild(n, k, create, expand, flowers, mid) != [-1]:
            right = mid
        else:
            left = mid
    answer = canBuild(n, k, create, expand, flowers, left)
    if answer == [-1]:
        answer = canBuild(n, k, create, expand, flowers, right)
    print len(answer[0]), answer[1]
    print ' '.join(str(x) for x in answer[0])

if __name__ == '__main__':
    test = int(raw_input())
    for t in range(test):
        main()