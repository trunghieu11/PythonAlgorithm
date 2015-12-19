__author__ = 'trunghieu11'


def losslessDataCompression(inputString, width):
    answer = ""
    n = len(inputString)
    for i in range(n):
        window = ""
        j = i - 1
        while j >= 0 and len(window) < width:
            window = inputString[j] + window
            j -= 1
        x = i
        y = 0
        diff = 0
        while y < len(window) and x < n and window[y] == inputString[x]:
            y += 1
            x += 1
        if x == i:
            answer += inputString[i]
        else:
            answer += "(" + str(i) + "," + str(x - i) + ")"
    return answer


if __name__ == '__main__':
    inputString = "abacabadabacaba"
    width = 7
    print losslessDataCompression(inputString, width)