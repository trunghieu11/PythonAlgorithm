__author__ = 'trunghieu11'


if __name__ == '__main__':
    n, m = map(int, raw_input().split(" "))
    total = set()
    for i in range(n):
        l = map(int, raw_input().split(" "))
        for x in l[1:]:
            total.add(x)
    print "YES" if len(total) == m else "NO"