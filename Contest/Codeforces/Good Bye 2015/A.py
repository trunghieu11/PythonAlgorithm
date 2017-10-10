__author__ = 'trunghieu11'

months = [52, 52, 52, 52, 53, 53, 52]

def solve(day, type):
    if type == "week":
        return months[day - 1]
    if day <= 29:
        return 12
    if day == 31:
        return 7
    return 11


if __name__ == '__main__':
    s = raw_input().split(" ")
    print solve(int(s[0]), s[2])