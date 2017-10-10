genValue = []

def isAllValid(s):
    return isValid(s, '*') and isValid(s, '+') and isValid(s, '-')

def isValid(s, sign):
    digits = "0123456789"
    info = s.split(sign)
    for x in info:
        i = 0
        while i < len(x) and x[i] in digits:
            i += 1
        if x[0] == '0' and i > 1:
            return False
    return True

def dfs(curGen, idx, digits, sequence, target, signCount):
    if idx >= len(digits):
        genValue.append(curGen)
        return

    if sequence <= 4:
        dfs(''.join([curGen, digits[idx]]), idx + 1, digits, sequence + 1, target, signCount)

    if signCount <= 4 and isAllValid(curGen):
        dfs('*'.join([curGen, digits[idx]]), idx + 1, digits, 1, target, signCount + 1)
        dfs('+'.join([curGen, digits[idx]]), idx + 1, digits, 1, target, signCount + 1)
        dfs('-'.join([curGen, digits[idx]]), idx + 1, digits, 1, target, signCount + 1)

def evalValue(numbers, signs):
    while len(signs) > 0:
        idx = -1
        for i in range(len(signs)):
            if signs[i] == '*':
                idx = i
                break

        if idx >= 0:
            value = numbers[idx] * numbers[idx + 1]
            signs.pop(idx)
            numbers.pop(idx)
            numbers.pop(idx)
            numbers.insert(idx, value)
            continue

        value = 0
        if signs[0] == '+':
            value = numbers[0] + numbers[1]
        else:
            value = numbers[0] - numbers[1]
        signs.pop(0)
        numbers.pop(0)
        numbers.pop(0)
        numbers.insert(0, value)

    return numbers[0]

def composeExpression(digits, target):
    dfs("" + digits[0], 1, digits, 1, target, 0)
    answer = []
    print "lenGenSize: ", len(genValue)
    for s in genValue:
        if isAllValid(s):
            numbers = []
            signs = []
            curNum = ""

            for x in s:
                if x == '*' or x == '+' or x == '-':
                    signs.append(x)
                    numbers.append(int(curNum))
                    curNum = ""
                else:
                    curNum += x

            numbers.append(int(curNum))

            if evalValue(numbers, signs) == target:
                answer.append(s)
            # else:
                # print s

    answer = sorted(answer)
    return answer

if __name__ == '__main__':
    print(composeExpression("33456237491", 100000))