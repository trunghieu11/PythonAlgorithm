__author__ = 'trunghieu11'

import sys

def main():
    keyWords = []
    while True:
        line = raw_input()
        if line == "":
            break
        if "-----" in line:
            continue
        if "Category: " in line:
            print "]"
            line = line[len("Category: ") - 1:].strip().replace(" ", "") + " = ["
            sys.stdout.write(line.upper())
        else:
            sys.stdout.write("\"" + line.strip() + "\",")


if __name__ == '__main__':
    main()