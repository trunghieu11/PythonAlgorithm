__author__ = 'trunghieu11'

from string import ascii_lowercase

def main():
    s = raw_input()
    a = raw_input()
    b = raw_input()

    totalS = dict()
    totalA = dict()
    totalB = dict()
    for c in ascii_lowercase:
        totalS.setdefault(c, s.count(c))
        totalA.setdefault(c, a.count(c))
        totalB.setdefault(c, b.count(c))

    maxA = min(totalS[c] / totalA[c] for c in ascii_lowercase if totalA[c] > 0)
    maxVal = [0, 0]
    for i in range(maxA + 1):
        tempS = dict(totalS)
        for c in ascii_lowercase:
            if totalA[c] > 0:
                tempS[c] -= totalA[c] * i
        remainB = min(tempS[c] / totalB[c] for c in ascii_lowercase if totalB[c] > 0)
        for c in ascii_lowercase:
            if totalB[c] > 0:
                tempS[c] -= totalB[c] * remainB
        if maxVal[0] + maxVal[1] < i + remainB:
            maxVal = [i, remainB]

    answer = maxVal[0] * a + maxVal[1] * b
    for c in ascii_lowercase:
        answer += c * (totalS[c] - totalA[c] * maxVal[0] - totalB[c] * maxVal[1])
    print answer


if __name__ == '__main__':
    main()