__author__ = 'trunghieu11'
from builtins import hash
n = int(input())
A = tuple(map(int, input().split()))
print(hash(A))