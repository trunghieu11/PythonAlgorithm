__author__ = 'trunghieu11'

def maxProductOld(A):
    n = len(A)

    # remember initial answer with very small number
    answer = -10**10

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                product = A[i] * A[j] * A[k]
                if product > answer:
                    answer = product

    return answer

def maxProduct(A):
    n = len(A)

    A = sorted(A)

    # create new array
    # if A have more than 6 elements newA's element will be
    # first three's A elements and last three's A elements
    if len(A) > 6:
        newA = [A[0], A[1], A[2], A[-1], A[-2], A[-3]]
    else:
        newA = A

    answer = -10**10
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                product = newA[i] * newA[j] * newA[k]
                if product > answer:
                    answer = product

    return answer


if __name__ == '__main__':
    A = [1,4,-5,2,-7]
    print maxProduct(A)