__author__ = 'trunghieu11'

def main():
    n, k = map(int, raw_input().split())
    A = []
    for i in range(n):
        A.append(int(raw_input(), 2))
    need = int(raw_input(), 2)
    answer = 0
    for mask in range(1, 1 << n):
        total = 0
        for bit in range(n):
            if mask & (1 << bit):
                total |= A[bit]
        answer += (total == need)
    print answer

if __name__ == '__main__':
    test = int(raw_input())
    for t in range(test):
        print "answer test #", t
        main()

'''
20 9
001001001
101101101
010010010
110110110
011011011
100100100
001001001
111111111
010010010
110110110
001001001
101101101
010010010
110110110
011011011
100100100
001001001
111111111
010010010
110110110
110110110
'''