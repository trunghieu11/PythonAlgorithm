__author__ = 'trunghieu11'

def main():
    n, k = map(int, raw_input().split())
    boys = list(map(int, raw_input().split()))
    girls = list(map(int, raw_input().split()))
    boys.sort()
    girls.sort()
    answer = 0
    i = 0
    j = 0
    while i < n and j < n:
        if abs(boys[i] - girls[j]) <= k:
            answer += 1
            i += 1
            j += 1
        elif boys[i] > girls[j]:
            j += 1
        else:
            i += 1
    print answer

if __name__ == '__main__':
    main()