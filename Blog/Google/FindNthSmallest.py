__author__ = 'trunghieu11'


def findNthSmallest(A, k):
    n = len(A)
    A = sorted(A)
    list = []
    increase = A[:]
    i = 0
    while len(list) < k:
        if i + 1 < n:
            if A[i] <= A[i + 1]:
                list.append(A[i])
                A[i] += increase[i]
            else:
                i += 1
        else:
            list.append(A[i])
            A[i] += increase[i]
            i = 0
    return list[k - 1]


if __name__ == '__main__':
    A = [4, 6]
    k = 100
    print findNthSmallest(A, k)