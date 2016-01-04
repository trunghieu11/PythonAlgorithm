
if __name__ == '__main__':
    total = 0
    while True:
        line = raw_input()
        if line == "":
            break
        info = line.split(" ")
        total += int(info[1])
    print total