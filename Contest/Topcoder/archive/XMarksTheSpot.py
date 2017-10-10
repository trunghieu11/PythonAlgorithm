class XMarksTheSpot:
    def countArea(self, board):
        n = len(board)
        m = len(board[0])

        top_max = n
        down_max = 0
        left_max = m
        right_max = 0

        cordinate = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == '?':
                    cordinate.append((i, j))
                if board[i][j] == 'O':
                    top_max = min(top_max, i)
                    down_max = max(down_max, i)
                    left_max = min(left_max, j)
                    right_max = max(right_max, j)

        answer = 0
        question_len = len(cordinate)
        for mask in range(0, (1 << question_len)):
            cur_top = top_max
            cur_down = down_max
            cur_left = left_max
            cur_right = right_max

            for bit in range(0, question_len):
                if (mask & (1 << bit)) != 0:
                    cur_top = min(cur_top, cordinate[bit][0])
                    cur_down = max(cur_down, cordinate[bit][0])
                    cur_left = min(cur_left, cordinate[bit][1])
                    cur_right = max(cur_right, cordinate[bit][1])

            answer += (cur_down - cur_top + 1) * (cur_right - cur_left + 1)

        return answer


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, hasAnswer, p1):
    obj = XMarksTheSpot()
    startTime = time.clock()
    answer = obj.countArea(p0)
    endTime = time.clock()
    testTime.append(endTime - startTime)
    res = True
    if hasAnswer:
        res = answer == p1
    if res:
        print(str("Test #") + str(testNum) + ": Passed")
        return res
    print(str("Test #") + str(testNum) + str(":"))
    print(("[") + str(p0) + str("]"))
    if (hasAnswer):
        print(str("Expected:"))
        print(str(p1))

    print(str("Received:"))
    print(str(answer))
    print(str("Verdict:"))
    if (not res):
        print(("Wrong answer!!"))
    elif ((endTime - startTime) >= 20):
        print(str("FAIL the timeout"))
        res = False
    elif (hasAnswer):
        print(str("OK!!"))
    else:
        print(str("OK, but is it right?"))
    print("Time: %.11f seconds" % (endTime - startTime))
    print(str("-----------------------------------------------------------"))
    return res

all_right = True
tests_disabled = False
testTime = []
# ----- test 0 -----
disabled = False
p0 = ("?.", ".O")
p1 = 5
all_right = (disabled or RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = ("???", "?O?", "???")
p1 = 1952
all_right = (disabled or RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = ("...?.", "?....", ".O...", "..?..", "....?")
p1 = 221
all_right = (disabled or RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = ("OOOOOOOOOOOOOOOOOOOOO",)
p1 = 21
all_right = (disabled or RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = ("?????????OO??????????",)
p1 = 9963008
all_right = (disabled or RunTest(4, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = ("OOO", "O?O", "OOO", "...")
p1 = 18
all_right = (disabled or RunTest(5, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = ("OOOOOOO", "OOOOO.?", "OO.OOOO", ".OO?OOO", "OOO.OOO", "OOOOOOO", "OOOO?.O", "O?OO?OO", "O?OO?O.", "O?O...O", "OOO.OO?", "OOO?O.O", "O.OOO.O", "O..O.OO", "O.OOOOO", "OO.OOO.", "..?.OO?", "OO?OOOO", "?OO?OO.", "?.OOOOO", "O.OOO.?", "O.OOOOO")
p1 = 20185088
all_right = (disabled or RunTest(6, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = ("OOOO.OOOOOOO..O.O..O?OOOOOO...", "OO...O...OOOO.O.?OOOOOOOOOO?OO", ".O.OO.O..OO.OOOOOOOOOO.OOO.OOO", "O.OOOOO.O.O.?OOOO..OO.OO.O.OOO", "OOO...O..OO.OO?..O..OOOO.OOO.O", "OOO.O?OOOOO.OO.OO.OOOO.OOOO?.O", "..O.O..O.OO.OOOO.OO.O..OO.OO.O", "OOOOOOO.O.OO...OOOOO.OOOOO.OOO", "OO.OOOO?O?.OOOO..O.OO..?OO.OO.", "OO.OOOO..?OO.OOOOOOOO?OO...OOO", "..?O.OOO.OOOOOOOOO?OO.O...OOOO", ".OOOOOOO.O.O.O.O..OOOO..O...OO", "O.OOOO.O...?O.O..OOOOOOOOOOO.O", "OOO.OO.OOO..OOOOOOO.O.OOOOOOOO", "OOOOO..O.OOOOOOOOO.O..OOOOO?O.")
p1 = 29491200
all_right = (disabled or RunTest(7, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = ("....O.............OO......O.....O", "O.O.O.O.O..O.....O....O.O.OO.....", "..O.OO....OOO?.O.O...OOO..O..O..O", "O...O...OO..O..O.....O.O...OO.?O.", "?.O..O.OO.OO..OO...O......O......", "O.O......O.OO........O........OOO", ".O....O.O..O..O..........O.....O.", "....O...OO.O..O.......O...?.OO...", ".O..O....?....OOO.........O......", "O.....O.O.......OO.OO....O.O...O.", ".OO.O.O...?......O...............", "........OO.......O.O.O....O......", "?.O........O......O.?..O....OO..O", ".?...O.O.........OOOO....OO......", "O.....O.OOOOO....O.......OO......", ".O..O....O.O......OO...O...O.....", "..O..O.O...O......OO.....O...OO.O", ".O....?....O..O...O.OO....OOOOO.O", "........O....OO..O....O.O.?......", "........O.O.O........OO....O.O...", "...O..O.O...O...O.....O....O?....")
p1 = 2838528
all_right = (disabled or RunTest(8, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = (".OO...OOOOOO?..O.O?O.OO.O.O.O..O.?O.....OOO.O..O", ".OO..O.OO..O.OOOO.O.OO.O..O..O.?OO..O.OOOOOO.O..", "O..OO.....O.OOOO.O....OO.?OOO.....O..OOOOOO..OO.", ".OO..O.O.OO.......O.O..O.OO.OOO.......O..O.O.O.O", ".OO..O....O.OOO.O..OO..?....OO..OOO.O....O..O.O.", ".OOO.?..O..O...OOO.O..OOO......O..O..O...O..OOOO", "...O..OO.....OOO.OO..OO.OO..OO.O....O..O.O.O.O.O", "OOOO.OOO..OO.OOOOOO?.OO.OO.O.O..O..O.O.OO...OO.O", "OO.OOOOO.OOOO........O...O..O..O..OO.O.OOO?.OOOO", "O.?..OOOO.....OOOO...OO.O...O.OOO.O?O.OO.OOO....", ".O..OOO.O.OOOO...OO.O..O...O....O..O..OOO.OO....", "O..OO.OO.O.O...OO.O..OO..OOO.O..OOO.OO...?O.OO.O", "...OOO..O..O..O..O.OOO..O..O.OO.O...O.OOO.?.....", ".....O.......O.O.OOOOOOOOOO..OOO.O.O.O.?.OOO..OO")
p1 = 11010048
all_right = (disabled or RunTest(9, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = (".OO.....OO..OO.O.O..OOO.O..OO.O.O.O", "..O.O.OOOOO...O..OO..OO..OOOO.O.OO.", "OOOO.OOOO.O..O.........O.O.O...OO..", "O?.OO....O?OOO.O.O..OOOOO...O...OOO", "OOO..OO..?OO..OO..OO...OOO.O..OOO.O", "OO.OOO.OO.O.OOO..OO.O.O.O..OO?O.OOO", "O..OOO..O.OOO.O..O..OOOO...OOOOOO.O", ".....O.O.?...O.....O.O......O....O.", ".O.O.OO.?OOO.OO.OOOO.O.OO.O.OOO....", "OOOOOOOOOOOOO.OO..OO....O..O..O..O.")
p1 = 22400
all_right = (disabled or RunTest(10, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = (".O.O.OO....OO.O.OOO....OOO.OO..O.O.OO.", "O.O.OO.OO.O.......OO...O..O....O.OO..O", ".OOO.OO.O..O.O.OO.....O.O.O......OOOOO", ".O...O.OOO.O...OO..OOOOOOOOOO.O.OO.O.O", "O..O.OOOOO..OOOO.O.O?OOO.OOO..OOOO.OO.", "...O....O..OO.OOO..O.O.OOOOOO.OOO.OOO.", "OOOO.OOOO..OOOOO.OO.OO..OOOOO.O..OOO.O", ".O.O.OOO...O.OOOOOO.OOOO.OOOOOO...O.O.", ".OO.O...O.O.OO.OO..O..OO..OO.OO...O.OO", "..OO.OO...OOOO.OOOOO....OOO.O.OOOOOOOO", "O.OOO...OOO.OO..O..OOO..O...O...OOOOO.", "OO.OOOO..OOO.OO....OOOOOOOOOO.OOOO.O..", "OO...OOO.OOO.O.O.OO.OO.O.OO..O.O.OO.O.", "OO....OO.OOOOOOOOO...OO.O.O..OO..OOOO.", "..O..OOO..OO....OO.....O.O.OO.OOOO.OO.", ".OOO.OOOOOOO..OOOO.O.OOO.O..OO.O.OOOO.", "OOOO..O.O.OOOO.O..OO..O.O.OOO..OO..OOO", ".OOO.O..OOOOOO.OO.OOOOOOO.O..O...OO...", ".OOOO.O....OO..OOOO...?OO..OOOO..OO...", "OOOOOOOOOOO.OOOOOOOO.OOOO.....OO....OO", "O..O..O..O.OOO.OO.OOO..O.OO....OO..O.O", "O..O..O.OOO.OOO.O.O.OOOOO...O.OOO.O...", "OOO.O..OOO.OOO.OO.....OO.OOO..OO.O.OOO", "..OOOO.OO.O....OOO.OOOOOOOOOOO..O.O..O", ".?O.?.O.OO..OOOO..OO...O..OOOOOOO.O...", "?O..O..O.O.....?O.OOOOO.O.OOOO.O...OOO", "....OOOOOO..O.OO.OO.....OO.OOOO..OO.OO", "O.OOOOO.O.O.OO.........OO.....OOO.OOOO", "O.OO..OOOOOOO.OOOO.O..OOO.OO..OO.OOOOO", ".OOOOOOOO...O.O..OOOO.OOO...O.OOOOOOO.", "OO...OOOO.O.O..O..O.....OOOOOO.O..OOO.", ".O.OOO.O.O..O.OOOOO...O.OOO...O..O.OO.", "O..O..OO.OOOO.OOOO..OOOOO.OOOO.OO.O.O.", ".OOOO..OOOOOO.OO..O.OOO....OO.O..OO.O.", "O.OO..OO.OOO.O.OOO...OOOO.O.O..O..O.OO", "..OOO.OOOOOOO...OOOOOOO.O...OO..O.OOO.", ".OOOOO.OO....OO.OO..O.OO.O....O.OO.OO.", "OOOOO.O.OO.O.....OOO..OOOO.OO.O.......", "O.OOOOO..O...OOOO...O...O.O.O...OOOOO.", "O..OOOOO.OO..OOO.OO.OOOO..OO.O.O..O.OO", "O..OOOOO..O..O....O.O.O..OOOOO..OOO..O", "O.OOO.O.OOO....OOOOO....OOOOO....OO..O", "OOO.OO..OOOOOOO.O..O.O.OOO.O.O.O.O.OOO", "....O.OOO.O...O.OO.O.O.OOO...O.OOOOOO.", "..OOOO.O.OO.O.O..OOOO...O.OOO.OOOOOO.O", ".OO.OOOOO..OOOO...OOOO.OOOOO.O.OOO.O.O", "...OO...O.O..OO..OOO.OO.OOO.O.O...OOOO", "OOOOOOO..OOOOO..O.O.OOOOO.O.OO.O.OOO.O", "..OOOOOO.OOO...OOO.O..OO..OOOOO.OOOO?.", "O.O.O..OOOOOOOO.O.O.O.....OOOOO.OO...O")
p1 = 243200
all_right = (disabled or RunTest(11, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = ("OOOOOOO?OO?O", "?.OOOOOOOOOO", "O.O.O.OO?OOO", "?OO.O.OOO?O.", "OOOO?OO.OOOO", ".?..OOOO..?O")
p1 = 36864
all_right = (disabled or RunTest(12, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = ("........OO..O..O....", "O.......O...O......O", ".......?.....OOO...O", ".O.O..O...O.........", "....O..........OO...", "..O....O............", "..O....O......OOO...", "O.O..OO.O.O......OO.", ".OO.....O...O......O", "..O....OO.....OOO...", "....O....O...?OO.?..", "O..O......?..OOO....", ".........O..O..?....", "O.......OO...O..O...", ".O?....O.....O.O.OO.", ".........O.......O..", "..OO....O.........OO", "...O.O.......O...O..", ".....?..?...O..O.O..", "..O...O...O.O.....O.", "....................", ".....O..OO...O.....O", "O...O....O.O.......O", "......OOO.......OO..", "...O.O...O.....O.O..", "O...O.O.?..OO..O....", "......?..O..O.....O.", "...OO?O..?........O.", "......OOOOO.....O...", "OO.O..........O....O", ".......O..O.....O?OO", "....O..OO.O....O....", "....OO..O...........", "..O.O....O.O?.....O.", "..O..O..OOO........O", "..O..O......O.......", "O.?.O..OO...........")
p1 = 24248320
all_right = (disabled or RunTest(13, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = ("OOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOO?OOOOO.OOOOOOOOOOOOOOO", "OOOOOO?OOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOO", "OOOOOOOO?OOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOO.OOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOO.O.", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOO?OOOOOOOOOOOOOO.OOOOOOOOO.OOOOOOOOO", "OOO.OOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOO?.OOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "O.OOOO.OOOOOOOOOOOOOO?OOOOO.OOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOO", "OOOOOO?OOOOOOOO?OOOOOOOOOO.OOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOO", ".OOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOO.OOOOOOOO.", "OOOOOOO.OOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOO?OO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOO..OOOOOOOOOOO.OOOOOOOOOOOOOOO", "OOOOOOOOOOOOOO?OOOOOOOOOOOOO.OOOOOOOOOOOOOO", "OOOOOOOOO?OOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOO", "OO.OOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOO.OOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOO", "OOOOOOO.OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "O.OOOOOOOOOOOOOOOOOOOOOOOOOO.OOO?.OOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO..OOO", "OOOOOOOOOO.OOOOO.OOOOOOOOO.OOOOOOOOOOOOOO.O", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OO?", "OOOOOOOO.OOOOO.OOOOOOOOOOOOOOOOOOOOOOO.OOOO", "OOOOOOOOOOOOO?OOOOOO.OOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOO", "OOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
p1 = 52133888
all_right = (disabled or RunTest(14, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = ("OOO?O", "?OOOO", "OOOOO", "O?OOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "?OOOO", "OOOOO", "OOOOO", "?OOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OO?OO", "OOO?O", "OOOOO", "OOOO?", "OOOO?", "OOOOO", "OOO??", "OOOOO", "OOOOO", "?OOOO", "OOOOO", "OOOOO", "OOOOO", "?OOOO", "O?OOO", "OOOOO", ".OO?O", "OOOOO", "OOOOO")
p1 = 6389760
all_right = (disabled or RunTest(15, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = ("OO.OOO.OOO", ".OO.OOOOOO", "OOOO..O.OO", "OOOO.OOOOO", ".O.OOOO.OO", "OOOOOOOOOO", "OOOOO.OOOO", ".OOO.OOOOO", "O.OOOO..OO", "OOOOO.OOOO", "OOOOOOO..O", "OOOOO.OO.O", "OOOOOOOO.O", ".OOOOO.OOO", "O.OOOOOOO.", ".O.O.OOO.O", "OOOOOO.OOO", "OO..O.OOO.", "O..OOO.OO.", "OOOOOO.OO.", "OOO.OOOOOO", "OOOO.OOOO.", "OOOOOOO.O.", ".OOOO.OOO.", ".O..OOOOOO", "OOOO..OO?O", "..OO.OO.OO", ".OOOOOOO.?", ".OOOOOOOO.", "O.O...OOOO")
p1 = 1200
all_right = (disabled or RunTest(16, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = ("OOO.OOOO..O.OOO.OOOOOOOOOOOOOO.OOOOOOOO", "O.OOOOO.OOOOOO...OOOOO.OOOOOOOOOOO.OO.O", "OOOOOOOOO.OOOOOOOOOOOO.OOOOO.OO.OO....O", ".OOOO..OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO.", "OOO.OO.OO.OOOOOOOOOOOOOOOO.OOO.O.OOO.OO", ".OOO..OOOOOOOO.O.OOOOOOOO.O..OO.OOO...O", "..OOO.OOOOOOOO.O.OOOO.OOOO.OOO.OOO.O.OO", ".OOOO.OOOOOO.O.OOO.OOOOOO?OOOOOOOOO.OOO", "O.OOOOOO.OO.OOOO.OOOOOO.O.OO...O.OOOOO.", "O.OOOOOOOOOO.OOO.OOO.OO.OOO.OO.OOO.OOOO", "OOO.OOO..OOOOOOOO.OOOOO..OOOOOOO.OOO?O.", "OOOOOO.OOOOOOOOOOOOO.OO.OO..OOOO.O.OOOO", "...OOOO.OO.OOOOO?OOOOOOOOOOO.OO.OOOO.O.", "OOOOOO..OOOO.OOO.OOOOOOOOOOOOOOOOOOO..O", "OOO.OOOOO.OOOOO.OOOOOOOOOOOOOOOOOOOOOO.", "OOOOOOOOOOOO..OOOOOOO.O.OOOOOOO..OO..OO", "OOOOO.OOO.OO.O.OOOOO.OOOOOOOOOOO.OOO..O", ".OO.O.OOO.O.OOOOOOOOOOO.O.OO..OOO.OOOOO", ".OOOOOOOOOOOOOO.OO.O.OO.OOOOOOOOOOOOOOO", "O.OOO..OOO.OOOOOO.OOOOOO.OOOOOOOOOOOOOO", ".OOOOOOOOOOOOOOOOO.OO.O.O..OOOOOOO.OO.O", "O.O.OOOOO.OO.OOOOOOO.OOOO.OO.OOOOOOOOO.", "OOOO.OOOO.OOOOOOOOOOOOOOOOO.OOOOOOOOOOO", "O.OO.O..OO.OOOOOOOOO.O..OOOOOOOOOOOO.OO", "O.OOOOOOOOOOO?O.OOOOOOOOOOOOOO.OOOOOOOO", "OOOOOOOOOOO.OOOOOO.OOOOOO..OOOOO.OOO.OO", "...OOOOOOO.OOOOOOOOOOO.OOOO?OO..OOOOOOO", "..OOOOOOOO..OOOOO.OO.O.OOOO.OOOOOOOOOOO", "OOOO.OOOOOOOOOOO.OOOOO.O.OOOOOOOOOOOOOO", "OOOOOOOOOOO.OOOOO.OOOOOOOOOOOOOO.OOOOO.", "OOOO.OO.OO.O..OOO.OOOO.OO..OOOOO.OOO.O.", "OOOOO.O..O.OOO.OOOO..OO.OO.OOOOOOOO..OO", "OOOOO.OOOOOOOOOOO.OOO.OOOO.OOOOOOOOOO.O", "OOOOOOO.OOOO.OO.OOO.OOO.OOOOOOOOOOOOOOO", "O.OOOOOOO.OOOO.OOOOOOOO.OOOOOOOOOOOO.OO", "OO.O.O.OOO.OOOOOOOOOOOOOOO.OOOOO.OO.OOO", ".O?.O.OOOO..OOOOO.OO.OOOOOOOOO.OOOOO...", ".OOOO.OOOO.OOOOOOOO.OOOOOOOOOOOOOOOOOO.", "OOOOOOOOOOOOOOOOOOOO.OO.OO.OOOOOOOOO.OO", "OOOOOOOOO.OOOO.OOOOOOOOO.O.OOOOOO.?OOOO", "OOOOOOOOOO.O.OOOOOOO.OOOOO.OOOO.OOOOOOO", "OOOOOOOOOOOOOOO.O...OOOOOOOOOO..O?.OOOO", "OOOOOOOOOO.OOOOO..OOO.O.O..OOOO.OOOOOOO", "O.OOOO..OOOOOOOO.OOOO..OOOOOOOOOOOOOOO.", "OOOO..OO.OOO.O.OOOOO.OOOOO.OOOOOOOO..OO", "OO.OOOO..OOOOOO.OOOOOOOOOOO.OOOOOOOO..O", "OOO.OOOOOOOO.OOOOOO.OOOOOOOOOOOOO.OOOOO", "OOOO.OO.OOOOOOO..O.OOOOOOOOOOO.OOOOOO.O", "OOOOOOOOO.OOOOOOOOO..OOOOOOOOOOO.OOOOOO")
p1 = 489216
all_right = (disabled or RunTest(17, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = ("?..OOOO...?...", ".O............", ".....O.O...O..", "O.O...O.O..O..", ".O.O.O.O...O..", "OO.......?OO.?", ".O........OO..", "...O....O?O..O", "OOO.OO..O.....", "O..OO........?", ".O....?.......", "...O...?..OO.O", "O...O...?O.O..", "O.?...........", "O..O.O?....O..", "O..OOOOO?...O.", ".O.O.OO.......", ".O....O?OO....", "OO..........OO")
p1 = 2179072
all_right = (disabled or RunTest(18, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = ("...OO........O", ".OO.....O.O...", ".O.O...O......", ".O?..OOOO.O?..", ".O.O....O..O.O", "..OOO........O", "O...O..O...O..", "O...O....OOOOO", "OO.O.OO?....O.", "OO...?...OO?..", "..........OOOO", "O.O.O.........", ".......O.O..O.", ".O...?.OOOOOO.", ".O.O?OO...O..O", ".OOOOOOO....O.", "OO....O?O.....", "...O.O.O......", "..OO.O.....OOO", "OO.O...O..O...", "..?OO.?O.....O", "O.O.OO.O.....O", "......OOO.O...", ".O.OOO.O....O.", "O.OO....OO....", "OOO..O..O?O..O", ".O..O.?.?O.O.O", "OO.OO.....?...", "..OO....O....O", "OO.?.....?O...", "OO.........OO.", "..?...O.OO.O.O", "OO..OOO.....OO")
p1 = 60555264
all_right = (disabled or RunTest(19, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = (".O...O.O.............O...........O...........O", ".....O.........................O.......O......", "....O....O....O...O...O.O.O.O.......O......O..", "...O.....O..O.............O....O.......O......", "O.......................O..O.O.O..............", ".....O.O................O..............O..O.O.", "...........O...O.....O.............O..O..O.O..", "..O...O.....OO..................O...O...O.....", "...O..........................OO..............", "..O.................O......O....O.O.O.........", "O.....O........O...O................O.O.....OO", ".......O......O...O......O......O..........O.O", ".O...O....O..........OO.........O.O.....OOO.?.", ".O.......O.O..OO.O..O.OOO....................O", ".....O..O......O.....O......OO....O...O.......", "..O.............O.........?...............O...", "..O.....O........O.....O........O.............", "....O.....O.O...OO...............O........O..O", ".O...O......O...OOO..OO..........O.........O..", "......O......OO...........O.O....O...OO..O....", "..........O...O.....O....O..............O...O.", "...O..............O.O.O...........O......O...O", "...O......O.....O..............O...O......O..O", ".....O.......O...O.....O......................", "..................O.........O.O.O..O.OO...O..O", "........O.............................OO......", "....................O...O.O................O..", "...O..........O..O...O............O...........", "O.................O.O..............O....O.O...", "......O.O.....O..O.....OOO.......?.....OOO....", "O..O......O...O..................OO.O...O.....", "......O......O.......O....O..................O")
p1 = 11776
all_right = (disabled or RunTest(20, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = (".?...O.O....O?OO.", ".O..OOO.O.OO..O?.", "OO.............?.", ".O...O..?OO..O??O", ".?..O?..O.?O..O..", ".O...O...O.?O..OO", "O.........OO...OO", ".OO.?.OO.OOOOO.O.", "...O..O..?OOOO...", "..?...O....O...O.", ".....O...OOO...O.", "...OO..O.OO.O....", ".O?O..OO...OO...O", "...O...?O.O?O..O.")
p1 = 31195136
all_right = (disabled or RunTest(21, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = ("OOOOOOOOOO.OOOOOOOOOOOOOOOOOOOO", "OOOOOOOO.OOOOOOOOOOOOOOOOO.OOOO", "OOOOO.OOOOOOOO.OO.OOOOOOOOOOOOO", ".OOOOOOOOOOOOOOOOOOOOOOOOOOOO.O", "O?OOO.O.OO.OOOOOOOOOOOOOOOO.OOO", "OO.OOOOOOOOOOOOOOOOOOOOOOOOO.OO", "OO.OOOOOOOOOOOOOOOOOOOOOOOOOOOO", ".O.OOOOOOOOOOOOOOOOOOOOOOOOOOOO", "O.OOOOOOOOOOOO?OOOOOOOO?OOOOOOO", "OOOOO.OOOOO.OOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOO.OOO", "OO.OOOOOOOOOOO?OOOOOOOOOOOO.OOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOO.OOOOOOOOOOOOOOOOOOOOOOO", "OOOO.OOOOOOOOO.OOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOO.OOOOOOOOOO.OOOOO", ".OO?OOOOOOOOO?OOOO.OOOOOOOOOO?O", "OOOOOOOOO.OOOO.OOOOOOOOOOOOOOOO", ".OOOO.OOOO?.OOOOOOOO.OOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOO.OOOOOOOOO?OOOOOOOOOOOOO.OO", ".OOOOOOOOOOOO.OOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", ".?OOOO..OOOOO.OOOOOOOOOOOOOOOOO", "OO.OOOOOOOOOOOOOOO?.OOOOOOOOOOO", "OOOOOOOOO.OOOOOOOOOOOOOOOOOOOOO", "O?OO.OOOOO.OOOOOOOOOOOOOOOOOOOO", "OOO.OOOOO.OOOOOOOOOOOOOOOOO.O.O", "OOOOOO?OOOOO.OO.OOOOO.OOOOOOOOO", "OOOOOOOOOOOOOOOOOO.OO.OOO?O.OOO", "OOOOOOOOOOOO?OOO.OOO.OOOOO?OOOO", "OOO.OOO?OOOOOOOOOOOOOOOOOO.OOOO", "OOOOOOOOOOOOOOOO.OOOOOOO.OOOOOO", "OOOOOOOOOOOOOOOOOOOOOO.OOOOOOOO", "OOO?OOOOO.OOOOOOOOOOOOO?OOOOOO.")
p1 = 568852480
all_right = (disabled or RunTest(22, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = (".......O................................", ".................O......O....O..........", "..................................O.....", "O....OO...............O..O.O...O........", "........O........O......O......O..O.....", "..O....O.......O.....O..................", "...............O.O......................", "......O..O.........?....................", "..O..?.....OO....OO.O.OO.......O........", ".............O..O..O....................", "........O.............O..............O..", "...O..............O.....................", "O........O..........OO............O.....", "...O.O.....?.......O................O...", "......................OO......O...O...O.", ".......O.OO......O..........O........O..", "O.?.......................O.........?.O.", "?.O.........O....................O..?.O.", "O..O?......O...........O...O.......?....", "O......................O.....O..........", "..?.....O?....OO........................", "....?.......O.......O....O....O.........", ".......O....O.....O.....................", ".O...O..O..O.OO............O............", "........O......O...O.O..................", "..O.............OO.....O...............O", ".O................OO....................", "...O..............................?.....", "..OO.O..OO..............O...............", "...?...?.......O......O..O......OO......", ".............O........O....O...O.O......", "..O..O........OOO.....OO......?.........", ".............................O.....O....", "O..........OO.......O.......O...........", ".............O................O...O.....", "..O...............O.........?.O.........", "....OO.O....O..............O........OO..", "..................?.....?.O...O.........")
p1 = 796917760
all_right = (disabled or RunTest(23, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = ("...O??O.?..?..OO..?.O..O?O.OO..O.....", ".OO....O??O.....??....O...OO...OO....", "..?OOOO.?..OO?.OOO.OO..OO...?O.O..OO.")
p1 = 1720320
all_right = (disabled or RunTest(24, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = ("?.??", "..OO", "..?.")
p1 = 116
all_right = (disabled or RunTest(25, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = ("......", "O...O.", "......", "..O.OO", "......", "..O...", "...O..", "......", ".O.OO.", ".....?", "......", ".....O", "..O..O", "......", "......", ".....O", "......", "O.....", "......", "......", "......", ".O....", "......", "......", ".?....", "......", "......", "O...OO", "......", ".?....", "......", "......", "......", "?O....", "......", "...O..", "......", "......", "......", "......", "...OOO")
p1 = 3840
all_right = (disabled or RunTest(26, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = ("OO.OOOOOOO.OOOOOOOOOOOOOOOOOOOOOOO..OO..", ".OO.O.O..O.OO.OOOOOOOOO.OOOOOOO.OO.OOOO?")
p1 = 158
all_right = (disabled or RunTest(27, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = ("O..OOO..OOO..O....OO......O..OOOOOO..O..O..O.O..O", "O..O.O.OOO.O....O..O...O.OO..O.O....OO.O.O.OOO.OO", "O.OOO...O.O..O....O..OO..OO?..O....O..O?OOOOOOOOO", "....O..OOO.O...O.O.O.O..O....O....O.O.O..OO.O....", "OOO..OO.OOOOO..OO.O.OOO.O.OO.OOOOO..O...O....O.OO", ".O..O.O..OOO.O.OOOOO...O.OO.........OO.O......OO.", "....OO.O.OO.OO..O.OOO.OOOO...O.OO...O.O..O....OO?", "O......OOO.OO.OOOOOO...O...O.O...O.OO....O....O.O", "...OOO....OO.OOOOOOO.......O.O..O.O..O..O.O...O..", ".OOO..OOO..O..O.O.O....O....O......O.OOOOOO.OO.O.", "..OO.O..O..OOO....OOO.O..O..O..O.OOOO.O...OOO..OO", "..OOOOO..O...O.O..OOOOOOO.O..O.O...O.OO.OO...O.O.", ".......O..OO...O......?OO..O....OO...O.O..O..O...", "O.OOO.O.OOOOO.O.O.O..O......O...O......OO...OOOO.", "OO..O....OO..OO.OOOO....OO.OO....OOO.O..O..O..OOO", "..OOOOO.O..OOOOO..?O..OO..OOOO.OO.OOOO.O....O.O..", ".O.?OOO.O.OO....OOOOOO.O..O.OO..O.O.OO.....O.O..O", ".O..OO.O..OOOO.OO..O.....O..O.O.OO?..O...O..O..OO", ".O.OO..OOOOOOO.OO.OOOOO..O.OO...O.O.....OO......O")
p1 = 119168
all_right = (disabled or RunTest(28, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = ("OOOO.OOOO.OOOOOOOO.OO...O....OOOOOOOOOOOO.OOO.", "OO.OOOOO.OOOOOO..OOO...OOO.OO.OOOOOOO..O.O..OO", "...OOOO..OOOO.O..OOOOOOO..OO.OO.O.O.O.OO?.OOOO", "..OO.OOOO.O.OO.O.OO.OOOOO.........O...OOOO..OO", "OOOOO.O...OO.OO..OOO..OO.O..O.....O..OO.O.O?OO", "OOO.....OOOOOO.O.OO..O.O.OO..OO.O.OO.O.OO?OO.O", "OOOOOOOO.OOO.O.OOOOO..OOO.O.OO.OOO....OOOOO..O", "O.O.O....O.O.OO..OOOOO.O.O.OOO...OO?.OO.OOO.O.", ".O?..OOOO.OO.OOOO.OOOOOOOOO...OOO.O.OOOO.O..OO", "OO.OOO.O.OO.O.??.O...OOO...OO.OOOOOOO..OO..O..", ".OOOOO.....?O..OO.O...O.O.OO..OOO.O.OOOOO.OOO?", "O.O.OOO.O..OO..OOOOO....OO..O..OO?.O.O..OO..OO", ".OOOOOO..O.OO.OOO.OOO...O.OOOOOO.OOO.OO..OOOOO", "OOO.OOO.OOOO.OO.O.OOO..O.OOO.O.OOO.O.OO.OOO.OO", "OO.OOOOOO.O..OOOO.O..O.O...O.O..O..OO.O.OO.O.O", "OOOO.OOOOOOOOOOOO.?OO.O..O.OOOO.O.O.OO.OOOOO.O", "OOOOOOOOO.OO.O.OOOO..OOO...O.OO?OO......OOO.O?", "OOOO.OO.OOOOOO.OOOOOOOO.OOOO..OO...OO.OOOO..O.", "O.OOO.O.OOO...O.O.O...OO.O.O....OOO..O..OOOOOO", "OO.OO.OO.OO.O..O...O?O..O..O....OOO.OO..OOOOO.", "OOO.OOOOO.O.O.O..OOO....OOOOO.OOOOOOOOOOOOOOOO", "OOOOOOOO...O.O..O..OO..OOO.O.O.OO..O..O..OOO..", "OO.OOOOO.O.OOOO.....OOOOOO..O..OOOO.OO.OO.OO.O", "O...OOO..O.OOOOO..OO.OOOOO.OO..OOOOOO.OOO.OO.O", "..OOOOOO?OOOOO.OO.OOOOO.OOOOOO.OO.OO.O.OO..O?O", "OOOOO.O.O..OOO...O.O...O.OOOO.O.O.OOOOO.OOO..O", ".O..OOO...OOOO..OO.O.OOOOOOOOOO?OO..OOOOO.OO.O", "OOOO..OOO.O.OOOO..OOOOO.OO.O...O...O..OO.OO.O.", "OO..O..OOOOOO.OOO.O..O.O.OO.OO.O.O...O.OOOOOO.")
p1 = 174850048
all_right = (disabled or RunTest(29, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = ("..?....?O.?...O??.O....O....O.........OO...", "...........?........O........OO...O........", "..OO.O...OO.O...O.O...O?...?.OO............", "...O..O.?....O..O....O.....O..O............", "...O..............?O.......................", "...O.............?...OO.......O.....O......", "..O............O....?..O.....O.......O....O")
p1 = 1175552
all_right = (disabled or RunTest(30, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = ("O...O...O", "......O.O", ".....O...", ".O...O..O", "...?.....", "?........", "?O....OO.", ".........")
p1 = 504
all_right = (disabled or RunTest(31, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = (".O.OO..OOOO.OO.OOO.OO..O", "O...?.OOO.O.OOOOOOOO.O.O", ".OOO.O..O...O.OOOOO?OOOO", "O.O..OOOOOO?.OOOOOOOOOO.", "O.O.OO.O.O.O...O....OO..", ".O?O.O.OO.OOOO.O.O....OO", ".OO..O.O..OO.OO..OOO.OOO", "OO.OOO.?.OOO.?OO.O?.O.OO", ".OOO.O.OOO....O..O.O..OO", "O....OOOOOOO...??OOO..O.", "...O.?O..OOOOO..O?OO..O.", "O..O?OOO.OO..O.OO?OO.?..", "O...OOO..OOO.O.O..OO.O.O", ".O....OO.O..OO.?OO..OO.O", "OOOOOO.OOO?OOO.OO.OOO..O", ".OO..OOO.OOOOOOO.OOOO..O", "O..OO.OO.O.O.O.OOOO..O.O", "O.OO..O....O.?OOO.O?..OO", "O.OO.OOOOO...OOOO.O.OOOO", "..OOO.OO..O..OO..OO.OOO.", "....O.OO...O?OOO.OO.OO..")
p1 = 264241152
all_right = (disabled or RunTest(32, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = (".O..........O....O..........O....O....", ".OO..OO....O......O..O...OO...........", ".......O....................O.......O.", ".......O.OO........OOO.OO...O....O.O..", "........O.....O...........OO...O......")
p1 = 180
all_right = (disabled or RunTest(33, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = (".OO..O.O.OO...OO..O.OOOO..OO.OO..O..OOOO.OOO..O", "OO..O...OOO..OO.OOO...O..O.O.OO.OO...O.O......O", ".?O.O...OOOOO..O.O..O.O...OO..OO.OO.O...O.OO..O", "...OOOOOOOO.OOO.OO.OO.O....OOOOOOO.OOOO.O..OO..", "O..OOO...OO.O.O.OO.OO....OOOO..O..OOO.OOO..OOO.", ".OO.O.O.....O.OOO...O.O...OOO...OOOO.O.OO.O.OO.", "..OOOOO..O.O..O...OOO..O....O.O.OOO.OO...OO....", "O.OO......O..OO.O.OOO.O....O.OO.O.OO..OO.OOO.O.", ".OO.OO.OOOOO..OOO.OOO.O....O....O.OO.O..OOOOOOO", "..O.OOOOOOO.OOOOO..OO..OOOO.OO.OO.O.O.OOOOO.O..", ".....O.O...OOO.OOOOO..O.OOOO.OO.O..OOO.OOO.OO..", ".OO..OOOOOOOOO..OOOOOO.OOO...O.OO..OOO.O....?O.", "O...OOOOOOOOO.OOO..O....O..O..OO.O.O.O..O....O.", "OOO.OOOO.....OOOO.OO.O.OO.O..OOOO.OO..OO.O.OOOO", "..?OOOO.OO.O..OO..OOOOO..OO..OOO.OO.O.OOOOOO.O.", "..O.OOOOOO.O.OOOOO...OO..OO..OOOOO..O...OOO..O.", "O..OO.O..OO..OO.OOO..O..OO.OOOOOOO.O..OOOOOO.OO", "O..OO.OOOOO..O.OOO.OOOOO.O.OO..O.OO....O.O.OO.O", ".....O.O.OO.OOOOOOOOO...OO...OOOO.OOO.OOOOO..O.", "OO..O..O....O...OO....O.O...O...OO.....OOOOO..O", "..OOOOOO..OOO....OO..O.OOO.OO.OO.OOOO.OO.OOOOO.", "OO.O..O.OOOOOOOO..O.OOOOO.O.O.OO.....OO...O.O.O", "OO..OOOO..O.OOO.O...O..OOOO.OOOO..O.OOO.OOO..OO", "O..O.O.OOO.O.O.OOOOO..OO.O.OOOOOOOO.O.OOOOO.OOO", "...OOOO...O..OO?O.O..O...O..OO.O..OO.O.OOOOO...", "....OO..O..O.OOOO..OO.O.O.O..O.OO....OOO..O...O", "..OOOOO.OOO..OOO....OO...OO...OO..O...O.OO.OO..", "O...OO.OOO..OOOO.OO..O.......OO.O.....OOO.O.OOO", ".O.O.OO.OOOO.OOOO.OOOO......O.OOOO.O..O...OOO.O", "OOO.O.O.OO.O.OOOOO..OO.O.OOOO.OOOOO.OO..OO.OO.O", "OOOO.O.O...OOO..O.OOO.OO.OOOOOO...OO.O...OO..?O", "..O.OOOOO....O..O....O...OOOOOOOO.OOO.OO?.OOOO.", ".O..O....OOO....O.O.O.OOO..OOOO.OO..OOO.O...OOO", "OO..........O.OOO..OOO.OO.OOOOOO.O.O...OOOO..O.", "O..O.O...O.OO.OO.O.OOO.....OO.OOO...O.OO....OOO", ".OO..OO.O.O..O..OO.O.OOO.O..OO.OO.OOO.OO.O.O.O.", ".OOO.OO.OO.OO.OOOO.O.OOO.OO..OOOO.OO.OOOOO.OO.O", "..OOOO.O.O..OOOOOOOOOO.O..O.O.....OOOO..OO..OOO", "..OO.OOOO...O..O..O..O.....OO.OO....OOOO.OOOOO.", "OOOOOO.OO.OOO.O.OOOOO...OOOO...O...OO.OOOO..OOO", ".OO.O.O....OOOOOOO....O.OO..OOOO.OOOOOOOOO...O.", ".OO.OO.OOOO.O..OOOO..OO.O.O.O..O.OOOO..OO.OOO.O", "O.OOO.O.O.O.OOOOO.OOO.OOOOO.OOOO.OOOO...OO.O...", "...........O...O.....O..OO..OO.OOOO..OO..O..O..")
p1 = 132352
all_right = (disabled or RunTest(34, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = ("OOOOO?O.?", "OOO?OOOO.", "OOOOO.OOO", "OOO?.O..O", "OO.OOOOOO", "OOO.OOOOO", ".OOOOO.OO", "O.OO..OOO")
p1 = 1152
all_right = (disabled or RunTest(35, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = (".............................O....", ".O.O.......O.O.O..O.O.........O...", "................O..............O..", "..................................", ".......O.....O....................", "...O..O......O......?..........O..", ".......O.......O.O....?...........", "....O..............O...O..........", ".....O..O......OO..O...O.......O..", ".......O..?...............O.......", "................?.................", "...................O........O.....", "........................OO.....O..", "......?................O....O.....", ".O................................", "......?...........................", ".............................OOO..", "...............O..................", "..........................O..O....", ".......OO......O..O....O......O.O.", ".O................O...O......O....", ".....O.............?..............", "........O..O.........OO...........", "...O...............?...O.......O..", ".....O......?............O........", ".?...................O............")
p1 = 851968
all_right = (disabled or RunTest(36, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = (".......O.....OOOOO..................O..O..O.O..", ".....O..O....O...O......OO.O.....O......O...O..", "O...........O.O.O..O......O...OO.O......O......", "..................O...O.....OO.O...........O...", ".O.OO..O.O..O...O.....O.O...?...........O...O..", ".O........O.O........O....O.O...O...O.OO.......", "O.OO....O..............O.O..O.........O.O......", "..O.OO......OO........O..O.O.OO......O.....O...", ".....O............O.O.....O.......O...O....O...", ".O........OO.?.?....O....O.......O.............", "OO...O....O..O...........O.O...O.....O.O.O...O.", "..OO.OO.O.O.O.........OO...OOOO.........OOOO..O", "O...........O.OO.....O.OO....OOOO..OO..........", "..O...O...........OO..O.....OO.............OO..", "..................O.........O...O..O..O........", ".O....O.O........O..O..........O.........O.....", ".............O....OO.....O...........O.........", ".........O.O..............O.OO..OOO?...O.O.....", ".O..............O..OO.O.O.O.O.O...O...O........", "........O...O.O...O.....O.....O.O..............", ".O.......OO........O....O.......O...O.........O", "...........O.....O....O..O.......OOOO......O...", "...........OO............OO.......O......O.O...", "O.OO.O..O......O..O....OOO...........OO.....O.O", "OO....O..O.....O....O..O..O.....O.....O..O.....", "O.....O..........O...O...OO..OO.O..............", "...OO.O.....OOOOO....O....O....O...............", "O..O..............O.......O..OO.....O.......O..", "OO.OO...........O....O....O........OO....OO....", "O..O..O....O....OO.OO..........................", ".O...O......OO.?.........OO.O..O.O.............", "...OO...O.?O...............O...OO..OO..O....O..", ".........O.....O......O.........OO..OO...OOO.O.", "OO.......O.O....O........?.....O..O.......OO..O", "...O...OO.........O...O.............O....O.O...", ".....O..O........O.............O...O....?......", ".......O.........O.O.......O.O......O....OOO...", "O....O..O.......O....O......O..O......O.O......", "............OO........O....O..O......OO..O.O...", "....O.......OO..........O.......OO..O.......O..", ".................O..O.O.O............O........O", "...O.....O......OO.OO..O.O.O.......OOO..O..O.O.", ".O.......O........O..O..O........OO..O.........", ".........O...OO...........O.....OO...O.........", ".O.......O....O..?..OOO...O..........O.....OO..", "...O....O...?..O...O..O.........O..O...O.....O.")
p1 = 2213888
all_right = (disabled or RunTest(37, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = ("OOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOO.OOOOOO", "OOOOOOOOOOOOOOOO.OOOOOO.OOOOOOOOOOOOOOOOOOO", "OOOOOO.OOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOO", "O.OOOOOOOOOOOOOOOOO.OOO.OOOOOOOOOOOOOOOOOOO", "OOOOOOOOOO.OOOOOOOOOOOOOOO.OOOOOOOOO..OOOOO", "OOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOO.OOOOO.", "OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOO.OOOOOOO.OOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", ".OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOO.OOOOOOOOOOOOOO.OOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOO.OOOOOOOOOO.OOOOOOOOOOOOO?OOOOOOOOO..OO", "OOOOOOOOOOOOOOOOO.OOOOOOOOOO.OOOOOOOOOOOOOO", "OOOOOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO.", "OOOOOOOOOOOOOOOOOOOOOOOOOOOO.O.OOOOOOOOOOOO", "OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOO?OOOOOOO", "OOOOOOO.OOOOOOOOOO.OOOOOOOO.OOOOOOOOOOOOOO.", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOO.OOOOOOOOO.OOOOOOOOO.OO", "OOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOO.O.", "OOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOO.OOOOOOO", "OOOOOOOOOOOOOOOOOO.OOOOO.OOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOO.OOO", "OOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOO.OOOO.OOOOO.OOOOOOOOOOOOOOOO", "O.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOO.OOOO.?OOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOO.OOOO", "OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOO.OOOOOOOOOOOO.OOO.OOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
p1 = 134848
all_right = (disabled or RunTest(38, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = ("O........O..O.OO..O.....OO...OO.O.........O.O", ".......OO.OO..O.O..O.OOO..O...O...O..O....O..", "O.OO..O...O..O...O....O.OO...OOO....O.......O", ".OO.....O....O.....OO..O......OO..O..OOO...O.", "OO.OOO..O..OO.O....O...O.OOO.O.O..O.O....OO..", ".O.....O.O..O..OO...OOO...O...OOO.......OOO..", "..O......O.O.OO..O.....OO........O.....O..O..", "OO....OOO..........O....O..OO................", ".....OO...O.OO..O...O........O.O..O.O.......O", "O...O.O.O......O.......O.OO..O.........O...O.", ".O...O....O...O.O........OOOOO.O..O..OO....OO", "..........OO.OO.OOO........OO.OO.O.O...O.....", "...O...O..O..O.O.O.......O.....O...O.....O.?.", ".OO.OO..O.O..O....O..O...O.....O..O.........O", "........O............O.OO..OO..OO..O...O.O...", "O.....O..O.........O....OO..O....OOO....O....", ".O.O...O....O.......O..O......O.O..O.....OO.O", ".OOO...O....O.OO.....O...O...O.....OOOOO.....", "O.O.OO.....O?..O.O.OO..O...OOO..OO..O.O......", ".....?..O.O......OO.........O.OOO.....OOO....", ".....OO.O.......OOOO...OO..O....O...O...O....", "OO...O.......O.....O....OOO.O.....O..O.?....O", ".O..OO.OO...O.O.....O..OO..O.O.O..OO.........", "O.O..O....O...OO....OOO.....O..........O....O", ".O....O...O.O......O.O......OO..O...O.OO...O.", "O..........O..O.........O....O.OO.O.O...O...O", ".......O..OOO..O...O..........OOO.OO...OOO..O", "..O.......O......OO..O..O.O.OO....O...O...O..", ".OOOOO...OO.O..O.......OOO......O.OOO.OO..O..", "....O.OO..O...O.O.O.....O..O.O.........O.....", "O..O.O.O..O..O..O.OOO..OO....O...............", ".....O.O.......O.O...O.O...O....OOO......O...", "OOO.O..OO..O...O..O.O..O.....O.O.............", "O..O....O.O..OOOOO.........O..O.OOO.O.OO...O.", "..........O...O..OO.O..OO.OOO..O.......OOO..O", "O.....OOO.O....O..O.......OOO....O.O.........", "......O..O..O...........O......O.....O.......", ".....O..O..O.O..O.O..O...............O....O..", ".OOO..O.O......OO....O......O.O.O....O.....O.", "...O....O......O..O..OOOO....O.........O.....", ".OOOO...OO.O..O....O...O......OO....O.O..O.O.")
p1 = 29520
all_right = (disabled or RunTest(39, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = ("O.OOOOO.O.O.OOO.O..OO..OOO.O.OOO.OOOOOO...O.O", "..O..OOOOO.OOOOOO...OOOOO.O.OOO..OO?.O..O.OO.", "O.OO.O.O..OO..O.O.O.O.OOO.O.OOOO.OO....O.OO..", "O.OO.OOO.OOOO?.O..O.OOOOO....OO.O.OO.OO.O.OOO", ".OOO...OOOOO.O.OO..OOOOOO.OOOOOOOOO?..O.OOOOO", "OOO.OOOOOOOOO....O..OOOOOOOO...OOOOOOO.O.O...", "O....OOOOO.OO.O.O.OOOOOO..O.O.O......OOOOO?OO", ".O..O.OOOOOOOOO....O.OOO..O..O....O.OOOO.O.OO", "OOO.O...OO.OO..O.O.OOO...OOO.OOO.O.O...OO...O", "OOOOOOO..O.O..OO.OOO.OOOO.OOO.OO..OOO..O...OO", ".OOOO.OOOOO.O.OOOOOO..O..O.OO...OOO..OOOOOOO.", ".OOO.OO..?OO..OO.O.O.OOOO..OO.OO.OOOOOO.O.OOO", ".O..O..O.O..O.....OO.OO.OO.O.OOOOOOOO.O....OO", "O.OOOOOO...O.OOO...OO..OOOOOOO..OOOOOOOOOO.OO", ".OO...OOO.O..O.OO.OO.O..OOO.O.O.O..OOOO..O..O", ".OOOO.OOO.O..O.OOOOO..OOOOO.OOOOOOOOOOOOOO.O.", ".OOO....OOOOOOO.O.OO..OO.OOOOO..O.OO.OOOO.O.O", ".OOOO.O.OOO.OO...O.OOOOOOOO.OO.OOOO.OOO.OO.OO", "..O..OOO.O.OOOOOO.O.O...O.O.OO.OOOO.O.O..OOOO", "O.OOOOOOOOOOOOOOOOO..O.OOO..OO..OOOOOOO?...OO", "O.O...OOOO..OO.OO.O...OOOO.O...O.O.O...O..O.O", ".OOOOOOOOO....O..O..OO.O..OOO.OOO.OO.OOO..OOO", "O.O..OOO.OO..OO.OO.OO..O.O.OOO.....OO..OO..OO", "OO.O.O.OO.O.OOOO.O.O.O.OOOOO.O.OOOOOOOOO.OOO.", "O.OOOO.OOOOO..OO..O.OOO..O.O.OOO.OO..OOO.OOO.", "OOO....OOOOOO.O.O..OOOO.O..OO.OO.OO.O..OO..O.", "OOO.OOOOO.O.OOO.OO...OOO.O...OOO.OOO..O.OOOOO", "OO.OOOO..OOOOOOOOOO..OOO.O.OO.O..OOOOOO.OOO..", "O.O.O.OOOOOO.O.O.OOOOOO.O.O.O.OOOOOO.O...OOO.", "...OOOOO.OOO..OO.OOOO.OOOO.OO..OO.OOOO.OOOO..", "OOOOOOOO.OOOOOO..OOO.OO.OOO.O.OOOOOO.OO.OO.O.", "OOOOOOOO..OOOO.OOO..OO.OO.OO.OOO.OOOO...O.O.O", "OOOO.OO.OOO.OO..OO.O...OOO...O....OOOOO.OO.OO", "..OO...O.OOOO.O...OOOOOOOO.O..OO.OO.OO....OOO", "O.O.O.O...O.OOOOOOOO.O..OO.O.OOOOO.O..OO.OOOO", ".OO..OO.OOO.OO..OO.OOO.OOO..O..OOO..O.O.OOO..", ".OOOOOO.OOO.OOO.OO.O.O.OO.OOO.O....OOOOO.O..O", "OOO.OOOO...OOO.O..O.....O.OOOO.OOO.O.O.OO.O.O", "OOOO..OOO.OOOOOOOO.OOO....OOOO.OOO.OO.O.OO...", ".O.O..OO.OOO...OO.OO...O.OO..OOOOOOOOOO.OOOO.", "OOOOO.OOOOO..OO.O..OO.O..OOO..OOOOOO.OOO.OOOO", "OOOO.....OOOOOO.OOOO...O.OO.OOO.OO.OOOOO.OO..")
p1 = 120960
all_right = (disabled or RunTest(40, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = ("..O...OO.O.O.....OOO....OOO.OO.O....O.OO....", ".OOO.....OO....O......OOO..O.O.OO.....O..O..", "..O..........O.O..OO..OO....O...............", "O.OO...OOO......O....O...O......OOO...O.O.OO", "O..OOO..O..OO.O.OO...OOO.O....O...O...O..OO.", ".O...O.O.O.O...O...O......O..O...OOO..OO.O..", ".O....O...OOOOO..O.O.......OO...?....OO..OOO", "....O..O.O.O..O.....O......OO........OO.....", "O.O...O.O...OO..OO..OOO...O...OOO...........", ".O......O..O.O.OO.OO...O.O.O.OOO..O....OO...", ".O.OOO...OO..OO.O..OOO.O...O..OO.O..O.OOOOO.", "OO..O...OOOOOO.OOOO.O.O.OOOOO.......O...O...", ".O.......OO.O..O......OO..OO......O.....O..O", "..O..O..O.O.O..O.O..O.OO..O.O.O.......O.O.O.", ".O...OO.....OO..O..O.OO......OO......OOOO.O.", "....O..O..O.O....O.O....O...O...OOO..O.O.OO.", "O......O.O....O...O.O..O....O..O.O.O.O...O.O", "..O.OO.O..OO..O.....O.OOO.OO.............OO.", "...O.......OOOO...O.OO.....OO...O...O....O..", "O.OO.OOO.....OO....O...O.O......OOO..O...O.O", "...O.O.O.O..OO..OO..O......O...O....O.OO.O..", ".OO..O...O...O.......O.O...O.....OOO.O.....O", ".OOO....OO....O.OOO.O.O.O.O..O.OO....O.O....", ".OO..O....O.....O...O..O...........O..OOOOO.", "....O......O.O......O..O....O...OO.O....O..O", "..O...O..O.....O.OOOOOOOOO........O.......OO", ".O.......O.O.OOOOO.O..OO.O.OOOO..O.........O", "OOO......O.....O..O.OO....OO......OO..O..OOO", "..O.O.OO...O......O..OOOO.O......O.O...O...O", "..OO..O.O.O.O.........O........OO..OOO...O..", "O.OO.OO.OOOO....O...O...O...OO..O.....O.O...", "..O...........OO..........O.OO.O...OOO....OO", ".O..O.OO..O.....OO.OO.OO.OO...........O.?O..", "..O...O.OO....OO..O...O.O.O..O.O.OOOO.O....O", "..O.O..OO..OOO....OOOO.OO.O.O.O.....O.O.O.O.", ".O....O..OOO..O..O.O.O..O...O.O.....OO......", "..OO...O....O..O.OO..............O.OO.O...O.", ".........O.O......O..O..O...OO.........OOOO.", ".OO...OOOO.O..OO...O......OO.O...OO.O..OOOO.", ".O......OOOO..O.OOO.OOO......OOOO..O.O...O.O")
p1 = 7040
all_right = (disabled or RunTest(41, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = ("O..OOO.O.......O..O..O...O.....O....O.O.......", ".......O......OOOO.O..O..O...O...........O....", ".O.........O.OO.....O...O................OO...", "........O.OO............O..O...OOO....O.......", "....O..O......................O.O...O..O..O..O", "...O...O...O......O.O.......O.O........O.O.O..", ".O.O.O..O.OO...OO.....OO.......O..OOOO.....O.O", "...O..........O...O......OO...O...O.O...O.....", "O.O..O...OO....O...O.O........O...O.O...O.....", ".....O........O...O.OO..O.......O............O", "..........O.O.OO.OOO..O..O..O....O....O...O...", "..OO...OO.OOO...O....O..........O.....O.OO....", "O....OO.O..OO.O..O..O............O........O...", "....O.......OOO...O..O.....O....O.O...O.......", "..OOO..O..OOO.OO.........O.O.....OO..O.OO.O.O.", "O...............O........OO.......O.OO...O....", "..O.....O....................O.O.O....OO......", "..O.......OO..O...OOO.......O.......O......O..", "...O.......O...........O..O..O....O.O.......O.", "......O.......O...O.....O.OO.................O", "..OO.OO........O.OO....OO..O...O.O...O.......O", "......OO...O.OO..O..O................OO.OO.OO.", "......O........O...O.O.O.......O..O...........", ".O.OOO.O.O......OO.O...O...OO..O....O.........", "..O......O.......O...O...OO..OO......O....OOO.", "..........O.O..OO.......OO.....O.......OOO....", "O....O...O............OOO..O....O.....O......O", ".O.........O........OOOO..........OOO......O..", "..O.........O...O....OOO.....O..O...O...O.....", "..OO.....O..OO.....O.........OOO.......OO.OO.O", "..O..O.O.O.................O..O...O.....OOO...", "..OO.......O.....O.O.O..................OO.O..", "...........O....OO.O...O............O.O.......", "..........O...O...O.OO....O....O.O.O....O.....", ".OO.O..O.O...O...OO..O..O.OOOO.O?.........O...", "OO..O...O.O.OO....OO......O.O..O.......O....O.", "O..O....O...O.OOO.O.O.O......O...O.O....O..O..", ".....O.....O....O.OO...O..OOO.....OO....OO.O.O", "..O.....OO....O.OO.O.O.OO..O.O........O...O..O", ".............OO...O.......OO....OO......O.O...", "..O....O..O.............O.O.....O......O.....O", "O....O...........O....O......O..O...O......O.O", ".O...O...........O..O..O...O..O....O..........", "..O..O.O............O.O.........O.O.........O.")
p1 = 4048
all_right = (disabled or RunTest(42, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = (".....O....................O.......O..O..", ".......O.....O..........................", ".........O....................O.........", ".O.........O...O..........O.............", "O...O...................O..........O....", "..............O.......O......?.O..?..O..", "..O.O.......O........O.....O............", ".............O.................O........", ".O..............O...............?O......", "..........OO........O....O.....O.......O", "O....O...O.O....O.......................", "..............O........OO...............", "O..................O..O.................", ".....................................O..", "..................O....O.O........O..O..", ".........................O.O............", "...OO....O.......................OO.....", ".....................................OO.", "........O......O......O..............O..", "..................O..................O..", ".....................O..?............O..", "..O.......?.........?O...............O..", ".........O.................O...O........", "......O..............O..............O...", "..O.........O.....O.............O.......", ".O...O.............O....................", "..........O......O...............O......", ".........O.....O.........OO...OO......O.", "...........................O..O........?", "..O...............O............O..O.....", "O.......O..........O.O....O.............", "...O..............O.....................", "....OO......OO................O.........", ".........O..........O...OO...O..........", "..........OO...?.......................O", ".........O..................O.....OO....", "....?................O..................", "........O.......O................?......", "..OO....OO.O.O..O..OO.....O.............", "........O...O....O.O....................", ".........................O......OO....O.", "..O.....................O..............O", ".O....................O...O...O...?..O.O", "O...........?.........O.................", ".......O..................?......OO...O.", "........O...O..............OO...........", ".O..........................O.......O..O")
p1 = 15400960
all_right = (disabled or RunTest(43, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = ("....O....O......O..............................", ".OO...............O........O...............O...", "..........?....................................", "...........................O.......O...........", "............................O..................", "..O...................O..........O.............", "............................................O..", "..............O..O...................O........?", "........O...OO.................................", "..O...............?..O......O..............O..O", "...........O.......O......................O....", "............................O.O...O............", "......................O......O.................", "..?....................O......O................", ".....................O............O............", ".O.....O......................................O", ".............O.............................O...", ".............................................O.", "............O.......................O..........", "O......O.......................................", "..............O................................", "..................O...O...O.......O..O.........", "...................O..............?..........O.", "...............................................", "................O?.................O..O........", "...O....O.........O............................", "....?.......O.O................O...............", "O..............................................", "O.O...................O............O...........", "..................O.........O..O...............", ".O.............................................", "................O..........O......O?...........", "....O.......O..................................", "..............OO........O.........O....O.......", "........O.O....................................", "..............O................................", ".....O................O........................", "...O............O..............................", "...O............O.............O.O......O.......", "..O..............OO.......?...................O", "...............................................")
p1 = 962560
all_right = (disabled or RunTest(44, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = ("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOO.OOOOOOO", "OOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOO.O", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOO.OOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOO.OOOOOO.OOOOOOOOOOOOOOOOOOOOOO", "OOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.O", "OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOO", "OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOO.OOOOOOOOOOO", "OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOO.OOOOOOOOO.OOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOO.OOOOOOOOOOOO", "OOOOOOOOOOOOOOO.OOOOOOOOO.OOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOO.OOOOOOOOO.OOOOOOO.OOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOO.OOOOOOOOOOOOO..OOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOO", "OOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOO", "OOOOOOOOOO.OOOOO.OOOO.OOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.O.OOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOO.OOOOO", "OOOO.OOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOO.OOOOO", "OOOOOOOOOOOO.OOOOOOOOOOOOOOOOO?OOOOOOOOOOOOOO", "OO.OOOOOOOOOOOOOOOOOOOOO.OOOOO.OOOO.OOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OO", "OOOO.OOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOO.OOOOOOO.OOOOOOOOOOOOOO", "OOOOOOO.O.OOOOOOOOOO.OOOOOOOOO.OOOOOOOOOOOOOO", "OOOOOOOOOO.OOOO.OO.OOOOOOOOOOOOOOOOOO.OOOOOOO")
p1 = 8460
all_right = (disabled or RunTest(45, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = (".OO.......O.................O...O...O.......", "........O...OO.......OO.O....O......??..OO.O", ".O.O........OOOO....O.OO..O.OO?.........O...", "OO..O.O....O........?.OO.............O....O.", "...........OO.............O......O..........", "......O...O..?..O....?..............O.......", "OO.O....O.......??O...................O...O.", "........OO..............O.O.............O...", ".OO.O.O........OO....O...OO.O..O.OO.....O...", "................O.....O.......O.............", "................O....O......O........O....O.", "...O..?OO........O...O...O..O...O.........OO", ".......OO.........?...O..O....O.............", "...O..O...O...O.....O.......O..OO.O......O..", ".OO..............O....O?..O....O.......O..O.", "....OO.......O..O...?.O....OOO...O..O.......", "O......OOO.......O..........O.O..O..........", ".O...........?..OO............O.OO........O.", "...O..OOO.O?...........O.OO...........O...OO", "...O........O...................OO..O......O", "......OOOO....O.....O....?..O.O...........?.", "O...?.O......OO..O....O.........OO.........O")
p1 = 126877696
all_right = (disabled or RunTest(46, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = ("OO?O.OOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOO.OOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOO", "OOOOOOOOOOOO.OOOO..OOOOOOO..OO.OOOOOOOOOO?OO.O.O", "O.OOO.OOOOO..O.OOOOOOOOOOOOO.OOOOOOOO?OOOOOOOOOO", "OOOOOOOOOOOOOO.O?OOO.OO.OOOOOOO.OOOOOOOOOOOOOO..", "OOOO.OOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOO.OO.OOOOOO", "OO?OOOOOOO.OOOOOOOOOOOOO.OO.OOOOOOOOOOOOOOOOOOOO", "OOOOOO.OOOOO.OOOOOOO.OOOOOOO.O?OOOOOOOOOOOO.OOOO", "OOOOOOOO.OOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOO", "OO.OOOOOOOO.OOOOOOOOO..OOOOOOOOOOOOOOOOO.OOOOO.O", "OOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOO.OOOOOOOOOOOOOOO", "OOO.OOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOO?OOOOOOOOO.", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOO.OOOOOOO.OOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.", "OOO..OOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO.OOO.OOOO.", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOO", "OOOOOOOOOOOOOOOOO.O.OOOOOOOO.OOO.OOOOOOOOOO..O.O", "O.O.OOOOOOOOOOOOOOOOOOOOOOO.OOOO.OOOOOOOOOOOOOOO", "OOO.OOOOOOOOOOO.OOOO.OOOOOOOOOOOOOOO.OOOO.OOOOOO", "OOO?OOO.OOOOOOO.OOO..OOOO.OOOOOOOOOOOOOO.OOOOOOO", "OOOOOOOOOOO.?OOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOO.", "OOOOOOOOOO.OOO.OOO?.O.OOOOOOO.OOOOOOOOOOOO.OOOOO", "OO..OOOOOOOOOOOOO.OOO.OOOOOOOO.OOOOOOO.OOOOOOOOO", "OOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOO.O.OOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOOOOOOO.OOOOOOOOOO", "O.OOO.O.OO.OO.OO.OOO.OOOO.OOOOOOOOOOO.OOOOOOOOOO", "OOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.O", ".OOO.O.OOOOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOO.", "OOOOOOOOOOO.?OOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOO", "OOOOOOOOOOOOO..OOOOOOOOOOOOOOO.OOOOO.OOOOOOOOOOO", "OOO.OOOOO.OOOOOOOOOOOOOOOOOOOOOOOOO.O.OOOO.OOOO.", "?O.OOOO..OOOOOOO?OOOOOOO.OOOOOOOOOOO.OOO.OOOOOO.", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOO", "OOOOOOOO?OOOOO..OOO.OOOOOO.OO.OOOOO.OOOOOOO.OOOO", "OOOOO.OOOOOOOOO.OOOOOOOOOOOOO?OOOOOOOOOOOOOOOOOO", "OOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOO", "OOOOOOOO.OOOOOOOOOOOOOO.OOOOOOOOOOOOO.OOOOOOOOOO")
p1 = 1006632960
all_right = (disabled or RunTest(47, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = ("OOOOOOOOOOOOOO.OOOO", "OOOOOOOOOOOOOOOOOO.", "OOOOOOOO?OOOOOOOOOO", "OOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOO.", "OOOOOOOOOOOOOOOOOOO", "OOO.OOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOO", "OOO..OOOOOO?OOOOOOO", "OOOOOOOOOOOOOOOOOOO", ".OOOOOOO?OOOOOOOOOO", "?O.OOOOOOOOOOOOOOOO", "OOO.OOOO?O?OO.OOO?O", "OOOOOOOO?OOOOOOOOOO", "OOOOOOO?OOOOOO.OOOO", "OOOOOOOO?OOO.?OOOOO", "OOOOOOOOOOOOOOOOOOO", "?OOOOOOOOOOOOOOOO.O", "OOOOOOOOOOOOOOOOOOO", "OOOOOOOOOO?OOOOOOOO", "OOOOOO.OOOOOOOOOOOO", "OO??OOOOOOOOOOOOOOO", "OOOO??OOOOOOOOOOOOO", "O.OO?OOOO?OOOOOOOOO")
p1 = 258998272
all_right = (disabled or RunTest(48, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = (".................?.OO..O", ".....?...O......O.......", "O...?..............?O.?.", ".?.....OO.?............O", "?....O........O.........", "...O.?.?................", "?.......?..O....?.......", ".....O..............O...", ".?.O.O....?.?......?...O", "....O.?.O......?O.......")
p1 = 125829120
all_right = (disabled or RunTest(49, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = ("O...OO.O...O....O.OOO..OO..OO.OOO?.O", "OO.O.OOOOOO.OO.OO.OOO.OOOOO.OOO...O.", ".O..OO..O.....OO..OO.O.OO.OO.O...O?O", ".O..OO...OOOOO..O.OOOOO.OO?OO....OOO", "...OO.O.OOOOOO.OO.O.O..OO.O.OOOO.OOO", "?OO.....O.O.OOO...OO.O..O.?O..O.OOOO", "..?OO..O.OOOO..O.O...OOOO....OOOO...", "?O.OOOOO.O.O..OO.OO.OO..OOO.OO..OOOO", "OOOOO?OOOOO.O.O.O....O.OO.......OO.O", "O..OOOOO.OOOO...O.OOOO.O.....?.OOO..", ".OO...O.O?OOOOOOOO..O.OOOOOO.OOO....", "?O..O.....OO.O.O.OOOO..O.O.OOO..OO.O", ".....OO.O.....O?OOOO?.OO..OO..O.OO..", "OO....OOOOO.OOO.OOO.OOOOOOO.....O..O", "OOO..O.O....OO....OOO.O.O.?.OO..O.O.", "O.O.OOO.OOO..O?O.OOO.OOO?OOO.....OO.", "?OOO.OOO...OOO.OO.OOOO.O.O..OOO.OO..", "O.OOOOOO.O......OOO..O.O.OOO.O..OOOO", ".O.O....O.O..OO.O.?..O.O.O?OO..O..O.")
p1 = 358612992
all_right = (disabled or RunTest(50, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = ("...OOOOOO?..", ".O.O..OOOOO.", "OOO?O.OOO.O.", "..OO.?OO..O.", "OO.OOOOOOOO.", ".OOOO...?OOO", ".?O.OO..OOOO", ".O.O..OO?OOO", "..O?O..OO...", "OOO.OO.?.OOO", "O.OOOOOO.OOO", "O?O.O??O.?OO", ".OOO...?O.OO", ".O..O.OOOOO.", "OO.OOO.?OOOO", "O..OO.O.OOOO", "OO.OOOOO.O..", "OOOOOO.OO.O.", ".OO.O?OOO.OO", "O.OO.OOOOOOO", "OOOOO.OO.?OO", "OOOOOO.O.O?O", "OOOOOOOOOO.O", "..O.OOOOOOOO", "OOOOOO....OO", "OO?OOO..O.O.", "O.OOOO.OOO..")
p1 = 84934656
all_right = (disabled or RunTest(51, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = ("OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOO.", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOO?OOOOOOOOOOOOOOOO.OOOOOOOOOOO", "OOOOOOO..OOOOOOOOOOOOOOOOOOOOOOOOOOOO?O", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOO.OOOOOOOOOOO.OOOOOOOOOOOOOOOOOO", "OOOOOOO.OOOOOOOOOOOOOOOOO?OOOOOOOOOOOOO", "OOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOO.OOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OO", "OOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOO.OO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOO?OOOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOO?OOOOOO.OOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOO?OO", "OOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOO?OOOOOOOOOOOOO?OOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOO.OO.OOOOOOOO?OOOOOOOOOOOO", ".OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.O", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOO?OOOOOOOOOOOOOOOOOOOOO", "OO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OO", "OOOOOOO.OOOOOOO.OOOOOOOOOOOOOOOOOOO??OO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOO?OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOO?OOOOO.OOOOOOOOO", ".OOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOO?OOOO.", "OOOOOOOOOOOOOOO.OOOOOOOO?OOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", ".OOOOOOOOOO.OOOOOOOO.OO.?OOOOOOOOOOOOOO")
p1 = 981467136
all_right = (disabled or RunTest(52, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = ("O..OOO.O.O.OOOO.O...OO..O.O..", "OOO.....O..O...OOO...OOOO....", ".OO..O.?O?O.?.OOO.O.OOO......", "...OO?.OO...O.OO.OOOO.O.OO.O.", "...O.....O.OO..OOOOOO.O?OOO..", "O.O..OO...O..O.OO.O..?O.O...O", ".O.O.O....O..OOO?.O.OOOOO.O..", ".OO...OOO.OOOOO.OOOOO..OOOOOO", "..OOOO..O...?.OO..O.?OOO.OO..", "..O.O..O.....O.OOO.O..OOOOO?O", "OOO.O.OOOO......OO.OO....OOO.", ".....OOO..O..OOO...OO..O.OOOO", "O?O..OO..OOOOOO..OO?...O.OOOO", "O...........O.OOO.......O..OO", ".OO..OOO..O.O.OO..O.OOOO.O...", "OOO.O..OO.OO.OOOO.O.OO..O..O.", "..OOO.O..O.O.OOO..OOO...OOOOO", "OOOOO.OO.O.OOO.OO.O.OOOO....O", "OO.O...OOOOOOOO.OO.OOO.O..OO.", "OOOO..O..OO.OO..O....O.OOOO..", "OOOOOO...O.O..O.O.OOO?O..O.O.", "O.OO..OOO..OOO.OO..O...O.O.?.", "O.OO..OOO...OOOOOOOOOOO.?.OO?", "OOO.OOO.OOO..OOO.OOOOO.OOOO.O", ".OO....O...O.OOOOOOOOO.O....O", ".O.O..O.OO..OOOOOO.O.O.OOO..O", "OOOO..O..OO.O.OOO.O..O.OO.O.O", "?.O..OOOOOOO.OOOOOO..OOOOO.OO", "..O...O.?.OO.OO?OOO.OO.O.OOO.")
p1 = 440926208
all_right = (disabled or RunTest(53, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 54 -----
disabled = False
p0 = (".O...........................O.....O......", ".O....OOO......O...O........O....OO.?...OO", ".................OOO.O....O......O........", ".......O.O......O.O.OOO.OOO....O.OO...O.O.", "....O..O...O.O.....O..OO....?.O.O..O..O.O.", ".O.O.....O..OO.O.O..OOOO..................", ".O..............O..........O.....O..O.O...", "O...O...O......O...O.O.OO......O.OO.......", "O....O....O........O................O....O", "...O...O...OO..?O.O..........O..OO..O..O..", ".?O.O....O...OO.....O.O.OO.O?O.O.......OO.", "....O.?.O..O.O......O?.O........O.O.......", ".OO..O....OOO.......OO.O..O.....O.O.O.....", "........O..OO.O.O.O....O..OO...O.O........", "...O...O..?....O.............O.OOOOO.O?OO.", "....O.......O..OOO.......O..O.O..O.OOO.OO.", "O..O.....O..O.O.OO.......O.O...OOOO.O..OO.", "OOO.O......O..................O....O......", "...?...OO..O..........OO..O.O.O...O.......", "............O.....O......OO.O..O.O.O.O...O", ".......O.O.O...O..O...........O...........", "....O.O.O...O...O....O....O..O..OOOO.....O", "..O...OO....OOO.....O......O............O.", "O.?O.........O...O.OOO....O.....O....O.O..", ".......O.O.......O..O.....O..O.........O..", ".O...OOO...O.....OO......O.O...O..OOO...O.", "...O.O...O.............O.......O..O.....O.", "...O....O......O......O.O.....O....O......", ".......OO.O...........O....OO.OO..........", "..O.O........O....O.........OOO..O....OO..", ".OO.........O.O?.......O.........OO.OO....", "O......O....O.O.....O..?.....?...O....O.O.", ".O...O......O..O.O..O.O.OO.......OO.O.....", "....O.OO..O.......O........O...O.O.O.OO..O", "..OOO......O.O......OO....OOO...........O.", ".O....O...............O....OO..O..O......O", ".O....O........OO..OOO.OO.O.............OO", ".O..O........O.O.O..O.O.....OO........OO..", "...O.....O?O...?O...............OO....O...", "..O....O...O..OO..O..........O.O..........", "O.O.?OO..O.O..O.O..O..O..?.O.OO.......O.O.", "O.......O.....O.........OOO.O..O....O.O...", "....OOO....OO.O..O.....O.O.......O.?..OO..")
p1 = 946864128
all_right = (disabled or RunTest(54, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 55 -----
disabled = False
p0 = (".OOOOOOOOOOOOO.OO.OOOOOOOOOOOOOOOO.OOOOOOOOOOO", "OOOOOOO?OOOOOOOOOOOO.OOOOOO.OOOO.OOOOOOOO.OOOO", "OOOOOOOO.OOOOOOOOOOOO.OOOOOO.OOOOO.OOOOOOOOOO.", "?OOOOOO.OOOOOOO.OOOO.OOOOOO.OOOOO.OOO..OOO.OOO", "OOOOOOOOO..OO.OOOO.O?O.OOO?OOOOOOOOOO.OOO.OO.O", ".OOO.OO.O.OOOOOOOOOOOOOO.OOOOOOOOOOOOOOO.OO?OO", "OOOOO.OOOO.OOOOOO.OO.OOOO.OOOOOOOOO.OOO.OOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOO.O.OOO.OOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO..OOOOO", "O.OOOOOOOO.OOOO.OOOOO.OOOOO.OOO.OOO.OOOO.OO.OO", "O.OOOOOO.OO?OOOOOOOO.OOOO.OOO.OOOOOO?OOOOOOOOO", "OO.OOOOOOOOOOOOO.OOOOOO.OOOOOOOO.OOOOOOOOO.O..", "OOOOOOO.O.OOOOOOO.OOOOO.OOOOOOOOO.OOOOO.OOOOOO", "OOOO.OOOOOOOO.O.OOOOOOO.OOOOOO.OOOOOOOOOOOO.OO", "OOOOOOO..OOOOOOOOOOOOOOOOOOOOO.OOOOOOOOO.?OOOO", "OOOO.O?O.OOOOOOOOOOOO.OOOOOO.O.OO.O.OOOOOOOOOO", "OOOOOOOOO.OO.OOOOOOOOO.OOO.OO.OOOOOOOO.OOOOO.O", "OOO.OOOOOOOO.OO.OOOOOOOOOOO?OOOOOO.OOOOOO.OOOO", "OOOO.OOOOOOOOOOOOOOOOOO.OOOO.O..OOOOOOOO..OO.O", "O.OOOOOOO.OOOOOOOOOOOOOO?OOO.O.OOO.OO..OOOOO.O", "OO.OOOOOOOOOOOOOOOOO.OOOOOOOOO.OOOOO.OO.OOOOOO", "OOOOOOOOOOOOOOOOOOOOOOO.OOOOOOO.OOO.OO.OOO.OOO", "OO.OOOOOOOOOOOOOOOOOOOOOOOOO.OOOOOOOOOOO.OOOOO", "OOOOOOOO.OOOOOO.O.OOOOOOOO.OOOOOOOOOOOOOOOOOOO", "OOOOOO.OOO.O.OOOOOOOO.OOOOOOOOOOOO.OO?OO.OOOOO", "OOOOO..O.OOOOOOOOOOO..OOOOOOOOOOOOO.OO.OO.OOO.", "OOO.OOOOOOO.OOOOOOOO..OOOOOO.OOOOOOOOOOOOOOO.O", "OOOO.O.OOOOOOOOOOO.OOOOO.OOOOOOOOOO?OOOO.OO.OO", "OOO.OOO...OOOOOOOOOOOOOOOOO..OOOOOOOO.OOO.OOOO", "OOO.OOO..OO...OOOOOOOO.OOOOOOOO..OOOOO.OOOOOOO", ".OO.O.OOOOOOO.O.OOOOOOOOOOOOOOOOOOOOOOOOO..OOO", "OOOOOOOOOOOOOOOOOO.OOOOOOOOO.OOOO..OOOOO.OOOOO", "O.OOOOOOOOOOOOOO.OOOOOOOOOOOOOOOOOOO.OOO.OOOOO", "OOOOOOOOOOOOO.O.OOOO?.OO.OO.OOOOOOOO.OOO.OOOOO", "OOOOOOO.O.OOOOOOO?OOOOOOOOOOOOOOOOOO.OOO.O.OOO", "OOO.OOOOOOO.OOOOOOOOOOOOOOOOOOOOOOOOO.O.OOOOOO", ".OOOOOOOOOOOOOO..OOO.OOOOOOOOOOO.OOO.OOOOOOOOO", "OO.OOOO..OOOO?OOOOOO.O.....OOOOO.OOOOOOOOOOOOO", ".OOOOOOO.OO.O.O..O..OOOOOOO.O?OOOOOO.OOOOO.OOO", "OOOOOOOOOOOOOOOOOO.OOOOOOOOOOO.OOOOOOOOO....OO", "OOOOOOOOOOOOOOOOO.O.OOO.OOOOOOO.OOOO...OOOO?OO", "OO..OOOOO.O.OOOOO.OOOOOOOO.OOOOOOOOOOOOOOO.OOO", "O.O.OOO.OOOOOO.OO.OOOOOOOOOOOOO.OOOOOOOOOOOOOO", "OOOOOOOOOOOOOOO.OOOOOO..OOOOOOOOOOO.OOO.OOOOOO", "OOOO.O.OOOOO..OOOO.OO?OOOOOOOOOO.OOO.O.OOOOOO.", "O.OOOOOOO.OOOOOO.O.O.O.OO.OOO.OO.OOO..OOOOOOOO")
p1 = 1109393408
all_right = (disabled or RunTest(55, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 56 -----
disabled = False
p0 = ("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOOOOOO", "OOOOOOO?OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOO", "OOOOO?OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOO??OOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOO?OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOO?OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
p1 = 1310720000
all_right = (disabled or RunTest(56, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 57 -----
disabled = False
p0 = ("...?.", "?....", ".O...", "..?..", "....?")
p1 = 221
all_right = (disabled or RunTest(57, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 58 -----
disabled = False
p0 = ("?................................................O", ".?...............................................O", "..?..............................................O", "...?.............................................O", "....?............................................O", ".....?...........................................O", "......?..........................................O", ".......?.........................................O", "........?........................................O", ".........?.......................................O", "..........?......................................O", "...........?.....................................O", "............?....................................O", ".............?...................................O", "..............?..................................O", "...............?.................................O", "................?................................O", ".................?...............................O", "..................?..............................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", ".................................................O", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
p1 = 1310720000
all_right = (disabled or RunTest(58, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 59 -----
disabled = False
p0 = (".......................?..........................", "..?.......?.......................................", "............?.....................................", ".....?...........??..........?....................", "................................................?.", "........?....?........?...........................", "?............?......................?.............", "........??................?.?.....................", "..................................................", "..................................................", "..................................................", "...............O..................................", "...............O..................................", ".................O...O............................", ".....................O............................", "..................................................", "...........OO................O....................", "..........................O.......O...............", ".............O....................................", "..................................................", ".............O....................................", "..................................................", "...................O...................O..........", "..................................................", ".................................O................", "......................O...........................", ".......................O....O.....................", "...................................OO.............", "..................................................", ".........................O..O......O..............", ".........................O........................", "..................................................", ".................................O................", "................................O.................", "..................................................", "..................................................", "............................O..O..................", "..................................................", "........................O..O......................", ".............O..........O.........O...............", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................")
p1 = 872260316
all_right = (disabled or RunTest(59, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 60 -----
disabled = False
p0 = ("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", "???????????????????OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
p1 = 1310720000
all_right = (disabled or RunTest(60, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 61 -----
disabled = False
p0 = ("..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "...................?..?..?........................", "...................?.???..........................", "....................??O?.?........................", "...................?.???.?........................", "...................?.?..?.........................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................")
p1 = 16700288
all_right = (disabled or RunTest(61, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 62 -----
disabled = False
p0 = ("?????????OO??????????.............................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................")
p1 = 9963008
all_right = (disabled or RunTest(62, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 63 -----
disabled = False
p0 = ("..O.", "O...", "...O", "..O.")
p1 = 16
all_right = (disabled or RunTest(63, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 64 -----
disabled = False
p0 = ("..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "......................?????.......................", ".......................???........................", ".......................?O??.......................", ".......................???........................", "......................?????.......................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................")
p1 = 11938688
all_right = (disabled or RunTest(64, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 65 -----
disabled = False
p0 = ("?.", ".O")
p1 = 5
all_right = (disabled or RunTest(65, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

print("===========================================================")
if all_right:
    if tests_disabled:
        print(str("All test Passed!! (but some test cases were disabled)!"))
    else:
        print(str("All test Passed!!"))
else:
    print(str("Some of the test cases had errors."))
print("Run time: %.11f seconds" % max(testTime))
