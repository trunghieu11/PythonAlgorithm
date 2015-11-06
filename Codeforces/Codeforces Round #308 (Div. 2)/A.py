__author__ = 'OnePiece'

def main():
    answer = 0
    n = int(raw_input())
    for i in range(n):
        row = list(map(int, raw_input().split()))
        answer += (abs(row[2] - row[0]) + 1) * (abs(row[3] - row[1]) + 1)
    print answer

if __name__ == '__main__':
    main()