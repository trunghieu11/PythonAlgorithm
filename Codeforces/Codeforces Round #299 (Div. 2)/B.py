__author__ = 'trunghieu11'

lucky = []

def build(s):
    if int(s) >= 10**9:
        return
    lucky.append(int(s))
    build(s + "4")
    build(s + "7")

def main():
    build("4")
    build("7")
    lucky.sort()
    n = int(raw_input())
    print lucky.index(n) + 1

if __name__ == '__main__':
    main()