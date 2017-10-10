__author__ = 'trunghieu11'

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def LCM(n):
    answer = n
    for i in range(1, n + 1):
        answer = answer * i / gcd(answer, i)
    return answer


if __name__ == '__main__':
    n = int(raw_input())
    print LCM(n)