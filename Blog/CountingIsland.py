def countIsland(field):
    n = len(field)
    m = len(field[0])

    answer = 0
    for i in range(n):
        for j in range(m):
            # if we meet a land, this must be a new island,
            # increase our answer one and clear all near land
            if field[i][j] == 'X':
                answer += 1
                clearIsland(i, j, field)

    return answer

def clearIsland(x, y, field):
    n = len(field)
    m = len(field[0])

    # if this cell is out of field or not a land, skip this
    if x < 0 or x >= n or y < 0 or y >= m or field[x][y] == '.':
        return

    # clear this cell
    field[x][y] = '.'

    # check near cell and clear if they are land
    clearIsland(x + 1, y, field)
    clearIsland(x - 1, y, field)
    clearIsland(x, y + 1, field)
    clearIsland(x, y - 1, field)

if __name__ == '__main__':
    n = int(raw_input())
    field = []
    for i in range(n):
        field.append(list(raw_input()))
    print countIsland(field)

'''
5
X....
XX...
....X
....X
X....
'''