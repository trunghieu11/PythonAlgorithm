__author__ = 'trunghieu11'

import re

def main():
    s = raw_input()
    ab = s.find("AB")
    ba = s.find("BA")
    if ab != -1 and "BA" in s[ab + 2:]:
        print "YES"
    elif ba != -1 and "AB" in s[ba + 2:]:
        print "YES"
    else:
        print "NO"

if __name__ == '__main__':
    main()