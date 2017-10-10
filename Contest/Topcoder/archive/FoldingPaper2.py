class FoldingPaper2:
    def solve(self, val0, val1, val2):
        return 0


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, p1, p2, hasAnswer, p3):
    obj = FoldingPaper2()
    startTime = time.clock()
    answer = obj.solve(p0, p1, p2)
    endTime = time.clock()
    testTime.append(endTime - startTime)
    res = True
    if hasAnswer:
        res = answer == p3
    if res:
        print(str("Test #") + str(testNum) + ": Passed")
        return res
    print(str("Test #") + str(testNum) + str(":"))
    print(("[") + str(p0) + str(",") + str(p1) + str(",") + str(p2) + str("]"))
    if (hasAnswer):
        print(str("Expected:"))
        print(str(p3))

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
p0 = 5
p1 = 3
p2 = 12
p3 = 1
all_right = (disabled or RunTest(0, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = 2
p1 = 2
p2 = 3
p3 = -1
all_right = (disabled or RunTest(1, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = 4
p1 = 4
p2 = 1
p3 = 4
all_right = (disabled or RunTest(2, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = 127
p1 = 129
p2 = 72
p3 = 8
all_right = (disabled or RunTest(3, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = 1
p1 = 100000
p2 = 100000
p3 = 0
all_right = (disabled or RunTest(4, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = 1
p1 = 1
p2 = 2
p3 = -1
all_right = (disabled or RunTest(5, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = 1000000000
p1 = 1000000000
p2 = 100000
p3 = 44
all_right = (disabled or RunTest(6, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = 1000000000
p1 = 1000000000
p2 = 1
p3 = 60
all_right = (disabled or RunTest(7, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = 10000
p1 = 10000
p2 = 9999
p3 = 14
all_right = (disabled or RunTest(8, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = 101
p1 = 103
p2 = 10403
p3 = 0
all_right = (disabled or RunTest(9, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = 103
p1 = 101
p2 = 10403
p3 = 0
all_right = (disabled or RunTest(10, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = 105
p1 = 100
p2 = 10403
p3 = -1
all_right = (disabled or RunTest(11, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = 103
p1 = 201
p2 = 10403
p3 = 1
all_right = (disabled or RunTest(12, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = 207
p1 = 202
p2 = 10403
p3 = 3
all_right = (disabled or RunTest(13, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = 207
p1 = 206
p2 = 10403
p3 = 3
all_right = (disabled or RunTest(14, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = 206
p1 = 207
p2 = 10403
p3 = 3
all_right = (disabled or RunTest(15, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = 6465
p1 = 103
p2 = 10403
p3 = 7
all_right = (disabled or RunTest(16, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = 9999
p1 = 9999
p2 = 10000
p3 = 14
all_right = (disabled or RunTest(17, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = 84
p1 = 286
p2 = 3003
p3 = 3
all_right = (disabled or RunTest(18, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = 8
p1 = 8
p2 = 35
p3 = 2
all_right = (disabled or RunTest(19, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = 7
p1 = 7
p2 = 35
p3 = 1
all_right = (disabled or RunTest(20, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = 6
p1 = 6
p2 = 35
p3 = -1
all_right = (disabled or RunTest(21, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = 16
p1 = 16
p2 = 128
p3 = 1
all_right = (disabled or RunTest(22, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = 8
p1 = 8
p2 = 128
p3 = -1
all_right = (disabled or RunTest(23, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = 1
p1 = 100000
p2 = 99999
p3 = 1
all_right = (disabled or RunTest(24, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = 3
p1 = 100000
p2 = 99999
p3 = 2
all_right = (disabled or RunTest(25, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = 100000
p1 = 3
p2 = 99999
p3 = 2
all_right = (disabled or RunTest(26, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = 4
p1 = 74
p2 = 222
p3 = 1
all_right = (disabled or RunTest(27, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = 4
p1 = 75
p2 = 222
p3 = 2
all_right = (disabled or RunTest(28, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = 4
p1 = 149
p2 = 222
p3 = 2
all_right = (disabled or RunTest(29, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = 4
p1 = 110
p2 = 222
p3 = 2
all_right = (disabled or RunTest(30, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = 4
p1 = 111
p2 = 222
p3 = 1
all_right = (disabled or RunTest(31, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = 3
p1 = 148
p2 = 222
p3 = 1
all_right = (disabled or RunTest(32, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = 3
p1 = 147
p2 = 222
p3 = 1
all_right = (disabled or RunTest(33, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = 3
p1 = 149
p2 = 222
p3 = 2
all_right = (disabled or RunTest(34, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = 234624
p1 = 35235
p2 = 108
p3 = 27
all_right = (disabled or RunTest(35, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = 657356
p1 = 54542
p2 = 108
p3 = 29
all_right = (disabled or RunTest(36, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = 30
p1 = 29
p2 = 225
p3 = 2
all_right = (disabled or RunTest(37, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = 730
p1 = 12
p2 = 729
p3 = 4
all_right = (disabled or RunTest(38, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = 100000
p1 = 20056
p2 = 208
p3 = 24
all_right = (disabled or RunTest(39, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = 75
p1 = 279
p2 = 225
p3 = 7
all_right = (disabled or RunTest(40, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = 775
p1 = 279
p2 = 225
p3 = 10
all_right = (disabled or RunTest(41, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = 1
p1 = 20
p2 = 5
p3 = 2
all_right = (disabled or RunTest(42, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = 1
p1 = 11
p2 = 5
p3 = 2
all_right = (disabled or RunTest(43, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = 1
p1 = 21
p2 = 5
p3 = 3
all_right = (disabled or RunTest(44, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = 9
p1 = 3
p2 = 12
p3 = 2
all_right = (disabled or RunTest(45, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = 1000000000
p1 = 1000000000
p2 = 12
p3 = 57
all_right = (disabled or RunTest(46, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = 1000000000
p1 = 3
p2 = 100000
p3 = 16
all_right = (disabled or RunTest(47, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = 1000000000
p1 = 1000000000
p2 = 3
p3 = 59
all_right = (disabled or RunTest(48, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = 99
p1 = 999
p2 = 23
p3 = 13
all_right = (disabled or RunTest(49, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = 10
p1 = 10
p2 = 6
p3 = 5
all_right = (disabled or RunTest(50, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = 15
p1 = 39
p2 = 133
p3 = 4
all_right = (disabled or RunTest(51, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = 1000000000
p1 = 1000000000
p2 = 99999
p3 = 44
all_right = (disabled or RunTest(52, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = 1247
p1 = 12
p2 = 13299
p3 = 2
all_right = (disabled or RunTest(53, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 54 -----
disabled = False
p0 = 7
p1 = 7
p2 = 9
p3 = 4
all_right = (disabled or RunTest(54, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 55 -----
disabled = False
p0 = 864682
p1 = 824
p2 = 100000
p3 = 14
all_right = (disabled or RunTest(55, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 56 -----
disabled = False
p0 = 16
p1 = 5
p2 = 20
p3 = 2
all_right = (disabled or RunTest(56, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 57 -----
disabled = False
p0 = 999999999
p1 = 999999999
p2 = 55566
p3 = 45
all_right = (disabled or RunTest(57, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 58 -----
disabled = False
p0 = 245344672
p1 = 45632342
p2 = 56322
p3 = 38
all_right = (disabled or RunTest(58, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 59 -----
disabled = False
p0 = 50
p1 = 20000
p2 = 5678
p3 = 8
all_right = (disabled or RunTest(59, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 60 -----
disabled = False
p0 = 7
p1 = 7
p2 = 36
p3 = 2
all_right = (disabled or RunTest(60, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 61 -----
disabled = False
p0 = 2
p1 = 10000000
p2 = 2
p3 = 24
all_right = (disabled or RunTest(61, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 62 -----
disabled = False
p0 = 4
p1 = 4
p2 = 2
p3 = 3
all_right = (disabled or RunTest(62, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 63 -----
disabled = False
p0 = 1
p1 = 1
p2 = 8
p3 = -1
all_right = (disabled or RunTest(63, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 64 -----
disabled = False
p0 = 1000000000
p1 = 99935080
p2 = 4096
p3 = 45
all_right = (disabled or RunTest(64, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 65 -----
disabled = False
p0 = 99
p1 = 195
p2 = 35
p3 = 10
all_right = (disabled or RunTest(65, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 66 -----
disabled = False
p0 = 3
p1 = 16
p2 = 12
p3 = 2
all_right = (disabled or RunTest(66, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 67 -----
disabled = False
p0 = 100000
p1 = 1
p2 = 100000
p3 = 0
all_right = (disabled or RunTest(67, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 68 -----
disabled = False
p0 = 1000000
p1 = 1000000
p2 = 1
p3 = 40
all_right = (disabled or RunTest(68, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 69 -----
disabled = False
p0 = 100000
p1 = 10000000
p2 = 1
p3 = 41
all_right = (disabled or RunTest(69, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 70 -----
disabled = False
p0 = 3
p1 = 8
p2 = 16
p3 = 1
all_right = (disabled or RunTest(70, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 71 -----
disabled = False
p0 = 3
p1 = 16
p2 = 6
p3 = 3
all_right = (disabled or RunTest(71, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 72 -----
disabled = False
p0 = 1000000000
p1 = 747172737
p2 = 1
p3 = 60
all_right = (disabled or RunTest(72, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 73 -----
disabled = False
p0 = 8
p1 = 8
p2 = 49
p3 = 2
all_right = (disabled or RunTest(73, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 74 -----
disabled = False
p0 = 156
p1 = 95
p2 = 35
p3 = 9
all_right = (disabled or RunTest(74, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 75 -----
disabled = False
p0 = 1232143
p1 = 99643
p2 = 23
p3 = 33
all_right = (disabled or RunTest(75, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 76 -----
disabled = False
p0 = 536870912
p1 = 536870912
p2 = 2
p3 = 57
all_right = (disabled or RunTest(76, p0, p1, p2, True, p3) ) and all_right
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
