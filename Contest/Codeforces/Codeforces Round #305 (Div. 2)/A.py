__author__ = 'trunghieu11'

def isPalindromes(s):
    mid = len(s) / 2
    left = list(s[:mid])
    right = list(s[mid + len(s) % 2:])
    right.reverse()
    return left == right

def main():
    s = raw_input()
    k = int(raw_input())
    if len(s) % k != 0:
        print "NO"
        return
    l = len(s) / k
    for i in range(k):
        if not isPalindromes(s[l * i: l * (i + 1)]):
            print "NO"
            return
    print "YES"

if __name__ == '__main__':
    main()