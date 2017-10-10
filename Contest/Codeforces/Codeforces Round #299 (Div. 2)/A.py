__author__ = 'trunghieu11'

def main():
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tynumbers = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    n = int(raw_input())
    if n < 20:
        print numbers[n]
    elif n % 10 == 0:
        print tynumbers[n / 10]
    else:
        print tynumbers[n / 10] + "-" + numbers[n % 10]


if __name__ == '__main__':
    main()