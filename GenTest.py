__author__ = 'trunghieu11'

from random import randint

def main():
    test = 10
    print test
    for i in range(test):
        n, k = randint(100, 200), randint(1, 20)
        print n, k
        for j in range(n + 1):
            solider = ""
            for x in range(k):
                solider += str(randint(0, 1))
            print solider

if __name__ == '__main__':
    main()