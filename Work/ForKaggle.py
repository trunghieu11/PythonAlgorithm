__author__ = 'trunghieu11'

def main():
    answer = []
    while True:
        line = raw_input()
        if line == '':
            break
        answer.append(line + " = factor(" + line + ")")
    print '\n'.join(answer)

if __name__ == '__main__':
    main()