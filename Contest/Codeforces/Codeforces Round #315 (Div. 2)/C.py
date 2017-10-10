__author__ = 'trunghieu11'

def primTable(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2, n):
        if prime[i]:
            j = i * i
            while j < n:
                prime[j] = False
                j += i
    return prime

def isPalindrome(x):
    return x == x[::-1]

def main():
    p, q = map(int, raw_input().split())
    n = 2000000
    pri = 0
    pal = 0
    isPrime = primTable(n)
    answer = -1
    for i in range(1, n):
        pri += isPrime[i]
        pal += isPalindrome(str(i))
        if pri * q <= pal * p:
            answer = i
    print answer

if __name__ == '__main__':
    main()