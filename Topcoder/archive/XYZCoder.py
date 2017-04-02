cache = dict()
MOD = 10**9 + 7
def dfs(leader, roomate, room, size):
    if leader == room:
        return 1
    key = (leader, roomate)
    if key in cache:
        return cache.get(key)
    answer = dfs(leader + 1, roomate + 1, room, size)
    if roomate + 1 <= leader * size:
        answer += dfs(leader, roomate + 1, room, size)
    cache.setdefault(key, answer)
    return answer

class XYZCoder:
    def countWays(self, room, size):
        global cache
        cache = dict()
        answer = dfs(1, 1, room, size)
        for i in range(1, room + 1):
            answer *= i
        return answer % MOD


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, p1, hasAnswer, p2):
    obj = XYZCoder()
    startTime = time.clock()
    answer = obj.countWays(p0, p1)
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
p1 = 1
p2 = 2
all_right = (disabled or RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = 1
p1 = 2
p2 = 1
all_right = (disabled or RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = 2
p1 = 2
p2 = 4
all_right = (disabled or RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = 4
p1 = 5
p2 = 6840
all_right = (disabled or RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = 100
p1 = 100
p2 = 718243627
all_right = (disabled or RunTest(4, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = 55
p1 = 96
p2 = 271394236
all_right = (disabled or RunTest(5, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = 29
p1 = 85
p2 = 186283699
all_right = (disabled or RunTest(6, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = 29
p1 = 100
p2 = 884148227
all_right = (disabled or RunTest(7, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = 92
p1 = 83
p2 = 78404347
all_right = (disabled or RunTest(8, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = 83
p1 = 71
p2 = 127505228
all_right = (disabled or RunTest(9, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = 19
p1 = 46
p2 = 709848259
all_right = (disabled or RunTest(10, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = 23
p1 = 15
p2 = 154577394
all_right = (disabled or RunTest(11, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = 49
p1 = 49
p2 = 827095815
all_right = (disabled or RunTest(12, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = 62
p1 = 42
p2 = 17280594
all_right = (disabled or RunTest(13, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = 41
p1 = 54
p2 = 422877699
all_right = (disabled or RunTest(14, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = 34
p1 = 23
p2 = 598119987
all_right = (disabled or RunTest(15, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = 4
p1 = 9
p2 = 42840
all_right = (disabled or RunTest(16, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = 79
p1 = 7
p2 = 418870014
all_right = (disabled or RunTest(17, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = 33
p1 = 72
p2 = 172932139
all_right = (disabled or RunTest(18, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = 66
p1 = 97
p2 = 714389422
all_right = (disabled or RunTest(19, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = 62
p1 = 16
p2 = 866154756
all_right = (disabled or RunTest(20, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = 94
p1 = 6
p2 = 308906022
all_right = (disabled or RunTest(21, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = 62
p1 = 7
p2 = 186334570
all_right = (disabled or RunTest(22, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = 73
p1 = 70
p2 = 497002066
all_right = (disabled or RunTest(23, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = 1
p1 = 73
p2 = 1
all_right = (disabled or RunTest(24, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = 51
p1 = 26
p2 = 739203971
all_right = (disabled or RunTest(25, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = 84
p1 = 16
p2 = 434079293
all_right = (disabled or RunTest(26, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = 74
p1 = 29
p2 = 12942240
all_right = (disabled or RunTest(27, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = 2
p1 = 58
p2 = 116
all_right = (disabled or RunTest(28, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = 64
p1 = 32
p2 = 34205287
all_right = (disabled or RunTest(29, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = 1
p1 = 59
p2 = 1
all_right = (disabled or RunTest(30, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = 92
p1 = 83
p2 = 78404347
all_right = (disabled or RunTest(31, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = 44
p1 = 79
p2 = 157109850
all_right = (disabled or RunTest(32, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = 81
p1 = 99
p2 = 640894437
all_right = (disabled or RunTest(33, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = 59
p1 = 25
p2 = 711410043
all_right = (disabled or RunTest(34, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = 10
p1 = 91
p2 = 217459910
all_right = (disabled or RunTest(35, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = 24
p1 = 35
p2 = 161911161
all_right = (disabled or RunTest(36, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = 16
p1 = 9
p2 = 440660168
all_right = (disabled or RunTest(37, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = 65
p1 = 54
p2 = 481427123
all_right = (disabled or RunTest(38, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = 77
p1 = 39
p2 = 317353169
all_right = (disabled or RunTest(39, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = 97
p1 = 81
p2 = 49314584
all_right = (disabled or RunTest(40, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = 24
p1 = 33
p2 = 927344964
all_right = (disabled or RunTest(41, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = 14
p1 = 32
p2 = 278794421
all_right = (disabled or RunTest(42, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = 25
p1 = 80
p2 = 284832361
all_right = (disabled or RunTest(43, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = 22
p1 = 34
p2 = 274986521
all_right = (disabled or RunTest(44, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = 89
p1 = 90
p2 = 509687471
all_right = (disabled or RunTest(45, p0, p1, True, p2) ) and all_right
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
