class TorusSailingEasy:
    def expectedTime(self, val0, val1, val2, val3):
        return 0


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, p1, p2, p3, hasAnswer, p4):
    obj = TorusSailingEasy()
    startTime = time.clock()
    answer = obj.expectedTime(p0, p1, p2, p3)
    endTime = time.clock()
    testTime.append(endTime - startTime)
    res = True
    if hasAnswer:
        res = answer == p4
    if res:
        print(str("Test #") + str(testNum) + ": Passed")
        return res
    print(str("Test #") + str(testNum) + str(":"))
    print(("[") + str(p0) + str(",") + str(p1) + str(",") + str(p2) + str(",") + str(p3) + str("]"))
    if (hasAnswer):
        print(str("Expected:"))
        print(str(p4))

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
p1 = 2
p2 = 1
p3 = 1
p4 = 1.0
all_right = (disabled or RunTest(0, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = 2
p1 = 2
p2 = 0
p3 = 1
p4 = -1.0
all_right = (disabled or RunTest(1, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = 4
p1 = 6
p2 = 1
p3 = 3
p4 = 27.0
all_right = (disabled or RunTest(2, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = 4
p1 = 7
p2 = 2
p3 = 3
p4 = 180.0
all_right = (disabled or RunTest(3, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = 6
p1 = 8
p2 = 3
p3 = 6
p4 = -1.0
all_right = (disabled or RunTest(4, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = 8
p1 = 6
p2 = 1
p3 = 0
p4 = -1.0
all_right = (disabled or RunTest(5, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = 3
p1 = 3
p2 = 1
p3 = 1
p4 = 2.0
all_right = (disabled or RunTest(6, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = 2
p1 = 2
p2 = 1
p3 = 0
p4 = -1.0
all_right = (disabled or RunTest(7, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = 10
p1 = 10
p2 = 9
p3 = 9
p4 = 9.0
all_right = (disabled or RunTest(8, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = 10
p1 = 10
p2 = 1
p3 = 1
p4 = 9.0
all_right = (disabled or RunTest(9, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = 10
p1 = 9
p2 = 9
p3 = 8
p4 = 89.0
all_right = (disabled or RunTest(10, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = 10
p1 = 9
p2 = 3
p3 = 6
p4 = 1881.0
all_right = (disabled or RunTest(11, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = 2
p1 = 9
p2 = 1
p3 = 5
p4 = 65.0
all_right = (disabled or RunTest(12, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = 2
p1 = 5
p2 = 1
p3 = 3
p4 = 21.0
all_right = (disabled or RunTest(13, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = 10
p1 = 8
p2 = 7
p3 = 4
p4 = -1.0
all_right = (disabled or RunTest(14, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = 6
p1 = 8
p2 = 1
p3 = 3
p4 = 95.0
all_right = (disabled or RunTest(15, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = 5
p1 = 2
p2 = 1
p3 = 1
p4 = 9.0
all_right = (disabled or RunTest(16, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = 7
p1 = 2
p2 = 1
p3 = 1
p4 = 13.0
all_right = (disabled or RunTest(17, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = 2
p1 = 3
p2 = 1
p3 = 2
p4 = 5.0
all_right = (disabled or RunTest(18, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = 3
p1 = 2
p2 = 0
p3 = 1
p4 = 9.0
all_right = (disabled or RunTest(19, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = 3
p1 = 3
p2 = 1
p3 = 2
p4 = -1.0
all_right = (disabled or RunTest(20, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = 3
p1 = 4
p2 = 2
p3 = 0
p4 = 32.0
all_right = (disabled or RunTest(21, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = 4
p1 = 6
p2 = 2
p3 = 2
p4 = 20.0
all_right = (disabled or RunTest(22, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = 6
p1 = 4
p2 = 1
p3 = 0
p4 = -1.0
all_right = (disabled or RunTest(23, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = 10
p1 = 10
p2 = 7
p3 = 3
p4 = -1.0
all_right = (disabled or RunTest(24, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = 10
p1 = 10
p2 = 9
p3 = 1
p4 = -1.0
all_right = (disabled or RunTest(25, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = 5
p1 = 10
p2 = 4
p3 = 2
p4 = -1.0
all_right = (disabled or RunTest(26, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = 5
p1 = 10
p2 = 1
p3 = 3
p4 = -1.0
all_right = (disabled or RunTest(27, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = 8
p1 = 2
p2 = 2
p3 = 0
p4 = 12.0
all_right = (disabled or RunTest(28, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = 10
p1 = 3
p2 = 8
p3 = 1
p4 = 56.0
all_right = (disabled or RunTest(29, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = 10
p1 = 4
p2 = 2
p3 = 2
p4 = 36.0
all_right = (disabled or RunTest(30, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = 10
p1 = 9
p2 = 5
p3 = 0
p4 = 2025.0
all_right = (disabled or RunTest(31, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = 9
p1 = 10
p2 = 0
p3 = 5
p4 = 2025.0
all_right = (disabled or RunTest(32, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = 3
p1 = 9
p2 = 1
p3 = 7
p4 = 14.0
all_right = (disabled or RunTest(33, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = 8
p1 = 2
p2 = 1
p3 = 0
p4 = -1.0
all_right = (disabled or RunTest(34, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = 10
p1 = 7
p2 = 7
p3 = 1
p4 = 741.0
all_right = (disabled or RunTest(35, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = 4
p1 = 7
p2 = 3
p3 = 6
p4 = 27.0
all_right = (disabled or RunTest(36, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = 10
p1 = 9
p2 = 1
p3 = 1
p4 = 89.0
all_right = (disabled or RunTest(37, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = 5
p1 = 8
p2 = 2
p3 = 5
p4 = 111.0
all_right = (disabled or RunTest(38, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = 8
p1 = 5
p2 = 2
p3 = 4
p4 = 204.0
all_right = (disabled or RunTest(39, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = 8
p1 = 9
p2 = 2
p3 = 1
p4 = 620.0
all_right = (disabled or RunTest(40, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = 8
p1 = 6
p2 = 1
p3 = 4
p4 = -1.0
all_right = (disabled or RunTest(41, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = 6
p1 = 8
p2 = 3
p3 = 0
p4 = -1.0
all_right = (disabled or RunTest(42, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = 8
p1 = 5
p2 = 2
p3 = 3
p4 = 396.0
all_right = (disabled or RunTest(43, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = 4
p1 = 4
p2 = 2
p3 = 2
p4 = 4.0
all_right = (disabled or RunTest(44, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = 5
p1 = 9
p2 = 4
p3 = 8
p4 = 44.0
all_right = (disabled or RunTest(45, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = 9
p1 = 10
p2 = 5
p3 = 3
p4 = 1541.0
all_right = (disabled or RunTest(46, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = 5
p1 = 4
p2 = 3
p3 = 0
p4 = 96.0
all_right = (disabled or RunTest(47, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = 3
p1 = 7
p2 = 1
p3 = 5
p4 = 38.0
all_right = (disabled or RunTest(48, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = 10
p1 = 3
p2 = 9
p3 = 0
p4 = 189.0
all_right = (disabled or RunTest(49, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = 7
p1 = 10
p2 = 0
p3 = 9
p4 = 1029.0
all_right = (disabled or RunTest(50, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = 4
p1 = 8
p2 = 2
p3 = 2
p4 = 12.0
all_right = (disabled or RunTest(51, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = 5
p1 = 7
p2 = 1
p3 = 2
p4 = 304.0
all_right = (disabled or RunTest(52, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = 10
p1 = 6
p2 = 3
p3 = 2
p4 = -1.0
all_right = (disabled or RunTest(53, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 54 -----
disabled = False
p0 = 4
p1 = 5
p2 = 3
p3 = 2
p4 = 91.0
all_right = (disabled or RunTest(54, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 55 -----
disabled = False
p0 = 6
p1 = 9
p2 = 4
p3 = 8
p4 = -1.0
all_right = (disabled or RunTest(55, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 56 -----
disabled = False
p0 = 8
p1 = 9
p2 = 2
p3 = 8
p4 = 1196.0
all_right = (disabled or RunTest(56, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 57 -----
disabled = False
p0 = 8
p1 = 2
p2 = 5
p3 = 0
p4 = -1.0
all_right = (disabled or RunTest(57, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 58 -----
disabled = False
p0 = 9
p1 = 2
p2 = 5
p3 = 0
p4 = 56.0
all_right = (disabled or RunTest(58, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 59 -----
disabled = False
p0 = 2
p1 = 8
p2 = 1
p3 = 6
p4 = -1.0
all_right = (disabled or RunTest(59, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 60 -----
disabled = False
p0 = 7
p1 = 5
p2 = 5
p3 = 4
p4 = 304.0
all_right = (disabled or RunTest(60, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 61 -----
disabled = False
p0 = 5
p1 = 6
p2 = 1
p3 = 5
p4 = 209.0
all_right = (disabled or RunTest(61, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 62 -----
disabled = False
p0 = 5
p1 = 3
p2 = 3
p3 = 0
p4 = 36.0
all_right = (disabled or RunTest(62, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 63 -----
disabled = False
p0 = 4
p1 = 7
p2 = 1
p3 = 0
p4 = 147.0
all_right = (disabled or RunTest(63, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 64 -----
disabled = False
p0 = 4
p1 = 9
p2 = 1
p3 = 1
p4 = 35.0
all_right = (disabled or RunTest(64, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 65 -----
disabled = False
p0 = 9
p1 = 9
p2 = 7
p3 = 2
p4 = -1.0
all_right = (disabled or RunTest(65, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 66 -----
disabled = False
p0 = 5
p1 = 9
p2 = 3
p3 = 5
p4 = 506.0
all_right = (disabled or RunTest(66, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 67 -----
disabled = False
p0 = 5
p1 = 4
p2 = 4
p3 = 0
p4 = 64.0
all_right = (disabled or RunTest(67, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 68 -----
disabled = False
p0 = 7
p1 = 4
p2 = 1
p3 = 3
p4 = 195.0
all_right = (disabled or RunTest(68, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 69 -----
disabled = False
p0 = 4
p1 = 7
p2 = 2
p3 = 0
p4 = 196.0
all_right = (disabled or RunTest(69, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 70 -----
disabled = False
p0 = 10
p1 = 2
p2 = 2
p3 = 0
p4 = 16.0
all_right = (disabled or RunTest(70, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 71 -----
disabled = False
p0 = 4
p1 = 10
p2 = 2
p3 = 3
p4 = -1.0
all_right = (disabled or RunTest(71, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 72 -----
disabled = False
p0 = 5
p1 = 7
p2 = 3
p3 = 6
p4 = 286.0
all_right = (disabled or RunTest(72, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 73 -----
disabled = False
p0 = 9
p1 = 9
p2 = 7
p3 = 1
p4 = -1.0
all_right = (disabled or RunTest(73, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 74 -----
disabled = False
p0 = 5
p1 = 9
p2 = 3
p3 = 3
p4 = 126.0
all_right = (disabled or RunTest(74, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 75 -----
disabled = False
p0 = 5
p1 = 4
p2 = 3
p3 = 1
p4 = 91.0
all_right = (disabled or RunTest(75, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 76 -----
disabled = False
p0 = 2
p1 = 4
p2 = 1
p3 = 3
p4 = 3.0
all_right = (disabled or RunTest(76, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 77 -----
disabled = False
p0 = 7
p1 = 5
p2 = 2
p3 = 2
p4 = 66.0
all_right = (disabled or RunTest(77, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 78 -----
disabled = False
p0 = 6
p1 = 4
p2 = 3
p3 = 0
p4 = -1.0
all_right = (disabled or RunTest(78, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 79 -----
disabled = False
p0 = 5
p1 = 4
p2 = 1
p3 = 1
p4 = 19.0
all_right = (disabled or RunTest(79, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 80 -----
disabled = False
p0 = 2
p1 = 9
p2 = 0
p3 = 7
p4 = 32.0
all_right = (disabled or RunTest(80, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 81 -----
disabled = False
p0 = 9
p1 = 4
p2 = 4
p3 = 3
p4 = 155.0
all_right = (disabled or RunTest(81, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 82 -----
disabled = False
p0 = 6
p1 = 10
p2 = 5
p3 = 4
p4 = -1.0
all_right = (disabled or RunTest(82, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 83 -----
disabled = False
p0 = 2
p1 = 10
p2 = 0
p3 = 9
p4 = -1.0
all_right = (disabled or RunTest(83, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 84 -----
disabled = False
p0 = 9
p1 = 4
p2 = 1
p3 = 3
p4 = 323.0
all_right = (disabled or RunTest(84, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 85 -----
disabled = False
p0 = 6
p1 = 10
p2 = 1
p3 = 4
p4 = -1.0
all_right = (disabled or RunTest(85, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 86 -----
disabled = False
p0 = 10
p1 = 3
p2 = 0
p3 = 2
p4 = 200.0
all_right = (disabled or RunTest(86, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 87 -----
disabled = False
p0 = 3
p1 = 10
p2 = 2
p3 = 0
p4 = 200.0
all_right = (disabled or RunTest(87, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 88 -----
disabled = False
p0 = 7
p1 = 10
p2 = 5
p3 = 1
p4 = 549.0
all_right = (disabled or RunTest(88, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 89 -----
disabled = False
p0 = 4
p1 = 2
p2 = 0
p3 = 1
p4 = -1.0
all_right = (disabled or RunTest(89, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 90 -----
disabled = False
p0 = 5
p1 = 6
p2 = 2
p3 = 5
p4 = 221.0
all_right = (disabled or RunTest(90, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 91 -----
disabled = False
p0 = 7
p1 = 4
p2 = 2
p3 = 1
p4 = 171.0
all_right = (disabled or RunTest(91, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 92 -----
disabled = False
p0 = 10
p1 = 8
p2 = 2
p3 = 5
p4 = -1.0
all_right = (disabled or RunTest(92, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 93 -----
disabled = False
p0 = 10
p1 = 2
p2 = 9
p3 = 1
p4 = 9.0
all_right = (disabled or RunTest(93, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 94 -----
disabled = False
p0 = 9
p1 = 7
p2 = 4
p3 = 5
p4 = 920.0
all_right = (disabled or RunTest(94, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 95 -----
disabled = False
p0 = 7
p1 = 7
p2 = 1
p3 = 5
p4 = -1.0
all_right = (disabled or RunTest(95, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 96 -----
disabled = False
p0 = 10
p1 = 10
p2 = 8
p3 = 9
p4 = -1.0
all_right = (disabled or RunTest(96, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 97 -----
disabled = False
p0 = 10
p1 = 9
p2 = 3
p3 = 4
p4 = 1001.0
all_right = (disabled or RunTest(97, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 98 -----
disabled = False
p0 = 9
p1 = 10
p2 = 1
p3 = 5
p4 = 1925.0
all_right = (disabled or RunTest(98, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 99 -----
disabled = False
p0 = 9
p1 = 7
p2 = 4
p3 = 0
p4 = 686.0
all_right = (disabled or RunTest(99, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 100 -----
disabled = False
p0 = 5
p1 = 2
p2 = 0
p3 = 1
p4 = 25.0
all_right = (disabled or RunTest(100, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 101 -----
disabled = False
p0 = 3
p1 = 3
p2 = 2
p3 = 1
p4 = -1.0
all_right = (disabled or RunTest(101, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 102 -----
disabled = False
p0 = 10
p1 = 9
p2 = 6
p3 = 1
p4 = 2024.0
all_right = (disabled or RunTest(102, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 103 -----
disabled = False
p0 = 10
p1 = 9
p2 = 4
p3 = 8
p4 = 2024.0
all_right = (disabled or RunTest(103, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 104 -----
disabled = False
p0 = 9
p1 = 10
p2 = 4
p3 = 7
p4 = 1541.0
all_right = (disabled or RunTest(104, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 105 -----
disabled = False
p0 = 10
p1 = 9
p2 = 9
p3 = 0
p4 = 729.0
all_right = (disabled or RunTest(105, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 106 -----
disabled = False
p0 = 5
p1 = 7
p2 = 2
p3 = 1
p4 = 286.0
all_right = (disabled or RunTest(106, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 107 -----
disabled = False
p0 = 9
p1 = 5
p2 = 6
p3 = 0
p4 = 450.0
all_right = (disabled or RunTest(107, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 108 -----
disabled = False
p0 = 5
p1 = 8
p2 = 3
p3 = 1
p4 = 231.0
all_right = (disabled or RunTest(108, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 109 -----
disabled = False
p0 = 5
p1 = 8
p2 = 3
p3 = 2
p4 = 396.0
all_right = (disabled or RunTest(109, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 110 -----
disabled = False
p0 = 9
p1 = 3
p2 = 6
p3 = 0
p4 = 18.0
all_right = (disabled or RunTest(110, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 111 -----
disabled = False
p0 = 2
p1 = 10
p2 = 1
p3 = 2
p4 = -1.0
all_right = (disabled or RunTest(111, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 112 -----
disabled = False
p0 = 3
p1 = 10
p2 = 1
p3 = 9
p4 = 209.0
all_right = (disabled or RunTest(112, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 113 -----
disabled = False
p0 = 4
p1 = 3
p2 = 3
p3 = 2
p4 = 11.0
all_right = (disabled or RunTest(113, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 114 -----
disabled = False
p0 = 3
p1 = 8
p2 = 2
p3 = 2
p4 = 44.0
all_right = (disabled or RunTest(114, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 115 -----
disabled = False
p0 = 7
p1 = 7
p2 = 5
p3 = 4
p4 = -1.0
all_right = (disabled or RunTest(115, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 116 -----
disabled = False
p0 = 5
p1 = 5
p2 = 2
p3 = 2
p4 = 6.0
all_right = (disabled or RunTest(116, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 117 -----
disabled = False
p0 = 10
p1 = 10
p2 = 5
p3 = 5
p4 = 25.0
all_right = (disabled or RunTest(117, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 118 -----
disabled = False
p0 = 10
p1 = 10
p2 = 4
p3 = 4
p4 = 24.0
all_right = (disabled or RunTest(118, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 119 -----
disabled = False
p0 = 6
p1 = 2
p2 = 3
p3 = 1
p4 = 9.0
all_right = (disabled or RunTest(119, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 120 -----
disabled = False
p0 = 6
p1 = 3
p2 = 1
p3 = 2
p4 = -1.0
all_right = (disabled or RunTest(120, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 121 -----
disabled = False
p0 = 6
p1 = 7
p2 = 1
p3 = 5
p4 = 437.0
all_right = (disabled or RunTest(121, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 122 -----
disabled = False
p0 = 6
p1 = 10
p2 = 2
p3 = 4
p4 = 224.0
all_right = (disabled or RunTest(122, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 123 -----
disabled = False
p0 = 7
p1 = 3
p2 = 5
p3 = 2
p4 = 80.0
all_right = (disabled or RunTest(123, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 124 -----
disabled = False
p0 = 7
p1 = 9
p2 = 2
p3 = 6
p4 = 612.0
all_right = (disabled or RunTest(124, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 125 -----
disabled = False
p0 = 8
p1 = 4
p2 = 2
p3 = 2
p4 = 12.0
all_right = (disabled or RunTest(125, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 126 -----
disabled = False
p0 = 9
p1 = 3
p2 = 7
p3 = 0
p4 = -1.0
all_right = (disabled or RunTest(126, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 127 -----
disabled = False
p0 = 9
p1 = 8
p2 = 6
p3 = 6
p4 = 396.0
all_right = (disabled or RunTest(127, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 128 -----
disabled = False
p0 = 9
p1 = 6
p2 = 4
p3 = 2
p4 = -1.0
all_right = (disabled or RunTest(128, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 129 -----
disabled = False
p0 = 10
p1 = 10
p2 = 9
p3 = 8
p4 = -1.0
all_right = (disabled or RunTest(129, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 130 -----
disabled = False
p0 = 10
p1 = 9
p2 = 1
p3 = 2
p4 = 869.0
all_right = (disabled or RunTest(130, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 131 -----
disabled = False
p0 = 10
p1 = 10
p2 = 6
p3 = 6
p4 = 24.0
all_right = (disabled or RunTest(131, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 132 -----
disabled = False
p0 = 7
p1 = 10
p2 = 2
p3 = 5
p4 = 325.0
all_right = (disabled or RunTest(132, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 133 -----
disabled = False
p0 = 7
p1 = 10
p2 = 1
p3 = 1
p4 = 69.0
all_right = (disabled or RunTest(133, p0, p1, p2, p3, True, p4) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 134 -----
disabled = False
p0 = 2
p1 = 4
p2 = 0
p3 = 1
p4 = -1.0
all_right = (disabled or RunTest(134, p0, p1, p2, p3, True, p4) ) and all_right
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
