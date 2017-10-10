__author__ = 'trunghieu11'

def main():
    n = int(raw_input())
    A = list(map(int, raw_input().split()))
    answer = []
    for x in A:
        answer.append(str(len([y for y in A if y > x]) + 1))
    print ' '.join(answer)

if __name__ == '__main__':
    main()