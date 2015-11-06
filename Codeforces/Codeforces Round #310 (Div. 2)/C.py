__author__ = 'trunghieu11'

def main():
    n, k = map(int, raw_input().split())
    answer = 0
    part = 0
    for i in range(k):
        ls = list(map(int, raw_input().split()))[1:]
        if 1 in ls:
            val = 1
            j = 0
            while j < len(ls) and ls[j] == val:
                val += 1
                j += 1
            part += 1
            answer += len(ls) - j
            part += len(ls) - j
        else:
            part += len(ls)
            answer += len(ls) - 1
    answer += part - 1
    print answer

if __name__ == '__main__':
    main()