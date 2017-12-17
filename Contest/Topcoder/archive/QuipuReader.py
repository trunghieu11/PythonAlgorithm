class QuipuReader:
    def readKnots(self, knots):
        n = len(knots)
        counter = [0 for i in range(n)]
        answer = [0 for i in range(n)]
        row_size = len(knots[0])

        for i in range(row_size):
            max_idx = [0]
            for j, x in enumerate(counter):
                if counter[max_idx[0]] < x:
                    max_idx = [j]
                if counter[max_idx[0]] == x:
                    max_idx.append(j)

            has_change = False
            for m in max_idx:
                if knots[m][i] == 'X':
                    has_change = True

            if not has_change:
                if sum(counter):
                    for k, x in enumerate(counter):
                        answer[k] = answer[k] * 10 + x
                counter = [0 for k in range(n)]

            for j in range(n):
                if knots[j][i] == 'X':
                    counter[j] += 1

        if sum(counter):
            for i, x in enumerate(counter):
                answer[i] = answer[i] * 10 + counter[i]
        return tuple(answer)


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, hasAnswer, p1):
    obj = QuipuReader()
    startTime = time.clock()
    answer = obj.readKnots(p0)
    endTime = time.clock()
    testTime.append(endTime - startTime)
    res = True
    if hasAnswer:
        res = compare_answer(answer, p1)
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

def compare_answer(my_answer, correct_answer):
    if isinstance(my_answer, float) and isinstance(correct_answer, float):
        return round(my_answer, 6) == round(correct_answer, 6)
    return my_answer == correct_answer
all_right = True
tests_disabled = False
testTime = []
# ----- test 0 -----
disabled = False
p0 = ("-XXXXXXX--XX-----XXXXX---", "---XX----XXX-----XXXX----", "-XXXXX---XXXXX--XXXXXXXX-")
p1 = (725, 234, 558)
all_right = (disabled or RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = ("XX---XXXX", "XXX-----X")
p1 = (24, 31)
all_right = (disabled or RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = ("-XXX---XX----X", "--X----X-XXXXX", "-XX--XXXX---XX")
p1 = (321, 115, 242)
all_right = (disabled or RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = ("-------X--------", "--XXX----XXXX---", "--------------XX")
p1 = (100, 3040, 2)
all_right = (disabled or RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = ("---------X----------------------", "--------------------------------", "---X----------------------------", "-----------X--------------------", "--X-----------------------------", "--------------X-----------------", "------------X-------------------", "------X-------------------------")
p1 = (1000, 0, 100000, 100, 1000000, 1, 10, 10000)
all_right = (disabled or RunTest(4, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = ("XXXXXXXXX-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX-XXXXXXXX-X", "XXXXXXXX---XXXXXXXX-XXXXXXXX---XXXXXXXX--XXXXXXX--", "------------XXX---------X-------XXXXXXX--XXXXXXX--", "-----XXX--XXXXXXXXX-----XXXX----XXX---------XXX--X")
p1 = (999981, 888870, 31770, 394331)
all_right = (disabled or RunTest(5, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = ("-X-X-X-X-", "XX----XXX")
p1 = (1111, 2003)
all_right = (disabled or RunTest(6, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = ("--XX--------XXXXXX---X-----XX--------", "--XXXXXXXX--XXXX-----XX----XXXXXXXXX-", "--XXXXXXXX-----------XXX---XXXXXXXXX-", "--XXXXX-----XXXXXXXX-XXX---XX--------", "--XXXXXXXXX-XXX------XXXXX-XXXXXXXXX-")
p1 = (2612, 8429, 8039, 5832, 9359)
all_right = (disabled or RunTest(7, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = ("-XXXXXXXXX-XX-------------XXXXXXX---", "-XXXXXX----XXXXXX---XXXX--XXX-------", "-XXXX------XXX------XXX---XXXX------", "-XXXXXXX------------X---------------", "-X---------XXXXX----XXXXX-XXXXXXXX--")
p1 = (9207, 6643, 4334, 7010, 1558)
all_right = (disabled or RunTest(8, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = ("-XXX-------XXXX------XXXXXXXX---XX-----", "-X-------------------XX---------X------", "-----------XXXXX-----XXX--------XXXXXX-", "-XX--------XXXXXXXXX-XX---------XXXX---", "-XXXXXXXX--XXXXXX----XXXXXX------------", "-X---------XXX-------XXXXXXXX---X------", "-XXX-----------------XX---------X------", "-XXXX------X---------X----------X------")
p1 = (3482, 1021, 536, 2924, 8660, 1381, 3021, 4111)
all_right = (disabled or RunTest(9, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = ("-XXXXX------XXXXXXX---XXXXXXX------XXX---", "-XX---------XXXXX--------XX---------X----", "-XXXX-------XXX------------------XXXXXXX-", "-XXX---------X--------XXXXXX-------------", "-XXXXXXXX--XXXXXXXXX----------------XX---", "-XXXXXX----XXXXXXXXX----------------X----", "-XXXXXX------X----------XXXX-------------", "-XXXXXX-----XXXXX-----XXXXXXXX-XXXXXXXXX-")
p1 = (5773, 2521, 4307, 3160, 8902, 6901, 6140, 6589)
all_right = (disabled or RunTest(10, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = ("---XXX---XXXXXXX----XXXXXXXXX-XXXXXXXXX----XXXX---", "-----------XX------------X----XXXXXXXX---XXXXXXX--", "----X-----XXXX---------XXXXXX---XXXXXX------X-----", "-----------XX------------XX------XXXX-------XX----", "--XXXX-----------------XXXXX----XXXXXX------XX----", "----XX-----XXX--------XXXXXXX---------------X-----", "----X----XXXXX------XXXXXXXXX---XXXXX----XXXXXXXX-", "----XX---XXXXXXXXX-------X-------XXXX-----XXXXX---", "----XX-----XX---------XXXXXXX----XX---------XX----", "---------XXXXXX---------------XXXXXXXX---XXXXXX---")
p1 = (37994, 2187, 14661, 2242, 40562, 23701, 15958, 29145, 22722, 6086)
all_right = (disabled or RunTest(11, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = ("--XXX-----XXXX----XXXXXXXX--------XXX-----------", "---X--------XX----XXXXXX----------XXXX--XXXXXXX-", "---------XXXXXXXX-------------XXXXXXXXX----X----", "---X--------X------XXXX--------XXXXXXXX--XXXXX--", "---X--------XX------XX---------XXXXXXXX---XXXX--", "--XXX----XXXXX-----XXXXX----------XXXX----------", "---------XXXXX----XXXXXX----------X-------------", "--XXX-------XX----XXXXXXX------------------XXX--", "-XXXX---------------X-------------XXX------XXX--", "---X-----XXXXXXXX-XXXXXXXXX----XXXXXXX-----XXX--")
p1 = (34830, 12647, 8091, 11485, 12284, 35540, 5610, 32703, 40133, 18973)
all_right = (disabled or RunTest(12, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = ("--XXX-XXXXXXXX----------XXXXXXXXX--XXXXXXXX-", "--XX----XXXX-----XXXXXX---XXX------XXXXXXXX-", "--------------------X----XXXXXXXX--XXXXXXXX-", "--XX-------X------XXXX----XXX-------XXXXXX--", "--XXX---XXXXX-------X------XX--------X------", "-XXXX--XXXXXXX-----------XXXXXXX----XXXXX---", "-----------X---XXXXXXXX----XX--------XXX----", "-----------X---XXXXXXXX----X----------------", "---X--XXXXXXXX--XXXXXXX---XXX---------------", "--XX---XXXXXXX--XXXXXXX----XX-------XXXXX---")
p1 = (38098, 24638, 188, 21436, 35121, 47075, 1823, 1810, 18730, 27725)
all_right = (disabled or RunTest(13, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = ("--XXX--XXXXXXX------------XXX-------", "--XXX---XX-----XXXXXX-----XXXX-XXX--", "-------XXXXXXXX-XXXXX--XXXXXXX-XXXX-", "--XX----XXXX---XXXXXX------XX--XXX--")
p1 = (37030, 32643, 8574, 24623)
all_right = (disabled or RunTest(14, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = ("----XXXX-XXXXXXXX----XX-----XXX--XXXXXX---", "----XXXX--XXXXXXX-XXXXXXX----XX-----------", "-----X----XXXXXXX-XXXXXXX---XXX--XXXXXX---", "----XXXX------XX-XXXXXXXX-XXXXXXX-XXXXX---")
p1 = (48236, 47720, 17736, 42875)
all_right = (disabled or RunTest(15, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = ("--XXXX---XXX----XXXXXXXXX--XXXX-----XXXX----", "--XXXX--XXXX--------------XXXXXXX-XXXXXXXX--", "XXXXXX-XXXXXXXX-XXXXXXXXX-XXXXX--XXXXXXXXX--", "--XXXX--XXXXX----XXXXXX---XXXXXXX--XXXXXX---")
p1 = (43944, 44078, 68959, 45676)
all_right = (disabled or RunTest(16, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = ("XXX----X----XXXX-------XX------XXXXXXXXX", "X-----XXXX---XXX---XXXXXXXXX------X-----", "XXX----X--XXXXXXXXX---XXX--------XXXXXX-", "XXX---XXX-XXXXXXXX----------------XXXX--")
p1 = (31429, 14391, 31936, 33804)
all_right = (disabled or RunTest(17, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = ("-----XX-XXX---------XXX-------XXX---XXXX------", "------X-XXXXX-------XXX-----------------------", "------X-XXXXX----XXXXXXXXX----XXX-XXXXXXXXX---", "---XXXX-XXX------XXXXXXXXX-XX-XXXX--XXXXXXX---")
p1 = (233034, 153000, 159039, 439247)
all_right = (disabled or RunTest(18, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = ("------------XXXXXXX----------XXXXX-", "-X---XXXXXXX--XXX---XXXXXX-XXXXXXXX", "-XX-XXXXXXXX--------XXXX-----XXXX--", "-XXX--XXXXXX-XXXXX---X-------XXX---")
p1 = (705, 17368, 28044, 36513)
all_right = (disabled or RunTest(19, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = ("XX----XXXXXXXXX-XXXXX--XXXXXXXXX----XXXXXXXXX-", "XX-------XXXX--XXXXXXXX-----XX-------XXXXXXX--", "XX-------X--------------XXXXXXXX---------XX---", "-------XXXXXXX------------XXXXXX----XXXXXXXXX-")
p1 = (29599, 24827, 21082, 7069)
all_right = (disabled or RunTest(20, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = ("X", "-")
p1 = (1, 0)
all_right = (disabled or RunTest(21, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = ("-XXX---XX----X", "--X----X-XXXXX", "-XX--XXXX---XX", "--------------")
p1 = (321, 115, 242, 0)
all_right = (disabled or RunTest(22, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = ("X-------------------------------------------------", "-XXXXXX-XXXXXX-XXXXXXX-XXXXXX-XXXXXXXXX-XXXXXXXXX-", "-XXX-------XXX---XX-----X----------XXX----XXXXX---", "-XXXXX---XXXXX--XXX-----XXX--------XX-----XXX-----", "------------------------XXXX---------------XX-----", "--X---------X----X------X----------X-------X------")
p1 = (1000000, 667699, 332135, 553323, 402, 111111)
all_right = (disabled or RunTest(23, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = ("X-----", "-X----", "--X---", "---X--", "----X-", "-----X")
p1 = (100000, 10000, 1000, 100, 10, 1)
all_right = (disabled or RunTest(24, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = ("X--", "XX-", "X-X")
p1 = (10, 20, 11)
all_right = (disabled or RunTest(25, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = ("X-", "-X")
p1 = (10, 1)
all_right = (disabled or RunTest(26, p0, True, p1) ) and all_right
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
