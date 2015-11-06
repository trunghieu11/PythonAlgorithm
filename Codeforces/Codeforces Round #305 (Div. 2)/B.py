__author__ = 'trunghieu11'

def countConsecutive(A):
    answer = 0
    cur = 0
    for x in A:
        if x == 1:
            cur += 1
        else:
            answer = max(answer, cur)
            cur = 0
    return max(answer, cur)


def main():
    n, m, query = map(int, raw_input().split())
    A = []
    s = [0] * n
    for i in range(n):
        A.append(list(map(int, raw_input().split())))
        s[i] = countConsecutive(A[i])

    for q in range(query):
        x, y = map(int, raw_input().split())
        x -= 1
        y -= 1
        A[x][y] ^= 1
        s[x] = countConsecutive(A[x])
        print max(s)

if __name__ == '__main__':
    main()