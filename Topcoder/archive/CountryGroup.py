class CountryGroup:
    def solve(self, a):
        a = list(a)
        t = [[i]*i for i in range(1, 101)]
        sumx =0
        while a:
            i0 = a[0]
            if a[:i0] in t:
                a = a[i0:]
                sumx += 1
            else:
                return -1
        return sumx


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, hasAnswer, p1):
    obj = CountryGroup()
    startTime = time.clock()
    answer = obj.solve(p0)
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
p0 = (2, 2, 3, 3, 3)
p1 = 2
all_right = (disabled or RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = (1, 1, 1, 1, 1)
p1 = 5
all_right = (disabled or RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = (3, 3)
p1 = -1
all_right = (disabled or RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = (4, 4, 4, 4, 1, 1, 2, 2, 3, 3, 3)
p1 = 5
all_right = (disabled or RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = (2, 1, 2, 2, 1, 2)
p1 = -1
all_right = (disabled or RunTest(4, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = (100,)
p1 = -1
all_right = (disabled or RunTest(5, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = (1,)
p1 = 1
all_right = (disabled or RunTest(6, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = (2,)
p1 = -1
all_right = (disabled or RunTest(7, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = (2, 2, 2, 2, 4, 4, 4, 4)
p1 = 3
all_right = (disabled or RunTest(8, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = (5, 4, 3, 2, 1)
p1 = -1
all_right = (disabled or RunTest(9, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = (1, 2, 2, 1)
p1 = 3
all_right = (disabled or RunTest(10, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = (3, 1, 3, 3)
p1 = -1
all_right = (disabled or RunTest(11, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = (7, 7, 7, 7, 7, 7, 7, 7)
p1 = -1
all_right = (disabled or RunTest(12, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = (1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 3, 3, 3, 1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 1, 1, 1)
p1 = 25
all_right = (disabled or RunTest(13, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = (3, 2, 2)
p1 = -1
all_right = (disabled or RunTest(14, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = (1, 2, 3, 4, 5)
p1 = -1
all_right = (disabled or RunTest(15, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
p1 = 100
all_right = (disabled or RunTest(16, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
p1 = 10
all_right = (disabled or RunTest(17, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = (99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99)
p1 = -1
all_right = (disabled or RunTest(18, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = (49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51)
p1 = 2
all_right = (disabled or RunTest(19, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = (2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1, 4, 4, 4, 4, 4, 4, 4, 4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 4, 4, 4, 4, 2, 2, 1, 3, 3, 3, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 3, 3, 3, 4, 4, 4, 4)
p1 = 31
all_right = (disabled or RunTest(20, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = (5, 5, 5, 5, 5, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 3, 3, 3, 1, 4, 4, 4, 4, 1, 1, 1, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 1, 5, 5, 5, 5, 5, 2, 2, 5, 5, 5, 5, 5, 3, 3, 3, 1)
p1 = 37
all_right = (disabled or RunTest(21, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = (2, 2, 5, 5, 5, 5, 5, 2, 2, 3, 3, 3, 1, 5, 5, 5, 5, 5, 1, 2, 2, 2, 2, 3, 3, 3, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 1, 3, 3, 3, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3)
p1 = 32
all_right = (disabled or RunTest(22, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = (1, 5, 5, 5, 5, 5, 1, 3, 3, 3, 5, 5, 5, 5, 5, 2, 2, 5, 5, 5, 5, 5, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
p1 = 31
all_right = (disabled or RunTest(23, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = (3, 3, 3, 4, 4, 4, 4, 1, 2, 2, 1, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 1, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 1, 5, 5, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 1, 1, 4, 4, 4, 4, 2, 2, 3, 3, 3, 2, 2, 4, 4, 4, 4, 2, 2, 2, 2, 5, 5, 5, 5, 5, 2, 2, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
p1 = 36
all_right = (disabled or RunTest(24, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = (3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 2, 2, 1, 4, 4, 4, 4, 2, 2, 2, 2, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 5, 5, 5, 5, 5, 2, 2, 2, 2, 1, 1, 4, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 2, 2, 1, 2, 2)
p1 = 40
all_right = (disabled or RunTest(25, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = (2, 2, 5, 5, 5, 5, 5, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 4, 4, 4, 4, 3, 3, 3, 1, 3, 3, 3, 2, 2, 3, 3, 3, 4, 4, 4, 4, 2, 2, 2, 2, 1, 2, 2, 5, 5, 5, 5, 5, 2, 2, 1, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 4, 4, 4, 4, 2, 2, 1)
p1 = 33
all_right = (disabled or RunTest(26, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = (5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 3, 3, 1, 2, 2, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 3, 3, 3, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 3, 3, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2)
p1 = 28
all_right = (disabled or RunTest(27, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = (3, 3, 3, 2, 2, 2, 2, 1, 5, 5, 5, 5, 5, 1, 1, 1, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 1, 3, 3, 3, 1, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 3, 3, 3, 5, 5, 5, 5, 5, 2, 2, 5, 5, 5, 5, 5)
p1 = 33
all_right = (disabled or RunTest(28, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = (5, 5, 5, 5, 5, 4, 4, 4, 4, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 1, 3, 3, 3, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 3, 3, 3, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 1, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 5, 5, 5, 5, 5, 2, 2, 1, 5, 5, 5, 5, 5)
p1 = 30
all_right = (disabled or RunTest(29, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = (2, 2, 3, 3, 3, 2, 2, 3, 3, 3, 2, 2, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 3, 3, 3, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 2, 2, 1, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 1, 4, 4, 4, 4, 2, 2, 2, 2, 5, 5, 5, 5, 5, 1, 2, 2, 2, 2, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4)
p1 = 35
all_right = (disabled or RunTest(30, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 1, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 4, 4, 4, 4, 2, 2, 5, 5, 5, 5, 5, 1, 1, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 1, 1, 1, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 2, 2, 3, 3, 3, 2, 2, 3, 3, 3, 1, 3, 3, 3)
p1 = 34
all_right = (disabled or RunTest(31, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = (3, 3, 3, 5, 5, 5, 5, 5, 1, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 1, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 4, 4, 4, 4, 1, 2, 2, 1, 3, 3, 3, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 2, 1, 1, 4, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4)
p1 = 35
all_right = (disabled or RunTest(32, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = (3, 3, 3, 3, 3, 3, 1, 2, 2, 4, 4, 4, 4, 3, 3, 3, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 3, 3, 3, 5, 5, 5, 5, 5, 2, 2, 1, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 5, 5, 5, 5, 5, 3, 3, 3, 4, 4, 4, 4, 1, 1, 2, 2, 1, 1, 5, 5, 5, 5, 5, 1, 1)
p1 = 34
all_right = (disabled or RunTest(33, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = (5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 1, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 3, 3, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 4, 4, 4, 4, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 1, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 1)
p1 = 29
all_right = (disabled or RunTest(34, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = (2, 2, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 4, 4, 4, 4, 3, 3, 3, 5, 5, 5, 5, 5, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4)
p1 = 31
all_right = (disabled or RunTest(35, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = (2, 2, 2, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 1, 4, 4, 4, 4, 5, 5, 5, 5, 5, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 1, 1, 5, 5, 5, 5, 5)
p1 = 30
all_right = (disabled or RunTest(36, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = (5, 5, 5, 5, 5, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 3, 3, 3, 1, 3, 3, 3, 2, 2, 1, 5, 5, 5, 5, 5, 2, 2, 3, 3, 3, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 1, 2, 2, 1, 5, 5, 5, 5, 5, 2, 2, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1)
p1 = 32
all_right = (disabled or RunTest(37, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = (4, 4, 4, 4, 2, 2, 1, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 2, 2, 5, 5, 5, 5, 5, 1, 2, 2, 2, 2, 5, 5, 5, 5, 5, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 1, 3, 3, 3, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4)
p1 = 37
all_right = (disabled or RunTest(38, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = (3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 1, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 1, 4, 4, 4, 4, 1, 3, 3, 3, 1, 2, 2, 4, 4, 4, 4, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 1, 3, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 1, 3, 3, 3, 2, 2)
p1 = 37
all_right = (disabled or RunTest(39, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = (5, 5, 5, 5, 5, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 6, 6, 6, 6, 6, 6, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16)
p1 = 7
all_right = (disabled or RunTest(40, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = (3, 3, 3, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 1, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 2)
p1 = 12
all_right = (disabled or RunTest(41, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = (1, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 1, 5, 5, 5, 5, 5, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 2, 2, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 6, 6, 6, 6, 6, 6, 1)
p1 = 12
all_right = (disabled or RunTest(42, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 2, 2, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 1, 5, 5, 5, 5, 5, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31)
p1 = 7
all_right = (disabled or RunTest(43, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = (7, 7, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 7, 7, 7, 7, 7, 7, 7, 3, 3, 3, 1, 7, 7, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 5, 5, 5, 5, 5)
p1 = 13
all_right = (disabled or RunTest(44, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = (47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 5, 5, 5, 5, 5, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 2, 2)
p1 = 6
all_right = (disabled or RunTest(45, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = (2, 2, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4, 4, 4, 4, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 2, 2, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22)
p1 = 8
all_right = (disabled or RunTest(46, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = (25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 2, 2, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 8, 8, 8, 8, 8, 8, 8, 8)
p1 = 6
all_right = (disabled or RunTest(47, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = (4, 4, 4, 4, 1, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 3, 3, 3, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 2, 2, 2, 2)
p1 = 11
all_right = (disabled or RunTest(48, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = (9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 2, 2, 1, 2, 2, 2, 2, 4, 4, 4, 4, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 1, 1)
p1 = 17
all_right = (disabled or RunTest(49, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = (4, 4, 4, 4, 4, 4, 4, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 3, 3, 3, 1, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 1)
p1 = 10
all_right = (disabled or RunTest(50, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = (2, 2, 5, 5, 5, 5, 5, 2, 2, 1, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 2, 2, 5, 5, 5, 5, 5, 2, 2, 4, 4, 4, 4, 2, 2, 1, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 4, 4, 4, 4)
p1 = 18
all_right = (disabled or RunTest(51, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = (3, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 2, 2, 7, 7, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 3, 3, 3)
p1 = 15
all_right = (disabled or RunTest(52, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = (1, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 3, 3, 3, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 1, 5, 5, 5, 5, 5, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15)
p1 = 13
all_right = (disabled or RunTest(53, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 54 -----
disabled = False
p0 = (3, 3, 3, 1, 2, 2, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 3, 3, 3, 5, 5, 5, 5, 5, 1, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 2, 2, 4, 4, 4, 4, 1)
p1 = 14
all_right = (disabled or RunTest(54, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 55 -----
disabled = False
p0 = (5, 5, 5, 5, 5, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 2, 2, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 5, 5, 5, 5, 5, 2, 2, 2, 2, 3, 3, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13)
p1 = 9
all_right = (disabled or RunTest(55, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 56 -----
disabled = False
p0 = (3, 3, 3, 3, 3, 3, 1, 1, 1, 4, 4, 4, 4, 1, 2, 2, 1, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 1, 2, 2, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 2, 2, 2)
p1 = 18
all_right = (disabled or RunTest(56, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 57 -----
disabled = False
p0 = (1, 1, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 4, 4, 4, 7, 7, 7, 7, 7, 7, 7, 4, 4, 4, 4, 2, 1, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 3, 3, 3, 5, 5, 5, 5, 5)
p1 = -1
all_right = (disabled or RunTest(57, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 58 -----
disabled = False
p0 = (8, 8, 8, 8, 8, 8, 8, 8, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 2, 2, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 4, 4, 4, 4, 7, 7, 7, 7, 7, 7, 7, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13)
p1 = 8
all_right = (disabled or RunTest(58, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 59 -----
disabled = False
p0 = (3, 3, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 2, 2, 4, 4, 4, 4, 2, 2, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 5, 5, 5, 5, 5, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 7, 7, 7, 7, 7, 7, 7, 4, 4, 4, 4, 5, 5, 5, 5, 5, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 2, 2)
p1 = 20
all_right = (disabled or RunTest(59, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 60 -----
disabled = False
p0 = (100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100)
p1 = -1
all_right = (disabled or RunTest(60, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 61 -----
disabled = False
p0 = (100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100)
p1 = 1
all_right = (disabled or RunTest(61, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 62 -----
disabled = False
p0 = (4, 4, 4, 4, 1, 1, 2, 2, 3, 3, 3)
p1 = 5
all_right = (disabled or RunTest(62, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 63 -----
disabled = False
p0 = (2, 1)
p1 = -1
all_right = (disabled or RunTest(63, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 64 -----
disabled = False
p0 = (2, 2, 1, 1, 3, 3, 3, 2, 2)
p1 = 5
all_right = (disabled or RunTest(64, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 65 -----
disabled = False
p0 = (2, 1, 1)
p1 = -1
all_right = (disabled or RunTest(65, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 66 -----
disabled = False
p0 = (3, 3, 3, 1, 3, 3, 3)
p1 = 3
all_right = (disabled or RunTest(66, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 67 -----
disabled = False
p0 = (3, 1, 3)
p1 = -1
all_right = (disabled or RunTest(67, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 68 -----
disabled = False
p0 = (2, 2, 2, 2)
p1 = 2
all_right = (disabled or RunTest(68, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 69 -----
disabled = False
p0 = (3, 3)
p1 = -1
all_right = (disabled or RunTest(69, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 70 -----
disabled = False
p0 = (1, 2)
p1 = -1
all_right = (disabled or RunTest(70, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 71 -----
disabled = False
p0 = (1, 2, 2, 2)
p1 = -1
all_right = (disabled or RunTest(71, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 72 -----
disabled = False
p0 = (3, 3, 3, 3, 3, 3)
p1 = 2
all_right = (disabled or RunTest(72, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 73 -----
disabled = False
p0 = (2, 2, 2)
p1 = -1
all_right = (disabled or RunTest(73, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 74 -----
disabled = False
p0 = (2,)
p1 = -1
all_right = (disabled or RunTest(74, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 75 -----
disabled = False
p0 = (2, 2, 3, 3, 3)
p1 = 2
all_right = (disabled or RunTest(75, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 76 -----
disabled = False
p0 = (4, 3, 4, 4)
p1 = -1
all_right = (disabled or RunTest(76, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 77 -----
disabled = False
p0 = (2, 1, 2)
p1 = -1
all_right = (disabled or RunTest(77, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 78 -----
disabled = False
p0 = (2, 3)
p1 = -1
all_right = (disabled or RunTest(78, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 79 -----
disabled = False
p0 = (4, 1, 1, 4, 1, 1)
p1 = -1
all_right = (disabled or RunTest(79, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 80 -----
disabled = False
p0 = (4, 4, 4, 3)
p1 = -1
all_right = (disabled or RunTest(80, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 81 -----
disabled = False
p0 = (2, 1, 2, 2, 1, 1)
p1 = -1
all_right = (disabled or RunTest(81, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 82 -----
disabled = False
p0 = (3, 1, 2, 3, 2, 3, 1)
p1 = -1
all_right = (disabled or RunTest(82, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 83 -----
disabled = False
p0 = (2, 2, 1, 2, 2)
p1 = 3
all_right = (disabled or RunTest(83, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 84 -----
disabled = False
p0 = (1,)
p1 = 1
all_right = (disabled or RunTest(84, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 85 -----
disabled = False
p0 = (1, 2, 2, 3, 2, 3, 3, 2)
p1 = -1
all_right = (disabled or RunTest(85, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 86 -----
disabled = False
p0 = (1, 2, 2, 1)
p1 = 3
all_right = (disabled or RunTest(86, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 87 -----
disabled = False
p0 = (2, 1, 2, 1)
p1 = -1
all_right = (disabled or RunTest(87, p0, True, p1) ) and all_right
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
