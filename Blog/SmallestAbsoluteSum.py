__author__ = 'trunghieu11'


def smallestAbsoluteSumOld(A):
    n = len(A)

    # initial answer with a very large number
    answer = 10**10

    # try all pairs number in array
    for i in range(n):
        for j in range(i + 1, n):
            answer = min(answer, abs(A[i] + A[j]))

    return answer

def samllestAbsoluteSum(A):
    n = len(A)

    A = sorted(A, key = lambda x: abs(x))

    answer = 10**10
    for i in range(n - 1):
        answer = min(answer, abs(A[i] + A[i + 1]))

    return answer


if __name__ == '__main__':
    A = [1, 10, -3]
    print samllestAbsoluteSum(A)