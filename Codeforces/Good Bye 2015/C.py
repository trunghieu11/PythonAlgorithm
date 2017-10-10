__author__ = 'trunghieu11'


if __name__ == '__main__':
    rowCount, columnCount = map(int, raw_input().split(" "))
    table = []
    for i in range(rowCount):
        table.append(list(raw_input()))

    cache = [[0 for j in range(columnCount)] for i in range(rowCount)]
    for i in range(rowCount):
        for j in range(columnCount):
            if i - 1 >= 0:
                if table[i - 1][j] == '.' and table[i][j] == '.':
                    cache[i][j] += cache[i - 1][j] + 1
                else:
                    cache[i][j] += cache[i - 1][j]
            if j - 1 >= 0:
                if table[i][j - 1] == '.' and table[i][j] == '.':
                    cache[i][j] += cache[i][j - 1] + 1
                else:
                    cache[i][j] += cache[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                cache[i][j] -= cache[i - 1][j - 1]

    rowReduce = [[0 for j in range(columnCount)] for i in range(rowCount)]
    columnReduce = [[0 for j in range(columnCount)] for i in range(rowCount)]

    for i in range(1, rowCount):
        for j in range(columnCount):
            if j == 0:
                rowReduce[i][j] = table[i][j] == '.' and table[i - 1][j] == '.'
            elif table[i][j] == '.' and table[i - 1][j] == '.':
                rowReduce[i][j] = rowReduce[i][j - 1] + 1
            else:
                rowReduce[i][j] = rowReduce[i][j - 1]

    for j in range(1, columnCount):
        for i in range(rowCount):
            if i == 0:
                columnReduce[i][j] = table[i][j] == '.' and table[i][j - 1] == '.'
            elif table[i][j] == '.' and table[i][j - 1] == '.':
                columnReduce[i][j] = columnReduce[i - 1][j] + 1
            else:
                columnReduce[i][j] = columnReduce[i - 1][j]

    queryCount = int(raw_input())
    for query in range(queryCount):
        idx = map(int, raw_input().split(" "))
        for i in range(4):
            idx[i] -= 1

        answer = cache[idx[2]][idx[3]]
        if idx[0] > 0:
            answer -= cache[idx[0] - 1][idx[3]]
        if idx[1] > 0:
            answer -= cache[idx[2]][idx[1] - 1]
        if idx[0] > 0 and idx[1] > 0:
            answer += cache[idx[0] - 1][idx[1] - 1]
        answer -= rowReduce[idx[0]][idx[3]] - (0 if idx[1] - 1 < 0 else rowReduce[idx[0]][idx[1] - 1])
        answer -= columnReduce[idx[2]][idx[1]] - (0 if idx[0] - 1 < 0 else columnReduce[idx[0] - 1][idx[1]])
        print answer