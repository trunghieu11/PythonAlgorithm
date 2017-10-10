__author__ = 'trunghieu11'


def incorrectPasscodeAttempts(passcode, attempts):
    answer = 0
    for x in attempts:
        if x == passcode:
            answer = 0
        else:
            answer += 1
            if answer >= 10:
                return True
    return False


if __name__ == '__main__':
    passcode = "1111"
    attempts = []
    print incorrectPasscodeAttempts(passcode, attempts)