__author__ = 'trunghieu11'


def solve(hexagon):
    answer = hexagon[0] + hexagon[1] + hexagon[2]
    answer = answer * answer - hexagon[0] * hexagon[0] * 3
    return answer


if __name__ == '__main__':
    hexagon = list(map(int, raw_input().split(" ")))
    print solve(hexagon)