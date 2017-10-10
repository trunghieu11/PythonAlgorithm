__author__ = 'trunghieu11'
from sys import stdin
#stdin = open("p.in","r")

R = lambda : int(stdin.readline())
RM = lambda : [int(x) for x in stdin.readline().split()]

stop = 1200000

prime = [True] * stop
prime[1] = False
for i in range(2,stop):
    if prime[i]:
        j = i*i
        while j < stop:
            prime[j] = False
            j += i

def pal(x):
    return x == x[::-1]

c1 = c2 = 0
ans = 1
[p,q] = RM()

for i in range(1,200):
    if pal(str(i)):
        c1 += 1
    if prime[i]:
        c2 += 1
    if c2 * q <= c1 * p:
        ans = i
    print i, c2, c1, c2 * q, c1 * p
    
print ans