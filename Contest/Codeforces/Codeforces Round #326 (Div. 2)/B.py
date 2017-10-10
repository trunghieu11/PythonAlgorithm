__author__ = 'trunghieu11'


def solve(n):
    answer = 1
    i = 2
    while i**2 <= n:
        if n % i == 0:
            answer *= i
            while n % i == 0:
                n /= i
        i += 1
    if n > 1:
        answer *= n
    return answer

if __name__ == '__main__':
    n = int(raw_input())
    print solve(n)