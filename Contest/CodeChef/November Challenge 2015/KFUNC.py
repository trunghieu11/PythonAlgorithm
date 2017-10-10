__author__ = 'trunghieu11'

import random

def sumOfDegit(x):
    answer = 0
    for c in str(x):
        answer += int(ord(c) - ord('0'))
    return answer if answer < 10 else sumOfDegit(answer)

def bruteForce(begin, distance, left, right):
    answer = 0
    left -= 1
    for i in range(0, right):
        if i >= left:
            answer += sumOfDegit(begin + i * distance)
    return answer

def solve(begin, distance, left, right):
    left -= 1
    right -= 1

    begin = sumOfDegit(begin + left * distance)
    distance = sumOfDegit(distance)
    visited = []
    total = 0
    firstTotal = 0
    circleLen = 0
    answer = 0
    step = 0

    cur = begin
    i = left
    while i <= right:
        if cur in visited:
            while begin != cur:
                left += 1
                circleLen -= 1
                firstTotal += sumOfDegit(begin)
                begin = sumOfDegit(begin + distance)
            answer += firstTotal
            step = total - firstTotal
            break
        else:
            circleLen += 1
            total += sumOfDegit(cur)
            visited.append(cur)
            cur = sumOfDegit(cur + distance)
            i += 1

    if i > right:
        return total

    answer += ((right - left + 1) / circleLen) * step
    remain = (right - left + 1) % circleLen
    for i in range(remain):
        answer += sumOfDegit(cur + i * distance)

    return answer

if __name__ == '__main__':
    testCase = int(raw_input())
    for test in range(testCase):
        begin, distance, left, right = map(int, raw_input().split())
        print solve(begin, distance, left, right)

    # for i in range(100):
    #     begin = random.randint(1, 20)
    #     distance = random.randint(1, 10)
    #     right = random.randint(20, 100)
    #     left = random.randint(1, right)
    #     answer1 = bruteForce(begin, distance, left, right)
    #     answer2 = solve(begin, distance, left, right)
    #     if answer1 != answer2:
    #         print begin, distance, left, right
    #         print "Expected: " + str(answer1)
    #         print "Received: " + str(answer2)