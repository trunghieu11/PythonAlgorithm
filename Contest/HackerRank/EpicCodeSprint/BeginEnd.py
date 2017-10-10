__author__ = 'trunghieu11'

from string import ascii_lowercase

def main():
    n = int(raw_input())
    s = raw_input()
    answer = 0
    for c in ascii_lowercase:
        total = s.count(c)
        answer += total * (total + 1) / 2
    print answer

if __name__ == '__main__':
    main()