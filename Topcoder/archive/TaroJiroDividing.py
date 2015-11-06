class TaroJiroDividing:
    def getNumber(self, A, B):
        l1 = [A]
        l2 = [B]
        while A % 2 == 0:
            A = A // 2
            l1.append(A)
        while B%2 == 0:
            B = B // 2
            l2.append(B)
        return len(set(l1).intersection(set(l2)))


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, p1, hasAnswer, p2):
    obj = TaroJiroDividing()
    startTime = time.clock()
    answer = obj.getNumber(p0, p1)
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
p0 = 8
p1 = 4
p2 = 3
all_right = (disabled or RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = 4
p1 = 7
p2 = 0
all_right = (disabled or RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = 12
p1 = 12
p2 = 3
all_right = (disabled or RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = 24
p1 = 96
p2 = 4
all_right = (disabled or RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = 1000000000
p1 = 999999999
p2 = 0
all_right = (disabled or RunTest(4, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = 42
p1 = 18468
p2 = 0
all_right = (disabled or RunTest(5, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = 6335
p1 = 26501
p2 = 0
all_right = (disabled or RunTest(6, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = 19170
p1 = 15725
p2 = 0
all_right = (disabled or RunTest(7, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = 11479
p1 = 29359
p2 = 0
all_right = (disabled or RunTest(8, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = 26963
p1 = 24465
p2 = 0
all_right = (disabled or RunTest(9, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = 5706
p1 = 28146
p2 = 0
all_right = (disabled or RunTest(10, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = 23282
p1 = 16828
p2 = 0
all_right = (disabled or RunTest(11, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = 9962
p1 = 492
p2 = 0
all_right = (disabled or RunTest(12, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = 2996
p1 = 11943
p2 = 0
all_right = (disabled or RunTest(13, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = 4828
p1 = 5437
p2 = 0
all_right = (disabled or RunTest(14, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = 32392
p1 = 14605
p2 = 0
all_right = (disabled or RunTest(15, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = 3903
p1 = 154
p2 = 0
all_right = (disabled or RunTest(16, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = 293
p1 = 12383
p2 = 0
all_right = (disabled or RunTest(17, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = 17422
p1 = 18717
p2 = 0
all_right = (disabled or RunTest(18, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = 19719
p1 = 19896
p2 = 0
all_right = (disabled or RunTest(19, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = 5448
p1 = 21727
p2 = 0
all_right = (disabled or RunTest(20, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = 14772
p1 = 11539
p2 = 0
all_right = (disabled or RunTest(21, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = 1870
p1 = 19913
p2 = 0
all_right = (disabled or RunTest(22, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = 25668
p1 = 26300
p2 = 0
all_right = (disabled or RunTest(23, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = 17036
p1 = 9895
p2 = 0
all_right = (disabled or RunTest(24, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = 5632
p1 = 2816
p2 = 9
all_right = (disabled or RunTest(25, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = 2672
p1 = 5344
p2 = 5
all_right = (disabled or RunTest(26, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = 2272
p1 = 284
p2 = 3
all_right = (disabled or RunTest(27, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = 6952
p1 = 869
p2 = 1
all_right = (disabled or RunTest(28, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = 1326
p1 = 1326
p2 = 2
all_right = (disabled or RunTest(29, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = 6880
p1 = 1720
p2 = 4
all_right = (disabled or RunTest(30, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = 4240
p1 = 1060
p2 = 3
all_right = (disabled or RunTest(31, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = 1152
p1 = 2304
p2 = 8
all_right = (disabled or RunTest(32, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = 4624
p1 = 4624
p2 = 5
all_right = (disabled or RunTest(33, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = 943
p1 = 943
p2 = 1
all_right = (disabled or RunTest(34, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = 3812864
p1 = 122011648
p2 = 10
all_right = (disabled or RunTest(35, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = 441057280
p1 = 110264320
p2 = 16
all_right = (disabled or RunTest(36, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = 164069376
p1 = 40056
p2 = 4
all_right = (disabled or RunTest(37, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = 14196
p1 = 454272
p2 = 3
all_right = (disabled or RunTest(38, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = 4183040
p1 = 4085
p2 = 1
all_right = (disabled or RunTest(39, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = 117824
p1 = 120651776
p2 = 7
all_right = (disabled or RunTest(40, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = 4026368
p1 = 251648
p2 = 9
all_right = (disabled or RunTest(41, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = 9760
p1 = 639631360
p2 = 6
all_right = (disabled or RunTest(42, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = 5670912
p1 = 1417728
p2 = 10
all_right = (disabled or RunTest(43, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = 68255744
p1 = 4265984
p2 = 12
all_right = (disabled or RunTest(44, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = 9900032
p1 = 39600128
p2 = 13
all_right = (disabled or RunTest(45, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = 4945408
p1 = 38636
p2 = 3
all_right = (disabled or RunTest(46, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = 15912
p1 = 8146944
p2 = 4
all_right = (disabled or RunTest(47, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = 76384
p1 = 312868864
p2 = 6
all_right = (disabled or RunTest(48, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = 7091200
p1 = 443200
p2 = 7
all_right = (disabled or RunTest(49, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = 11939840
p1 = 46640
p2 = 5
all_right = (disabled or RunTest(50, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = 326272
p1 = 5220352
p2 = 8
all_right = (disabled or RunTest(51, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = 26328
p1 = 215678976
p2 = 4
all_right = (disabled or RunTest(52, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = 2412544
p1 = 2356
p2 = 3
all_right = (disabled or RunTest(53, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 54 -----
disabled = False
p0 = 730726400
p1 = 5708800
p2 = 11
all_right = (disabled or RunTest(54, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 55 -----
disabled = False
p0 = 481755136
p1 = 58808
p2 = 4
all_right = (disabled or RunTest(55, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 56 -----
disabled = False
p0 = 110400
p1 = 1766400
p2 = 7
all_right = (disabled or RunTest(56, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 57 -----
disabled = False
p0 = 2269184
p1 = 141824
p2 = 10
all_right = (disabled or RunTest(57, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 58 -----
disabled = False
p0 = 175374336
p1 = 171264
p2 = 9
all_right = (disabled or RunTest(58, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 59 -----
disabled = False
p0 = 63520768
p1 = 31016
p2 = 4
all_right = (disabled or RunTest(59, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 60 -----
disabled = False
p0 = 18247680
p1 = 8910
p2 = 2
all_right = (disabled or RunTest(60, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 61 -----
disabled = False
p0 = 17293312
p1 = 69173248
p2 = 14
all_right = (disabled or RunTest(61, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 62 -----
disabled = False
p0 = 19788
p1 = 324206592
p2 = 3
all_right = (disabled or RunTest(62, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 63 -----
disabled = False
p0 = 1641984
p1 = 6414
p2 = 2
all_right = (disabled or RunTest(63, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 64 -----
disabled = False
p0 = 1327104
p1 = 10368
p2 = 8
all_right = (disabled or RunTest(64, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 65 -----
disabled = False
p0 = 2228608
p1 = 4457216
p2 = 8
all_right = (disabled or RunTest(65, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 66 -----
disabled = False
p0 = 84123648
p1 = 164304
p2 = 5
all_right = (disabled or RunTest(66, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 67 -----
disabled = False
p0 = 14129152
p1 = 110384
p2 = 5
all_right = (disabled or RunTest(67, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 68 -----
disabled = False
p0 = 194808
p1 = 389616
p2 = 4
all_right = (disabled or RunTest(68, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 69 -----
disabled = False
p0 = 150000
p1 = 600000
p2 = 5
all_right = (disabled or RunTest(69, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 70 -----
disabled = False
p0 = 384352
p1 = 787152896
p2 = 6
all_right = (disabled or RunTest(70, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 71 -----
disabled = False
p0 = 314704
p1 = 10070528
p2 = 5
all_right = (disabled or RunTest(71, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 72 -----
disabled = False
p0 = 620625920
p1 = 9470
p2 = 2
all_right = (disabled or RunTest(72, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 73 -----
disabled = False
p0 = 105676
p1 = 422704
p2 = 3
all_right = (disabled or RunTest(73, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 74 -----
disabled = False
p0 = 7578
p1 = 7759872
p2 = 2
all_right = (disabled or RunTest(74, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 75 -----
disabled = False
p0 = 244383744
p1 = 119328
p2 = 6
all_right = (disabled or RunTest(75, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 76 -----
disabled = False
p0 = 736755712
p1 = 719488
p2 = 8
all_right = (disabled or RunTest(76, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 77 -----
disabled = False
p0 = 228976
p1 = 937885696
p2 = 5
all_right = (disabled or RunTest(77, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 78 -----
disabled = False
p0 = 38973440
p1 = 9515
p2 = 1
all_right = (disabled or RunTest(78, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 79 -----
disabled = False
p0 = 38780928
p1 = 4847616
p2 = 12
all_right = (disabled or RunTest(79, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 80 -----
disabled = False
p0 = 43008000
p1 = 21000
p2 = 4
all_right = (disabled or RunTest(80, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 81 -----
disabled = False
p0 = 747077632
p1 = 22799
p2 = 1
all_right = (disabled or RunTest(81, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 82 -----
disabled = False
p0 = 90185728
p1 = 88072
p2 = 4
all_right = (disabled or RunTest(82, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 83 -----
disabled = False
p0 = 30699520
p1 = 982384640
p2 = 13
all_right = (disabled or RunTest(83, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 84 -----
disabled = False
p0 = 655552
p1 = 2622208
p2 = 7
all_right = (disabled or RunTest(84, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 85 -----
disabled = False
p0 = 1
p1 = 2
p2 = 1
all_right = (disabled or RunTest(85, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 86 -----
disabled = False
p0 = 7
p1 = 7
p2 = 1
all_right = (disabled or RunTest(86, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 87 -----
disabled = False
p0 = 5
p1 = 5
p2 = 1
all_right = (disabled or RunTest(87, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 88 -----
disabled = False
p0 = 15
p1 = 15
p2 = 1
all_right = (disabled or RunTest(88, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 89 -----
disabled = False
p0 = 1
p1 = 1
p2 = 1
all_right = (disabled or RunTest(89, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 90 -----
disabled = False
p0 = 1
p1 = 8
p2 = 1
all_right = (disabled or RunTest(90, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 91 -----
disabled = False
p0 = 2
p1 = 1
p2 = 1
all_right = (disabled or RunTest(91, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 92 -----
disabled = False
p0 = 124
p1 = 512
p2 = 0
all_right = (disabled or RunTest(92, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 93 -----
disabled = False
p0 = 7
p1 = 14
p2 = 1
all_right = (disabled or RunTest(93, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 94 -----
disabled = False
p0 = 10
p1 = 5
p2 = 1
all_right = (disabled or RunTest(94, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 95 -----
disabled = False
p0 = 3
p1 = 3
p2 = 1
all_right = (disabled or RunTest(95, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 96 -----
disabled = False
p0 = 6
p1 = 3
p2 = 1
all_right = (disabled or RunTest(96, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 97 -----
disabled = False
p0 = 9
p1 = 27
p2 = 0
all_right = (disabled or RunTest(97, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 98 -----
disabled = False
p0 = 6
p1 = 8
p2 = 0
all_right = (disabled or RunTest(98, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 99 -----
disabled = False
p0 = 4
p1 = 5
p2 = 0
all_right = (disabled or RunTest(99, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 100 -----
disabled = False
p0 = 3
p1 = 5
p2 = 0
all_right = (disabled or RunTest(100, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 101 -----
disabled = False
p0 = 15
p1 = 3
p2 = 0
all_right = (disabled or RunTest(101, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 102 -----
disabled = False
p0 = 14
p1 = 7
p2 = 1
all_right = (disabled or RunTest(102, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 103 -----
disabled = False
p0 = 8
p1 = 1
p2 = 1
all_right = (disabled or RunTest(103, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 104 -----
disabled = False
p0 = 4
p1 = 12
p2 = 0
all_right = (disabled or RunTest(104, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 105 -----
disabled = False
p0 = 1
p1 = 12
p2 = 0
all_right = (disabled or RunTest(105, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 106 -----
disabled = False
p0 = 24
p1 = 16
p2 = 0
all_right = (disabled or RunTest(106, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 107 -----
disabled = False
p0 = 1
p1 = 3
p2 = 0
all_right = (disabled or RunTest(107, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 108 -----
disabled = False
p0 = 1
p1 = 4
p2 = 1
all_right = (disabled or RunTest(108, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 109 -----
disabled = False
p0 = 6
p1 = 1
p2 = 0
all_right = (disabled or RunTest(109, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 110 -----
disabled = False
p0 = 10
p1 = 2
p2 = 0
all_right = (disabled or RunTest(110, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 111 -----
disabled = False
p0 = 18
p1 = 4
p2 = 0
all_right = (disabled or RunTest(111, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 112 -----
disabled = False
p0 = 7
p1 = 6
p2 = 0
all_right = (disabled or RunTest(112, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 113 -----
disabled = False
p0 = 24
p1 = 36
p2 = 0
all_right = (disabled or RunTest(113, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 114 -----
disabled = False
p0 = 9
p1 = 18
p2 = 1
all_right = (disabled or RunTest(114, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 115 -----
disabled = False
p0 = 5
p1 = 10
p2 = 1
all_right = (disabled or RunTest(115, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 116 -----
disabled = False
p0 = 3
p1 = 6
p2 = 1
all_right = (disabled or RunTest(116, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 117 -----
disabled = False
p0 = 12
p1 = 2
p2 = 0
all_right = (disabled or RunTest(117, p0, p1, True, p2) ) and all_right
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
