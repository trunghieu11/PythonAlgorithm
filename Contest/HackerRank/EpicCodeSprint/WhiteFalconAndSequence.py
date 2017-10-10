__author__ = 'trunghieu11'

def main():
    n = int(raw_input())
    A = list(map(int, raw_input().split()))
    answer = -10**30
    for i in range(n):
        for j in range(n - 1, i, -1):
            curAnswer = 0
            x = i
            y = j
            while x < y:
                curAnswer += A[x] * A[y]
                x += 1
                y -= 1
            answer = max(answer, curAnswer)
    print answer


if __name__ == '__main__':
    main()