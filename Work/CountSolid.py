__author__ = 'trunghieu11'


if __name__ == '__main__':
    total = 0
    while True:
        line = raw_input()
        if line == "":
            break
        info = line.split(",")
        if int(info[2]) >= 3 and int(info[1]) + int(info[2]) >= 10:
            total += 1
    print total