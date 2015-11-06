__author__ = 'trunghieu11'

def main():
    while True:
        line = raw_input()
        if line == "":
            break
        line = line.split()
        if line[0] == "Correct":
            print line[2], ","

if __name__ == '__main__':
    main()