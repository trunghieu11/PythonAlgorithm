__author__ = 'trunghieu11'
import random

def getAnswer(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '1':
                return [i, j]
    return [-1, -1]

def fillAnswer(answer, board):
    # fill answer
    board[answer[0]][answer[1]] = '0' if board[answer[0]][answer[1]] == '1' else '1'
    if answer[0] + 1 < 8:
        board[answer[0] + 1][answer[1]] = '0' if board[answer[0] + 1][answer[1]] == '1' else '1'
    if answer[1] + 1 < 8:
        board[answer[0]][answer[1] + 1] = '0' if board[answer[0]][answer[1] + 1] == '1' else '1'

#!/bin/python
def nextMove(player,board):
    ls = []
    for x in board:
        ls.append(list(x))
    answer = getAnswer(ls)
    fillAnswer(answer, ls)
    # print board
    nextAnswer = getAnswer(ls)

    # If I win, return this
    if nextAnswer == [-1, -1]:
        print answer[0], answer[1]
        return

    # check next player can Win?
    fillAnswer(nextAnswer, ls)
    if getAnswer(ls) == [-1, -1]:
        if nextAnswer[0] + 1 < 8 and ls[nextAnswer[0] + 1][nextAnswer[1]] == '1':
            print nextAnswer[0] + 1, nextAnswer[1]
            return
        if nextAnswer[1] + 1 < 8 and ls[nextAnswer[0]][nextAnswer[1] + 1] == '1':
            print nextAnswer[0], nextAnswer[1] + 1
            return
        if answer[0] + 1 < 8 and ls[answer[0] + 1][answer[1]] == '1':
            print answer[0] + 1, answer[1]
            return
        if answer[1] + 1 < 8 and ls[answer[0]][answer[1] + 1] == '1':
            print answer[0], answer[1] + 1
            return

    print answer[0], answer[1]
#If player is 1, I'm the first player.
#If player is 2, I'm the second player.
player = raw_input()

#Read the board now. The board is a 8x8 array filled with 1 or 0.
board = []
for i in xrange(0, 8):
    board.append(raw_input())

nextMove(player,board)
