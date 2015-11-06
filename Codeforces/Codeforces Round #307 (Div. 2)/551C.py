__author__ = 'trunghieu11'

def isOk(n, m, A, ls, k):
    remain = 0
    for i in range(len(ls) - 1, -1, -1):
        canDo = k - ls[i] - 1
        if canDo <= 0:
            return False
        need = (A[ls[i]] - remain + canDo - 1) // canDo
        remain = canDo * need - (A[ls[i]] - remain)
        m -= need
        if m < 0:
            return False
    return True

def main():
    n, m = map(int, raw_input().split())
    A = list(map(int, raw_input().split()))
    ls = [i for i in range(n) if A[i] > 0]
    left = 0
    right = 10**15
    while right - left > 1:
        mid = (right + left) >> 1
        if isOk(n, m, A, ls, mid):
            right = mid
        else:
            left = mid
    print right if isOk(n, m, A, ls, right) else left

if __name__ == '__main__':
    main()