__author__ = 'trunghieu11'

def evenSum(N):
    total = 0
    counter = 0
    i = 1
    j = 0
    while counter < N:
        for j in range(i):
            total += (1 << i) + (1 << j)
            counter += 1
            if counter >= N:
                break
        i += 1
    return total % 1000000007

def MegaEvenSum(N):
    N = int(N)
    MOD = 1000000007
    left = 0
    right = 2000000000
    while right - left > 1:
        mid = (right + left) / 2
        if mid * (mid + 1) / 2 <= N:
            left = mid
        else:
            right = mid
    k = 0
    if right * (right + 1) <= N:
        k = right
    else:
        k = left

    remain = N - k * (k + 1) / 2

    answer = (k - 1) * power(2, k + 1, MOD) + 2
    answer %= MOD
    answer += power(2, k + 1, MOD) - 2 - k
    answer %= MOD
    answer += remain * power(2, k + 1, MOD) + power(2, remain, MOD) - 1

    return answer % MOD

def power(base, exponent, mod):
    if base >= mod:
        base %= mod
    if exponent == 0:
        return 1 % mod
    result = power(base, exponent >> 1, mod)
    result = result * result % mod
    if (exponent & 1) != 0:
        result = result * base % mod
    return result

if __name__ == '__main__':
    for i in range(1, 10000):
        expected = evenSum(i)
        recieved = MegaEvenSum(str(i))
        if expected != recieved:
            print "----------------------"
            print "i = " + str(i)
            print "expected: " + str(expected)
            print "recieved: " + str(recieved)
    # print evenSum(3)