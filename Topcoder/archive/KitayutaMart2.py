class KitayutaMart2:
    def numBought(self, K, T):
        T //= K
        ans = 0
        while T > 0:
          T //= 2
          ans += 1
        return ans


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, p1, hasAnswer, p2):
    obj = KitayutaMart2()
    startTime = time.clock()
    answer = obj.numBought(p0, p1)
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
p0 = 100
p1 = 100
p2 = 1
all_right = (disabled or RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = 100
p1 = 300
p2 = 2
all_right = (disabled or RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = 150
p1 = 1050
p2 = 3
all_right = (disabled or RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = 160
p1 = 163680
p2 = 10
all_right = (disabled or RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = 80
p1 = 80
p2 = 1
all_right = (disabled or RunTest(4, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = 125
p1 = 125
p2 = 1
all_right = (disabled or RunTest(5, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = 129
p1 = 129
p2 = 1
all_right = (disabled or RunTest(6, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = 139
p1 = 139
p2 = 1
all_right = (disabled or RunTest(7, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = 157
p1 = 157
p2 = 1
all_right = (disabled or RunTest(8, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = 83
p1 = 249
p2 = 2
all_right = (disabled or RunTest(9, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = 86
p1 = 258
p2 = 2
all_right = (disabled or RunTest(10, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = 106
p1 = 318
p2 = 2
all_right = (disabled or RunTest(11, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = 112
p1 = 336
p2 = 2
all_right = (disabled or RunTest(12, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = 114
p1 = 342
p2 = 2
all_right = (disabled or RunTest(13, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = 85
p1 = 595
p2 = 3
all_right = (disabled or RunTest(14, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = 108
p1 = 756
p2 = 3
all_right = (disabled or RunTest(15, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = 138
p1 = 966
p2 = 3
all_right = (disabled or RunTest(16, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = 155
p1 = 1085
p2 = 3
all_right = (disabled or RunTest(17, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = 158
p1 = 1106
p2 = 3
all_right = (disabled or RunTest(18, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = 83
p1 = 1245
p2 = 4
all_right = (disabled or RunTest(19, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = 87
p1 = 1305
p2 = 4
all_right = (disabled or RunTest(20, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = 98
p1 = 1470
p2 = 4
all_right = (disabled or RunTest(21, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = 110
p1 = 1650
p2 = 4
all_right = (disabled or RunTest(22, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = 157
p1 = 2355
p2 = 4
all_right = (disabled or RunTest(23, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = 116
p1 = 3596
p2 = 5
all_right = (disabled or RunTest(24, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = 119
p1 = 3689
p2 = 5
all_right = (disabled or RunTest(25, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = 138
p1 = 4278
p2 = 5
all_right = (disabled or RunTest(26, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = 154
p1 = 4774
p2 = 5
all_right = (disabled or RunTest(27, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = 158
p1 = 4898
p2 = 5
all_right = (disabled or RunTest(28, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = 94
p1 = 5922
p2 = 6
all_right = (disabled or RunTest(29, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = 141
p1 = 8883
p2 = 6
all_right = (disabled or RunTest(30, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = 143
p1 = 9009
p2 = 6
all_right = (disabled or RunTest(31, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = 145
p1 = 9135
p2 = 6
all_right = (disabled or RunTest(32, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = 151
p1 = 9513
p2 = 6
all_right = (disabled or RunTest(33, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = 81
p1 = 10287
p2 = 7
all_right = (disabled or RunTest(34, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = 82
p1 = 10414
p2 = 7
all_right = (disabled or RunTest(35, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = 92
p1 = 11684
p2 = 7
all_right = (disabled or RunTest(36, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = 130
p1 = 16510
p2 = 7
all_right = (disabled or RunTest(37, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = 160
p1 = 20320
p2 = 7
all_right = (disabled or RunTest(38, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = 106
p1 = 27030
p2 = 8
all_right = (disabled or RunTest(39, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = 119
p1 = 30345
p2 = 8
all_right = (disabled or RunTest(40, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = 127
p1 = 32385
p2 = 8
all_right = (disabled or RunTest(41, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = 157
p1 = 40035
p2 = 8
all_right = (disabled or RunTest(42, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = 159
p1 = 40545
p2 = 8
all_right = (disabled or RunTest(43, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = 80
p1 = 40880
p2 = 9
all_right = (disabled or RunTest(44, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = 82
p1 = 41902
p2 = 9
all_right = (disabled or RunTest(45, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = 120
p1 = 61320
p2 = 9
all_right = (disabled or RunTest(46, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = 155
p1 = 79205
p2 = 9
all_right = (disabled or RunTest(47, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = 158
p1 = 80738
p2 = 9
all_right = (disabled or RunTest(48, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = 83
p1 = 84909
p2 = 10
all_right = (disabled or RunTest(49, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = 91
p1 = 93093
p2 = 10
all_right = (disabled or RunTest(50, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = 93
p1 = 95139
p2 = 10
all_right = (disabled or RunTest(51, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = 108
p1 = 110484
p2 = 10
all_right = (disabled or RunTest(52, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = 110
p1 = 112530
p2 = 10
all_right = (disabled or RunTest(53, p0, p1, True, p2) ) and all_right
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
