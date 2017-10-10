__author__ = 'trunghieu11'


def solve(n, fileSize, usb):
    usb = sorted(usb, reverse = True)
    i = 0
    total = 0
    answer = 0
    while total < fileSize:
        total += usb[i]
        answer += 1
        i += 1
    return answer


if __name__ == '__main__':
    n = int(raw_input())
    fileSize = int(raw_input())
    usb = []
    for i in range(n):
        usb.append(int(raw_input()))
    print solve(n, fileSize, usb)