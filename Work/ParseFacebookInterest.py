__author__ = 'hieunt6'

def main():
    line = raw_input()
    i = 0
    while i < len(line):
        text = ""
        while i < len(line) and line[i] != '>':
            i += 1
        i += 1
        while i < len(line) and line[i] != '<':
            text += line[i]
            i += 1

        allText = True
        for c in text:
            if c not in " ()'" and not c.isalpha():
                allText = False
        if allText and len(text) > 0:
            print text
        i += 1

if __name__ == '__main__':
    main()