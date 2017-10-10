__author__ = 'trunghieu11'


if __name__ == '__main__':
    s = raw_input()
    queryCount = int(raw_input())
    for query in range(queryCount):
        begin, end, k = map(int, raw_input().split(" "))
        begin -= 1
        end -= 1
        sub = s[begin:end + 1]
        size = len(sub)
        k %= size
        s = s[:begin] + sub[size - k:] + sub[:size - k] + s[end + 1:]
    print s