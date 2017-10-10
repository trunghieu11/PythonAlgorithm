__author__ = 'OnePiece'

def main():
    n = int(raw_input())
    answer = 0
    x = 0
    len = 1
    while x * 10 + 9 <= n:
        answer += len * (x * 10 + 9 - x)
        len += 1
        x = x * 10 + 9
    answer += len * (n - x)
    print answer

if __name__ == '__main__':
    main()
