__author__ = 'trunghieu11'

def main():
    n = int(raw_input())
    s = raw_input()
    print abs(s.count('0') - s.count('1'))

if __name__ == '__main__':
    main()