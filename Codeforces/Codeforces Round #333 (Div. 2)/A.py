__author__ = 'trunghieu11'


def solve(n1, b1, val1, n2, b2, val2):
    realVal1 = 0
    for x in val1:
        realVal1 *= b1
        realVal1 += x
    realVal2 = 0
    for x in val2:
        realVal2 *= b2
        realVal2 += x
    if realVal1 < realVal2:
        return '<'
    if realVal1 > realVal2:
        return '>'
    return '='


if __name__ == '__main__':
    n1, b1 = map(int, raw_input().split(" "))
    val1 = map(int, raw_input().split(" "))
    n2, b2 = map(int, raw_input().split(" "))
    val2 = map(int, raw_input().split(" "))
    print solve(n1, b1, val1, n2, b2, val2)