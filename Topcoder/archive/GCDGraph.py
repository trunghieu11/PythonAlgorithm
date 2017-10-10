__author__ = 'trunghieu11'

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

class GCDGraph:
    def possible(self, n, k, x, y):
        lstFrom = []
        lstTo = []

        for i in range(k + 1, x + 1):
            if x % i == 0:
                lstFrom.append(i)

        for i in range(k + 1, y + 1):
            if y % i == 0:
                lstTo.append(i)

        print lstFrom
        print lstTo

        for a in lstFrom:
            for b in lstTo:
                value = a * b / gcd(a, b)
                print value
                if value <= n or a == b:
                    return "Possible"

        return "Impossible"
