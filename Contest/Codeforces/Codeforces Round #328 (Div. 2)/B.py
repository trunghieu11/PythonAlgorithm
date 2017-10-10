__author__ = 'trunghieu11'


def solve(chessBoard):
    minA = 8
    for j in range(8):
        curAnswer = 0
        for i in range(8):
            if chessBoard[i][j] == '.':
                curAnswer += 1
            if chessBoard[i][j] == 'W':
                break
            if chessBoard[i][j] == 'B':
                curAnswer = 8
                break
        minA = min(minA, curAnswer)
    minB = 8
    for j in range(8):
        curAnswer = 0
        for i in range(7, -1, -1):
            if chessBoard[i][j] == '.':
                curAnswer += 1
            if chessBoard[i][j] == 'B':
                break
            if chessBoard[i][j] == 'W':
                curAnswer = 8
                break
        minB = min(minB, curAnswer)
    return 'A' if minA <= minB else 'B'

if __name__ == '__main__':
    chessBoard = []
    for i in range(8):
        chessBoard.append(raw_input())
    print solve(chessBoard)