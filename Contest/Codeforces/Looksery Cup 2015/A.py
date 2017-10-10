__author__ = 'trunghieu11'

def main():
    row, column = map(int, raw_input().split())
    image = []
    for i in range(row):
        image.append(list(raw_input()))

    answer = 0
    for i in range(row - 1):
        for j in range(column - 1):
            face = []
            for k in range(2):
                for l in range(2):
                    face.append(image[i + k][j + l])

            isAnswer = True
            for c in "face":
                if c not in face:
                    isAnswer = False
            answer += 1 if isAnswer else 0
    print answer

if __name__ == '__main__':
    main()