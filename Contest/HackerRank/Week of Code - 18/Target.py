__author__ = 'trunghieu11'


def solve(circleCount, shotCount, circles, shots):
    circles = circles[::-1]
    answer = 0
    for s in shots:
        left = 0
        right = circleCount - 1
        distance = s[0] ** 2 + s[1] ** 2
        while right - left > 1:
            mid = (right + left) / 2
            if circles[mid] ** 2 >= distance:
                right = mid
            else:
                left = mid
        if circles[left] ** 2 >= distance:
            answer += circleCount - left
        elif circles[right] ** 2 >= distance:
            answer += circleCount - right
    return answer




if __name__ == '__main__':
    circleCount, shotCount = map(int, raw_input().split(" "))
    circles = list(map(int, raw_input().split(" ")))
    shots = []
    for i in range(shotCount):
        shots.append(tuple(map(int, raw_input().split(" "))))
    print solve(circleCount, shotCount, circles, shots)