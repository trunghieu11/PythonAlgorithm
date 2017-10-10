__author__ = 'trunghieu11'


def main():
    a = raw_input().zfill(6)
    b = raw_input().zfill(6)
    print a, b
    if a < b:
        print '<'
    elif a > b:
        print '>'
    else:
        print '='



if __name__ == '__main__':
    main()