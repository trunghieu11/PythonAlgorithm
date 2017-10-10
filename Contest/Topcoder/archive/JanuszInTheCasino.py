class JanuszInTheCasino:
    def findProbability(self, val0, val1, val2):
        return 0


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, p1, p2, hasAnswer, p3):
    obj = JanuszInTheCasino()
    startTime = time.clock()
    answer = obj.findProbability(p0, p1, p2)
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
p0 = 3
p1 = 2
p2 = 2
p3 = 0.75
all_right = (disabled or RunTest(0, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = 1
p1 = 3
p2 = 3
p3 = 0.2962962962962962
all_right = (disabled or RunTest(1, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = 4
p1 = 3
p2 = 2
p3 = 1.0
all_right = (disabled or RunTest(2, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = 5
p1 = 4
p2 = 5
p3 = 0.87109375
all_right = (disabled or RunTest(3, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = 1000000000000
p1 = 2
p2 = 40
p3 = 0.9094947017729282
all_right = (disabled or RunTest(4, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = 2
p1 = 10
p2 = 50
p3 = 0.010293277937713185
all_right = (disabled or RunTest(5, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = 4324
p1 = 3
p2 = 25
p3 = 0.16981540046618473
all_right = (disabled or RunTest(6, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = 7
p1 = 4
p2 = 5
p3 = 0.982421875
all_right = (disabled or RunTest(7, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = 8
p1 = 4
p2 = 5
p3 = 1.0
all_right = (disabled or RunTest(8, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = 1073741824
p1 = 2
p2 = 30
p3 = 1.0
all_right = (disabled or RunTest(9, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = 1073640803
p1 = 2
p2 = 30
p3 = 0.9999059168621898
all_right = (disabled or RunTest(10, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = 21
p1 = 21
p2 = 42
p3 = 0.9699964585463249
all_right = (disabled or RunTest(11, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = 23323233
p1 = 3
p2 = 45
p3 = 0.2724504209732145
all_right = (disabled or RunTest(12, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = 534545
p1 = 4
p2 = 50
p3 = 0.2901849427392484
all_right = (disabled or RunTest(13, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = 432545123543
p1 = 2
p2 = 45
p3 = 0.012293671817445784
all_right = (disabled or RunTest(14, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = 323432541
p1 = 3
p2 = 50
p3 = 0.4806697202565555
all_right = (disabled or RunTest(15, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = 10
p1 = 41
p2 = 47
p3 = 0.9827463407427732
all_right = (disabled or RunTest(16, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = 10
p1 = 5
p2 = 50
p3 = 1.4272436512995996E-4
all_right = (disabled or RunTest(17, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = 45
p1 = 17
p2 = 30
p3 = 0.9999999972560882
all_right = (disabled or RunTest(18, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = 564656
p1 = 3
p2 = 35
p3 = 0.37472411790163795
all_right = (disabled or RunTest(19, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = 9
p1 = 28
p2 = 43
p3 = 0.8970519842195317
all_right = (disabled or RunTest(20, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = 5
p1 = 14
p2 = 47
p3 = 0.146546252339407
all_right = (disabled or RunTest(21, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = 3
p1 = 50
p2 = 50
p3 = 0.7481823862559633
all_right = (disabled or RunTest(22, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = 45
p1 = 8
p2 = 29
p3 = 0.6868117579367694
all_right = (disabled or RunTest(23, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = 2323
p1 = 2
p2 = 15
p3 = 0.070892333984375
all_right = (disabled or RunTest(24, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = 1000
p1 = 6
p2 = 45
p3 = 0.25763800991541025
all_right = (disabled or RunTest(25, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = 7
p1 = 41
p2 = 43
p3 = 0.9566256685135859
all_right = (disabled or RunTest(26, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = 10
p1 = 26
p2 = 35
p3 = 0.9611832973858667
all_right = (disabled or RunTest(27, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = 23
p1 = 4
p2 = 27
p3 = 0.009732852154560212
all_right = (disabled or RunTest(28, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = 4
p1 = 15
p2 = 3
p3 = 1.0
all_right = (disabled or RunTest(29, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = 32300032
p1 = 5
p2 = 40
p3 = 1.0
all_right = (disabled or RunTest(30, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = 232876324
p1 = 3
p2 = 48
p3 = 0.7231326905540486
all_right = (disabled or RunTest(31, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = 34254312343
p1 = 3
p2 = 45
p3 = 1.0
all_right = (disabled or RunTest(32, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = 455666434444
p1 = 47
p2 = 49
p3 = 0.9999999999999861
all_right = (disabled or RunTest(33, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = 455000654666
p1 = 42
p2 = 50
p3 = 1.0000000000000016
all_right = (disabled or RunTest(34, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = 1072240003
p1 = 2
p2 = 30
p3 = 0.9986013201996684
all_right = (disabled or RunTest(35, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = 1011100000
p1 = 3
p2 = 50
p3 = 0.9989955665603316
all_right = (disabled or RunTest(36, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = 77
p1 = 5
p2 = 50
p3 = 0.0010989371304622444
all_right = (disabled or RunTest(37, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = 100000000000
p1 = 50
p2 = 50
p3 = 0.9999999999999993
all_right = (disabled or RunTest(38, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = 100000000
p1 = 3
p2 = 40
p3 = 1.0
all_right = (disabled or RunTest(39, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = 1000000000000
p1 = 50
p2 = 50
p3 = 0.9999999999999949
all_right = (disabled or RunTest(40, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = 10
p1 = 5
p2 = 1
p3 = 1.0
all_right = (disabled or RunTest(41, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = 100000000000
p1 = 21
p2 = 50
p3 = 0.9999999999999998
all_right = (disabled or RunTest(42, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = 1000000000
p1 = 50
p2 = 50
p3 = 1.0
all_right = (disabled or RunTest(43, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = 1000000000000
p1 = 10
p2 = 50
p3 = 0.9999999999999993
all_right = (disabled or RunTest(44, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = 1000000000000
p1 = 50
p2 = 49
p3 = 0.9999999999999951
all_right = (disabled or RunTest(45, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = 99999999999
p1 = 50
p2 = 50
p3 = 0.9999999999999993
all_right = (disabled or RunTest(46, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = 10000000000
p1 = 50
p2 = 50
p3 = 1.000000000000024
all_right = (disabled or RunTest(47, p0, p1, p2, True, p3) ) and all_right
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
