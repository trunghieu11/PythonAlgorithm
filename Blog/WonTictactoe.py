__author__ = 'trunghieu11'

def someoneWon(table):
    for i in range(3):
        table[i] = list(table[i])

    isWon = False

    # check rows and columns
    for i in range(3):
        if table[i][0] != '.' and table[i][0] == table[i][1] == table[i][2]:
            isWon = True
        if table[0][i] != '.' and table[0][i] == table[1][i] == table[2][i]:
            isWon = True

    # check two diagonals
    isWon |= (table[0][0] != '.' and table[0][0] == table[1][1] == table[2][2])
    isWon |= (table[0][2] != '.' and table[0][2] == table[1][1] == table[2][0])

    return isWon

if __name__ == '__main__':
    table = ["XO.",
             ".X.",
             "OOX"]
    print someoneWon(table)