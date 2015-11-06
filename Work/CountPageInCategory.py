__author__ = 'hieunt6'

def main():
    while True:
        line = raw_input()
        if line == '':
            continue
        split = line.split(" ")
        result = 0
        category = ""
        for s in split:
            if s.isdigit():
                result += 1
            else:
                category += s + " "
        print category, result

if __name__ == '__main__':
    main()