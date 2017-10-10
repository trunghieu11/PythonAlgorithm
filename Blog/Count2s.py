__author__ = 'trunghieu11'

MAX_DIGIT = 20

def count2(n):
    total2 = [0 for i in range(0, MAX_DIGIT)]

    # total 2s from 0 to 9
    total2[1] = 1

    # continue calculate 2s from 0 to 99, 0 to 999, etc...
    for i in range(2, MAX_DIGIT):
        total2[i] = total2[i - 1] * 10 + 10**(i - 1)

    answer = 0

    # example: 123 = 1 * total2[2] + 2 * total2[1] + 23 + 3 * total2[0] + 10^0
    for i in range(len(n)):
        # calculate number of 2 exists
        value = int(n[i])
        digits = len(n) - i - 1
        answer += value * total2[digits]

        # if this digits is 2, increase answer by all remains value
        if value == 2:
            answer += int("0" + n[i + 1:len(n)]) + 1

        # if this digits is larger than 2, increase answer by 10**digits
        if value > 2:
            answer += 10**digits

    return answer

def countNormal(n):
    n = int(n)

    answer = 0
    for i in range(1, n + 1):
        value = str(i)
        answer += value.count("2", 0, len(value))
    return answer

if __name__ == '__main__':
    for i in range(10000000):
        if count2(str(i)) != countNormal(str(i)):
            print "False ", i