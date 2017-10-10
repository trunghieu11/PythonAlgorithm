__author__ = 'trunghieu11'
n = int(input())
A = list(map(int, input().split()))
A.sort()
answer = 0
for i in range(1, n):
    increase = max(0, A[i - 1] - A[i] + 1)
    A[i] += increase
    answer += increase
print(answer)