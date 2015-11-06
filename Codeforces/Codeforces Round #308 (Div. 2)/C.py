__author__ = 'OnePiece'

def main():
    ls = map(int, raw_input().split())
    w, m = ls[0], ls[1]
    while m > 0:
        if m % w == 0:
            m /= w
        elif m % w == 1:
            m -= 1
        elif m % w == w - 1:
            m += 1
        else:
             print "NO"
             return
    print "YES"

if __name__ == '__main__':
    main()