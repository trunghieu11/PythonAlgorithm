__author__ = 'trunghieu11'
k, n, w = map(int, input().split())
w = k * w * (w + 1) // 2
print(max(0, w - n))