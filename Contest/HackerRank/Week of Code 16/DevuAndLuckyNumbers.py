__author__ = 'trunghieu11'

MOD = 10**9 + 7
save = dict()

def calc(A):
    key = tuple(A)
    if key in save:
        answer = save.get(key)
        return answer
    answer = [0, 1]
    for i in range(3):
        if A[i] > 0:
            A[i] -= 1
            curAnswer = calc(A)
            answer[0] = (answer[0] + (i + 4) * curAnswer[1] + curAnswer[0]) % MOD
            answer[1] = (answer[1] + curAnswer[1] * 10) % MOD
            A[i] += 1
    save.setdefault(key, answer)
    return answer

def main():
    A = list(map(int, raw_input().split()))
    answer = calc(A)
    print answer[0]

if __name__ == '__main__':
    main()