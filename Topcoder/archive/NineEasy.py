class NineEasy:
    def count(self, val0, val1):
        return 0


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, p1, hasAnswer, p2):
    obj = NineEasy()
    startTime = time.clock()
    answer = obj.count(p0, p1)
    endTime = time.clock()
    testTime.append(endTime - startTime)
    res = True
    if hasAnswer:
        res = answer == p2
    if res:
        print(str("Test #") + str(testNum) + ": Passed")
        return res
    print(str("Test #") + str(testNum) + str(":"))
    print(("[") + str(p0) + str(",") + str(p1) + str("]"))
    if (hasAnswer):
        print(str("Expected:"))
        print(str(p2))

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
p0 = 2
p1 = (1, 2)
p2 = 4
all_right = (disabled or RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = 2
p1 = (3, 3)
p2 = 12
all_right = (disabled or RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = 2
p1 = (1, 3, 2)
p2 = 16
all_right = (disabled or RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = 5
p1 = (1, 2, 4, 8, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
p2 = 893703876
all_right = (disabled or RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = 1
p1 = (0, 0, 1)
p2 = 200
all_right = (disabled or RunTest(4, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = 1
p1 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
p2 = 333333881
all_right = (disabled or RunTest(5, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = 5
p1 = (31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31)
p2 = 333333881
all_right = (disabled or RunTest(6, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = 5
p1 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31)
p2 = 980
all_right = (disabled or RunTest(7, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = 4
p1 = (15,)
p2 = 2
all_right = (disabled or RunTest(8, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = 1
p1 = (0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1)
p2 = 222222146
all_right = (disabled or RunTest(9, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = 1
p1 = (1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
p2 = 222222706
all_right = (disabled or RunTest(10, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = 1
p1 = (0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0)
p2 = 222222146
all_right = (disabled or RunTest(11, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = 2
p1 = (3, 2, 1, 0, 3, 1, 3, 2, 0, 3, 1, 3, 1, 2, 0, 3, 0, 0, 1, 2)
p2 = 555624679
all_right = (disabled or RunTest(12, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = 2
p1 = (1, 2, 3, 0, 3, 3, 3, 2, 2, 3, 1, 1, 2, 1, 1, 0, 3, 0, 1, 3)
p2 = 680000749
all_right = (disabled or RunTest(13, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = 2
p1 = (2, 1, 3, 0, 3, 0, 2, 3, 1, 3, 1, 0, 0, 3, 2, 3, 3, 1, 1, 1)
p2 = 457784679
all_right = (disabled or RunTest(14, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = 3
p1 = (5, 0, 7, 4, 3, 6, 7, 5, 4, 6, 4, 0, 6, 7, 7, 4, 5, 0, 2, 1)
p2 = 664452425
all_right = (disabled or RunTest(15, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = 3
p1 = (5, 7, 7, 6, 0, 1, 2, 7, 5, 0, 0, 6, 1, 6, 6, 2, 1, 0, 6, 2)
p2 = 470183551
all_right = (disabled or RunTest(16, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = 3
p1 = (4, 2, 5, 2, 2, 7, 3, 1, 2, 3, 5, 4, 3, 4, 7, 6, 3, 2, 0, 3)
p2 = 580336766
all_right = (disabled or RunTest(17, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = 4
p1 = (4, 5, 8, 13, 11, 3, 5, 1, 10, 3, 4, 9, 0, 15, 4, 5, 2, 0, 4, 5)
p2 = 109306378
all_right = (disabled or RunTest(18, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = 4
p1 = (1, 14, 6, 6, 3, 0, 10, 8, 12, 5, 1, 5, 0, 4, 13, 5, 14, 14, 12, 13)
p2 = 138351351
all_right = (disabled or RunTest(19, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = 4
p1 = (10, 15, 10, 0, 10, 6, 0, 8, 4, 7, 11, 4, 3, 1, 5, 15, 3, 2, 7, 8)
p2 = 252780751
all_right = (disabled or RunTest(20, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = 5
p1 = (27, 15, 6, 20, 8, 2, 1, 28, 15, 18, 20, 20, 27, 13, 5, 12, 28, 0, 30, 17)
p2 = 176267203
all_right = (disabled or RunTest(21, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = 5
p1 = (21, 4, 19, 21, 29, 17, 19, 9, 25, 25, 26, 20, 29, 16, 9, 17, 13, 12, 9, 1)
p2 = 894308276
all_right = (disabled or RunTest(22, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = 5
p1 = (31, 5, 0, 5, 16, 31, 27, 8, 27, 24, 25, 0, 18, 1, 19, 24, 25, 3, 2, 10)
p2 = 341103193
all_right = (disabled or RunTest(23, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = 5
p1 = (25, 25, 28, 24, 0, 15, 28, 11, 29, 29, 31, 25, 7, 16, 31, 0, 12, 26, 21, 31)
p2 = 288393436
all_right = (disabled or RunTest(24, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = 5
p1 = (25, 4, 12, 29, 19, 14, 9, 27, 22, 5, 5, 5, 6, 24, 22, 13, 31, 12, 4, 29)
p2 = 267686778
all_right = (disabled or RunTest(25, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = 5
p1 = (28, 7, 16, 8, 19, 11, 4, 25, 29, 31, 28, 5, 15, 22, 10, 22, 8, 0, 17, 16)
p2 = 508700670
all_right = (disabled or RunTest(26, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = 5
p1 = (3, 18, 4, 15, 12, 0, 24, 7, 9, 31, 2, 6, 11, 20, 10, 23, 31, 30, 28, 24)
p2 = 828910486
all_right = (disabled or RunTest(27, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = 5
p1 = (4, 13, 19, 15, 3, 24, 26, 15, 11, 22, 12, 30, 5, 1, 8, 19, 28, 0, 4, 4)
p2 = 978991294
all_right = (disabled or RunTest(28, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = 5
p1 = (20, 8, 24, 11, 19, 12, 18, 11, 14, 0, 18, 28, 13, 30, 6, 25, 3, 25, 7, 10)
p2 = 268192997
all_right = (disabled or RunTest(29, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = 5
p1 = (12, 8, 7, 28, 23, 27, 1, 7, 27, 29, 31, 9, 25, 0, 10, 3, 17, 7, 8, 7)
p2 = 887700065
all_right = (disabled or RunTest(30, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = 5
p1 = (22, 9, 3, 0, 21, 17, 24, 14, 15, 13, 4, 12, 22, 15, 31, 1, 29, 25, 13, 18)
p2 = 85615536
all_right = (disabled or RunTest(31, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = 5
p1 = (8, 18, 31, 17, 28, 11, 0, 15, 24, 19, 18, 25, 17, 24, 5, 5, 8, 2, 2, 26)
p2 = 308348974
all_right = (disabled or RunTest(32, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = 5
p1 = (5, 0, 18, 25, 24, 31, 7, 29, 31, 6, 31, 15, 10, 0, 27, 24, 23, 29, 19, 28)
p2 = 346242919
all_right = (disabled or RunTest(33, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = 5
p1 = (2, 30, 20, 9, 30, 23, 2, 3, 18, 15, 19, 4, 22, 9, 25, 18, 15, 12, 30, 26)
p2 = 774720374
all_right = (disabled or RunTest(34, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = 5
p1 = (3, 0, 4, 25, 18, 31, 14, 20, 15, 7, 28, 19, 26, 18, 21, 23, 18, 14, 2, 0)
p2 = 77966416
all_right = (disabled or RunTest(35, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = 5
p1 = (5, 26, 27, 23, 28, 10, 10, 31, 16, 14, 5, 30, 30, 26, 23, 2, 19, 27, 0, 1)
p2 = 626829947
all_right = (disabled or RunTest(36, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = 5
p1 = (23, 23, 28, 10, 18, 17, 16, 21, 17, 28, 22, 26, 1, 3, 27, 26, 25, 25, 25, 27)
p2 = 885677707
all_right = (disabled or RunTest(37, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = 5
p1 = (11, 18, 1, 18, 6, 3, 27, 8, 13, 12, 8, 29, 31, 10, 14, 27, 0, 12, 0, 30)
p2 = 972417918
all_right = (disabled or RunTest(38, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = 5
p1 = (12, 2, 21, 21, 25, 26, 25, 4, 14, 20, 10, 0, 24, 4, 1, 4, 3, 7, 3, 19)
p2 = 759086689
all_right = (disabled or RunTest(39, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = 5
p1 = (0, 20, 8, 29, 6, 7, 11, 25, 11, 20, 24, 17, 3, 14, 26, 9, 7, 7, 16, 12)
p2 = 778939970
all_right = (disabled or RunTest(40, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = 5
p1 = (18, 20, 3, 28, 24, 21, 18, 14, 16, 17, 24, 3, 14, 24, 24, 10, 14, 25, 30, 5)
p2 = 300316258
all_right = (disabled or RunTest(41, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = 5
p1 = (19, 5, 16, 3, 8, 25, 4, 14, 14, 17, 28, 26, 12, 5, 13, 5, 5, 0, 16, 15)
p2 = 861848698
all_right = (disabled or RunTest(42, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = 5
p1 = (22, 0, 16, 12, 2, 30, 2, 18, 9, 1, 15, 24, 26, 7, 13, 6, 1, 1, 19, 6)
p2 = 290215468
all_right = (disabled or RunTest(43, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = 5
p1 = (15, 30, 25, 19, 13, 10, 25, 13, 31, 15, 29, 4, 12, 0, 14, 4, 10, 10, 6, 27)
p2 = 781832384
all_right = (disabled or RunTest(44, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = 5
p1 = (2, 3, 19, 21, 13, 19, 12, 8, 21, 17, 12, 3, 21, 25, 6, 24, 28, 15, 25, 11)
p2 = 719721769
all_right = (disabled or RunTest(45, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = 5
p1 = (17, 31, 11, 5, 13, 1, 20, 27, 30, 22, 24, 10, 8, 21, 14, 15, 4, 15, 0, 18)
p2 = 358783912
all_right = (disabled or RunTest(46, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = 5
p1 = (6, 21, 25, 1, 17, 8, 16, 13, 28, 1, 14, 2, 13, 29, 25, 3, 30, 3, 22, 2)
p2 = 814842248
all_right = (disabled or RunTest(47, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = 5
p1 = (12, 13, 20, 0, 27, 5, 23, 30, 22, 10, 31, 18, 6, 27, 22, 30, 31, 7, 12, 14)
p2 = 504587632
all_right = (disabled or RunTest(48, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = 5
p1 = (9, 26, 8, 0, 11, 4, 13, 5, 28, 18, 2, 13, 21, 31, 11, 8, 28, 4, 22, 4)
p2 = 607658997
all_right = (disabled or RunTest(49, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = 5
p1 = (16, 11, 24, 14, 3, 19, 10, 4, 17, 0, 27, 28, 24, 25, 29, 20, 20, 20, 22, 19)
p2 = 975150026
all_right = (disabled or RunTest(50, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = 2
p1 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
p2 = 567901286
all_right = (disabled or RunTest(51, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = 5
p1 = (1, 2, 4, 8, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
p2 = 893703876
all_right = (disabled or RunTest(52, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = 2
p1 = (1, 3, 2)
p2 = 16
all_right = (disabled or RunTest(53, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 54 -----
disabled = False
p0 = 1
p1 = (0, 0, 1)
p2 = 200
all_right = (disabled or RunTest(54, p0, p1, True, p2) ) and all_right
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
