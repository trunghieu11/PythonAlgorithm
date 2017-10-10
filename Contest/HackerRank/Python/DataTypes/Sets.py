__author__ = 'trunghieu11'
input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))
ls = list(a.difference(b))
ls = ls + list(b.difference(a))
ls.sort()
for x in ls:
    print(x)