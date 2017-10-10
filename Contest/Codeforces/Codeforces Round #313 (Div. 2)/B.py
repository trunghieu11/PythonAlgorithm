__author__ = 'trunghieu11'


def solve(rectangles):
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if rectangles[1][0] + rectangles[2][0] <= rectangles[0][0] and rectangles[1][1] <= rectangles[0][1] and rectangles[2][1] <= rectangles[0][1]:
                    return "YES"
                rectangles[2] = [rectangles[2][1], rectangles[2][0]]
            rectangles[1] = [rectangles[1][1], rectangles[1][0]]
        rectangles[0] = [rectangles[0][1], rectangles[0][0]]
    return "NO"


if __name__ == '__main__':
    rectangles = []
    for i in range(3):
        x, y = map(int, raw_input().split())
        rectangles.append([x, y])
    print solve(rectangles)