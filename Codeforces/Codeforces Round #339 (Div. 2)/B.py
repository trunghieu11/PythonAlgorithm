import sys

__author__ = 'trunghieu11'


def solve(n, A):
    if "0" in A:
        print 0
        return
    answer = "1"
    zeroCount = 0
    for x in A:
        val = x[1:]
        if len(val) <= 0 and int(x) > 1:
            answer = x
        elif len(val) > 0 and int(val) > 0:
            answer = x
        elif int(x[0:1]) > 1:
            answer = x
        else:
            zeroCount += len(x) - 1
    print answer + '0' * zeroCount

if __name__ == '__main__':
    n = int(raw_input())
    A = raw_input().split(" ")
    solve(n, A)