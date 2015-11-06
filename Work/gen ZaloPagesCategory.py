__author__ = 'trunghieu11'

def main():
    idx = 100
    while True:
        line = raw_input()
        if line == "":
            break
        splitted = line.split(",")
        upper = splitted[1].replace(" ", "_").upper()
        upper = upper + "(\"" + splitted[1] + "\"," + splitted[0] + "),"
        print upper
        idx += 2

if __name__ == '__main__':
    main()