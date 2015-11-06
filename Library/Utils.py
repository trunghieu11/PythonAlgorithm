__author__ = 'trunghieu11'

def isPalindrome(x):
    return x == x[::-1]

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

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a