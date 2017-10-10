MOD = (int)(1e9 + 7)
class SimilarNames2:
    def count(self, names, L):
        n = len(names)
        dp = [[0 for i in range(n)] for j in range(L + 1)]
        for i in range(n):
            dp[0][i] = 1

        def isPrefix(first, second):
            return second.find2(first) == 0

        for i in range(1, L):
            for j in range(n):
                for k in range(n):
                    if j != k and isPrefix(names[j], names[k]):
                        dp[i][k] += dp[i - 1][j]
                        dp[i][k] %= MOD
        answer = 0
        for i in range(n):
            answer += dp[L - 1][i]
            answer %= MOD

        for i in range(1, n - L + 1):
            answer *= i
            answer %= MOD
        return answer


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, p1, hasAnswer, p2):
    obj = SimilarNames2()
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
p0 = ("kenta", "kentaro", "ken")
p1 = 2
p2 = 3
all_right = (disabled or RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = ("hideo", "hideto", "hideki", "hide")
p1 = 2
p2 = 6
all_right = (disabled or RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = ("aya", "saku", "emi", "ayane", "sakura", "emika", "sakurako")
p1 = 3
p2 = 24
all_right = (disabled or RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = ("taro", "jiro", "hanako")
p1 = 2
p2 = 0
all_right = (disabled or RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = ("alice", "bob", "charlie")
p1 = 1
p2 = 6
all_right = (disabled or RunTest(4, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = ("ryota", "ryohei", "ryotaro", "ryo", "ryoga", "ryoma", "ryoko", "ryosuke", "ciel", "lun", "ryuta", "ryuji", "ryuma", "ryujiro", "ryusuke", "ryutaro", "ryu", "ryuhei", "ryuichi", "evima")
p1 = 3
p2 = 276818566
all_right = (disabled or RunTest(5, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = ("fjewoi", "fejwoifjewiefw", "f", "fewi", "few", "fweewe", "fldskds", "fefwwjo", "fww", "fewww")
p1 = 2
p2 = 443520
all_right = (disabled or RunTest(6, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = ("fjewoi", "fejwoifjewiefw", "f", "fewi", "few", "fweewe", "fldskds", "fefwwjo", "fww", "fewww")
p1 = 3
p2 = 10080
all_right = (disabled or RunTest(7, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = ("fjewoi", "fejwoifjewiefw", "f", "fewi", "few", "fweewe", "fldskds", "fefwwjo", "fww", "fewww")
p1 = 4
p2 = 0
all_right = (disabled or RunTest(8, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 50
p2 = 1
all_right = (disabled or RunTest(9, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 49
p2 = 50
all_right = (disabled or RunTest(10, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 25
p2 = 875934861
all_right = (disabled or RunTest(11, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 2
p2 = 159304024
all_right = (disabled or RunTest(12, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(13, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 8
p2 = 385325365
all_right = (disabled or RunTest(14, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 17
p2 = 183404719
all_right = (disabled or RunTest(15, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 24
p2 = 898371378
all_right = (disabled or RunTest(16, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 32
p2 = 875441647
all_right = (disabled or RunTest(17, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 41
p2 = 774691803
all_right = (disabled or RunTest(18, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = ("a", "b")
p1 = 1
p2 = 2
all_right = (disabled or RunTest(19, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = ("a", "b")
p1 = 2
p2 = 0
all_right = (disabled or RunTest(20, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = ("a", "aa")
p1 = 1
p2 = 2
all_right = (disabled or RunTest(21, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = ("a", "aa")
p1 = 2
p2 = 1
all_right = (disabled or RunTest(22, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = ("a", "aa", "aaa")
p1 = 1
p2 = 6
all_right = (disabled or RunTest(23, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = ("a", "aa", "aaa")
p1 = 2
p2 = 3
all_right = (disabled or RunTest(24, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = ("a", "aa", "aaa")
p1 = 3
p2 = 1
all_right = (disabled or RunTest(25, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = ("a", "aa", "ab")
p1 = 2
p2 = 2
all_right = (disabled or RunTest(26, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = ("a", "aa", "ab")
p1 = 3
p2 = 0
all_right = (disabled or RunTest(27, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa")
p1 = 2
p2 = 12
all_right = (disabled or RunTest(28, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa")
p1 = 3
p2 = 4
all_right = (disabled or RunTest(29, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa")
p1 = 4
p2 = 1
all_right = (disabled or RunTest(30, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = ("a", "aa", "ab", "aaa")
p1 = 2
p2 = 8
all_right = (disabled or RunTest(31, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = ("a", "aa", "ab", "aaa")
p1 = 3
p2 = 1
all_right = (disabled or RunTest(32, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = ("a", "aa", "ab", "aaa")
p1 = 4
p2 = 0
all_right = (disabled or RunTest(33, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = ("a", "aa", "b", "bb")
p1 = 2
p2 = 4
all_right = (disabled or RunTest(34, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = ("a", "aa", "b", "bb")
p1 = 3
p2 = 0
all_right = (disabled or RunTest(35, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = ("a", "aa", "b", "bb")
p1 = 1
p2 = 24
all_right = (disabled or RunTest(36, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa")
p1 = 2
p2 = 60
all_right = (disabled or RunTest(37, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa")
p1 = 3
p2 = 20
all_right = (disabled or RunTest(38, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa")
p1 = 4
p2 = 5
all_right = (disabled or RunTest(39, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa")
p1 = 5
p2 = 1
all_right = (disabled or RunTest(40, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = ("fkuxwu", "jkiekaajgr", "om", "necfhmw", "ookrihq", "fkusasqx", "fkuooeeimsi", "ggeyqxji", "ggeyq", "ggeosfwftss", "ggeyqcrxq", "necfhmwory", "fkuooeel", "gge", "jkie", "ggeyqzvef", "ggeyqveeg", "ggeoxok", "jkieqsl", "oo", "ggeyqxjibxn", "fku", "jkiedyfrd", "ne", "ootjf", "fkurvt", "jkietjyq", "ggeyqva", "jkiekaajg", "ggeo", "ggeyqv", "fkujstu", "fkuooee", "ootywl", "netty", "hhc", "g", "fkuug", "ggeosfw", "ggeyqvw", "fkuxw", "qab", "fkuooeeimsibgszh", "jkieq", "ggeyqxjim", "omcavc", "ggeyqzf", "jkiekaajgrpj", "jkieqya", "nedoy")
p1 = 6
p2 = 0
all_right = (disabled or RunTest(41, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = ("gfvtoqmt", "pwynnxavgelw", "pwynnxavvebyybdrbehbq", "gtwbzewoplstk", "pwynnxavcrblwxmdv", "g", "muemydnr", "gnfioebwxj", "pwynnxavvebyybuf", "pwynnxavvebyybzqguqkyoaijwuqxy", "pwynnxavvebyybdrfjgz", "pwynnxavvebyybdrcjsvsi", "gkuu", "gkuujbuft", "pwynnxavgelp", "gtuasxmzcu", "muemybrghcuykw", "pwynnxav", "pw", "gkuuj", "gt", "gnfioebw", "pwynnxavvebyybzqguqkyoaijwjnbv", "gfs", "gf", "gxatmn", "pwynnxavvebyyb", "gkuujq", "gxatmnv", "pwynnxavvebyybzqguqk", "pwynnxavvebyybdrcjsvsijury", "muemybrgkxd", "muemywftr", "gfjewls", "pwyd", "gtwbzewoplstkszcr", "gxatm", "muemy", "pwynnxavvebyybdr", "pwqi", "pwynnxavgel", "pwynnxavcrblw", "gnfio", "gtuasxm", "muemybrg", "gtua", "pwynnxavvebyybdrfjgzkqrxzn", "pwynnxavvebyybzqguqkyoaijw", "gtwbzewo", "pwynnxavvebyybdrbe")
p1 = 8
p2 = 0
all_right = (disabled or RunTest(42, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = ("kfrpxtlcavd", "kfrpnsiuonicn", "kfrpxthbgyyl", "kfrpxthbgyylabl", "kfrpxtlcakn", "kfrpxtlcavdizj", "kfrpxthbgyylo", "kfrpxtlcapw", "kfiyu", "kfrpxeqzlvj", "kfni", "kfrpxtlca", "kfrpxtlcav", "kfrpxeqzpkqaz", "kfrpnsiuonic", "kficd", "k", "kyic", "kfrp", "kfrpxthbgdq", "kfrpxt", "kfrpxeqzqwzcw", "kfrpxtuxolh", "ky", "kfrpxtuxogh", "kfrpxeq", "kfrpxthbg", "kfrpxeqzqw", "kfrpxeqzpk", "kfrpxthbgdqk", "kfrpxeqz", "kfrpnsi", "kfrpxtlcavpli", "zvw", "kfrpxtlcakngd", "kfrptvf", "kfrpxthbgyylab", "kfrpnsiuo", "kfnic", "kf", "kfrpxtlcavdtpe", "kfrpxeqzpkx", "kfrpmt", "kfrpxeqzqwwpc", "kfrpxeqlj", "kfrpxtuxo", "kfrpxtlcavdtpeqpf", "kfrpxthbgyylosd", "kfrpxtlcakngdn", "kfi")
p1 = 8
p2 = 149120794
all_right = (disabled or RunTest(43, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = ("mfhulmrudkbl", "mfhulmrudkblmaqpcaifmivsjrsklfweoyzu", "mfhulmrudkblmaqpcaifmivsjrsklfweoyzummco", "ztntaajuhzjufp", "mfhulmrudkblvjog", "zt", "ztnta", "mfhulmrudkbpzqfjrpeas", "zthbbaxembwcckggyymw", "ztntaajuhzjufpuybkkmoljzv", "mfhulmrudkblmaqpcaifmivsjrsoypaxcxms", "ztntaajuhzjufpuybkkmoljzvqllci", "mfhulmrudkblmaqpcaifmivsjrf", "mfhulmrudkblmaqpcaifm", "mfhulmrudkblmaqpcaifmfugpasfobigzml", "ztntahkoujtgasg", "mfhulmrudkblvjoggbpjrhktbnkmeuxgwng", "onge", "mfhulmrudkbcbonp", "acmgsqq", "mfhulmrudkblaclaea", "mfhulmrudkblmaqpcaifmivsjrsoypaxcxmwvwurdns", "mfhulmrudkblmaqpcaifmivsjrs", "mfhulmrudkblfhebemqdy", "mfhulmrudkbpzqfjrpea", "ztxoknxt", "kdzofkmxlv", "mfhulmrudkbcbonprla", "ztntaa", "mfhulmrudkbpzqfjrpeasletmz", "mfhulmrudkblmaqpcaifmfugpasfobixopmqkyy", "mfhulmrudkb", "mfhulmrudkblmaqpcaifmivsjrsklfweoyzuzwgj", "mfhulmrudkblmaqpcaifmfugpasfobitbvra", "mfhulmrudkbcbonpkqinokkca", "mfhulmrudkblvjoggbpjrh", "zthbbaxembwcc", "ztntaajuhzjufpnombnblay", "mfhulmrudkblmaqpcaifmivsjrsoypaxcxm", "ztntahkoujtgasgcafbown", "mfhulmrudkblmaqpcaifmivsjrfdwjocvmgya", "mfhulmrudkblmaqpcaifmivsjr", "mfhulmrudkblvjoggbpjrhktbnkmeuxgw", "mfhulmrudkblfhebemqdyfjvcd", "mfhulmrudkblmaqpcaifmfugpasfobiyhnhzkv", "mfhulmrudkblvjoggbpjrhbspgg", "mfhulmrudkblmaqpcaifmfugpasfobixi", "ltvckzcmo", "mfhulmrudkblmaqpcaifmfugpasfobi", "mfhulmrudkblmaqpcaifmivsjrsoypaxcxmbcsxmla")
p1 = 2
p2 = 552047667
all_right = (disabled or RunTest(44, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = ("giacozdx", "gixwtmjutysxltn", "ztoyj", "gixwtmjutysxcjfl", "giacoyr", "q", "gixwtmjutysxqys", "giigfvmw", "gixwtmjutysxcjflyis", "giigfzosqlglecnlkyahzsf", "gixwtmjutysxcjflsm", "gixwtmjutysxcjfly", "giacozdxy", "giigfzostbncjx", "gixwtmjutysx", "giac", "zt", "giigfvmwt", "gixwtmjutysxezp", "giigfzostbn", "giigfzosql", "gixwtmjutysxp", "giigfzosqlmcsih", "giigfzosqlglec", "giaco", "giigfzosgnn", "giigfvmwtd", "gixwsotv", "giigfzosqlglecnlkya", "bamn", "gixwtmjutysxezpcnq", "s", "qwv", "giackt", "giigfzosqlm", "giigfzos", "gixwtmjutysxcjflsbki", "giigfzosqlglecn", "gixw", "gixwtmjutysxpxkb", "giigf", "giigfvmwtaryv", "gixwtmjutysxcjfls", "gixwtmjutysxezpcn", "gi", "giigfzosg", "giigfzostbnc", "giigfl", "gixwtmjutysxs", "gixwtmju")
p1 = 8
p2 = 626855450
all_right = (disabled or RunTest(45, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = ("s", "jcgfk", "jcgfandgax", "xdovw", "xdnxph", "xdnn", "sxqk", "jcgfan", "jcgfunr", "sxq", "sxqwd", "jcgfjhho", "jcgfandgprx", "jcgfjhxatd", "jcgf", "xdn", "xdnxy", "jcgfanq", "jcu", "xd", "jcgfaa", "jcgfjhhoerun", "jcgfun", "jcgfandgtg", "sxqeye", "jcgfjhxa", "jc", "jcgfundk", "sxqey", "jcgfjhhoer", "xdouej", "jcgfandgpr", "jcgfanqln", "jcct", "jcgfjh", "jcgfu", "xdsr", "xdo", "jcgfandgprejjg", "jcgfandgprej", "sxqjo", "sxqeyh", "jcumr", "jccd", "jcgfjhhox", "jcgfans", "xdoue", "xdnx", "jcc", "jcgfandg")
p1 = 8
p2 = 0
all_right = (disabled or RunTest(46, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = ("nakomgxnwttpgcuvzzqvpceie", "zsiu", "us", "nakomgxnwttpggjafbheliwldljsobi", "nakomgxnwttpgcuv", "nakomgxnwttpggjafbhel", "uxsbcrqoe", "natlh", "nakomgxnwttpgpz", "fbndmtte", "nakomgxoxr", "nakomgxjcxexbfznmlpo", "nakomgxnwttpg", "xj", "ywt", "nakomgxhcsqttwudcf", "nakomgxnwttpgpzpc", "nakomgxjcxexb", "natlhfhhghofa", "natlhjafxqhctiw", "nakomgx", "u", "naxugma", "na", "uyond", "ywieatxuhhqk", "nakomgxnwttpgcuvzzqvpceem", "nakomgxnwttpgcuvzzqvpce", "nakomgxhcs", "ulsylnt", "tnbbsafoqeee", "yw", "nakomgxhcsqttwudcfmn", "natlhjafxqhctiwyzcb", "nakomgxnwttpggjafbheli", "natlhjafxqh", "xjcqmikiu", "nakomgxnwttpggjafbheliwldljso", "nakomgxjcxexbfznmlposysf", "natlhfhhg", "nakomgxnwttpgpdajlwjlvm", "tnbbsa", "udgbqgupa", "nakomgxhcsqttwudcftys", "naxu", "xjmdpldnxi", "natlhj", "ulsy", "ywieat", "nakomgxnwttpgpdajlwj")
p1 = 4
p2 = 141270782
all_right = (disabled or RunTest(47, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = ("aidjpprarxrlndhunoueqadr", "cdhgqy", "rjkehszhcqvsecxfxpagyz", "jcquyceqzjxwsnozgjflikvgmobrmt", "jcquyceqzjxngou", "jcquyceqzylhegvuhmfqvikguonthq", "jcquyceqzjxwsnojpvhft", "khbhcyfedhlwusmuglnda", "jcquyceqzjxwsno", "jcquyceqzjx", "jcquyceqzbcix", "jcquyceqzbcixqh", "khbhcyfedhlwsupagvuxl", "jcquyceqzjxfncfafrhuyrkpkdzbn", "kistqdpirvxkroqax", "ux", "jcquyceqzylhegvuhmn", "jcquyceqzjxwsnokbibov", "jcquyceqzjxfncfafrhuyrkp", "rjkehszhc", "aidjpprar", "aidjpprarxr", "rjkehszhcqvsecxfxpagyznxpp", "khbrslyphxar", "kistqdpirv", "jcquyceqzylhegvuhm", "jcquyceqzjxwsnozgjflikvg", "khb", "kistqdpirvxkro", "jcquyceqz", "jcquyceqzylhegvuhmfqvikguont", "jcquyceqzjxqbiagh", "jcquyceqzjxfncfafrh", "khbhcyfedhlwusmuglndaqysop", "jcquyceqzylhegvuhmfqvikguon", "jcquyceqzjxfncfafrhyx", "aidjpprarxrlndhoatfx", "khbhcyfedhlwusmuglndahuv", "khbhcyfed", "aidjpprarxrlndh", "uxzpu", "aidjpprarxrlndhpdnhqnx", "aidjppra", "rjkehszhcqvsecxf", "khbhcyfedhlw", "khbhcyfedhlwusmuglndaqysopcxlhmsy", "uxxcjwn", "jcquyceqzjxfncfafrhuyrkpdewpuyxw", "kistqd", "jcquyceqzylhegvuhmfqvikguontxxahesq")
p1 = 7
p2 = 0
all_right = (disabled or RunTest(48, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = ("hhjjxnrbpkkdyjjejk", "ezjlrweumrlaattet", "hhjjiympkmjimzfq", "hhjjxnrbpkkdyjjejkvobqio", "ezjlrweumr", "hhjjiyhbicwjtqojrknjmet", "ezjlrweumrlaattetuhvmgxjbzmt", "hhjjxnrbpkkdyjjejkgdiphubyf", "ez", "hhjjlauwx", "hhjjxnrbpkkdygkkcapaxmfdtfuakoh", "hhjjbjmvt", "hhjj", "hhjjiypqjvav", "ezjlrweumrlaattetktov", "hhjjrdjfwqxmgcbqz", "ezcrsmdr", "hhjjiympkmjimzf", "hhjjiymkfqd", "hhjjxnrbpkkdygkkcapaxmf", "hhjjrdjfwqxm", "hhjjou", "hhjjiy", "hhjjxnrbpkkdygkkcapaxdky", "hhjjxnrbpkkdygkkcapaxdkyxnrc", "ezjlrweumrrjrb", "hhjjiyhbicwjtqoylcc", "hhjjxnrbpkkdyjvpj", "hhjjrdjfwqxmssjhxj", "hhjjxnrbpkkdyepj", "hhjjxnrbpkkdygkkcapaxdkygilnfzjn", "ezjlrweumrlaattetuhvmgx", "hhjjxnrbpkkdygkkcapaxdkyvsz", "hhjjxnrbpkkdygkkcapaxmfdtfua", "hhjjxnrbpkkdygkkcapaxmfdtfuaragdgfjg", "hhjjxnrbpkkdygkkcapaxdkygilnfzjnd", "hhjjrdjfwqxmbvilzgu", "hhjjxnrbpkkdygkkcapax", "ezv", "hhjjiyah", "hhjjxnrbpkkdyowgjjby", "hhjjiyjirbk", "hhjjiyjirbkuud", "hhjjxnrbpkkdy", "hhjjiyhbicwjtqo", "hhjjxnrbpkkdygkkcapaxdkyume", "hhjjxnrbpkkdyjjejkasdimac", "hhjjxnrbpkkdygkkcapaxdkyxnrccrdohk", "hhjjbjmvtnmvoj", "hhjjiyhbicwjtqolx")
p1 = 4
p2 = 347365796
all_right = (disabled or RunTest(49, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = ("hwradvgyvpmlavagnuobl", "hwradvgyvpmlavfrw", "hwraugyaaqkhpjrozekblmavffixodaq", "hwra", "hwraugyaaqkhpjrozekblmavffixoda", "hwradwtm", "hwraugyaaqkhpjrozekblmav", "hw", "hwraugyaaqkhpjrozekblmavffixodaylrbczjmli", "hwradpaep", "hwradpde", "hwraugyaaqkhpjrozekblmavffixodavzsccrjykwcnixvdcp", "hwradglaewmxwymtaksgmlvkixcpfdqjju", "hwradp", "hwraugyaaxqluzhczhcq", "hwradvgyvpmlavlwapykfab", "hwradvgyvpmlavlwapykfa", "fzryhitugvjou", "hwrafm", "hwqfu", "hwrafmax", "fzry", "hwraugyaaqkhpjrozekblmavffixodavzsccrjykwcnixv", "hwradglaewmxwymtaksgmlvkixcpfdqjjunj", "fzryxljfjttdadqum", "hwradvgyvpmlavlwapykfaio", "hwradvgyvpmlavlwapykfarifimzoxu", "hwraugyaaxqluzhczhcciczipciref", "hwradglaewmxwymta", "hwmdhzguocndqbtz", "hwrahjotoxuwuiy", "fzryhitugvjouitlibaerc", "hwradpa", "hwrahjotoxuwuiyoqjtckgo", "hwraugyaaxqluzhczhc", "hwraugyaa", "hwradvgyvpmlavq", "hwradvgyvpmlav", "hwradglaewmxwymt", "fzryxljfjttdadqumbbbebhw", "fzryhitugvjouitlibaercuseyidkv", "hwraugyaaxqluzhczhcqo", "hwqf", "hwraugyaaqkhpjrozekblmavxanbyzawamqg", "hwradwxjmtz", "hwradpaeprjjswrn", "fzryhitugvjouzhnkqjaydlh", "hwradpamyn", "hwradglaewmxwymtaksgm", "hwrad")
p1 = 4
p2 = 611764249
all_right = (disabled or RunTest(50, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = ("fwgjtbllygebaofptsyt", "fwgjtbllygebpeniyvhyyjhybauktmpvqum", "fwgjtbllygeb", "fwg", "fwgjtbllygebpeniyvhyy", "fwgjtbllbhxds", "f", "fwgjtbllygebpeniyvhy", "fwgjtbllygebaofptsytn", "fwgjtbllygebp", "fwgjtbllygebpeniyvhyyjhybauloh", "fwgjtbllygebpeniyvhyyjhyba", "fwgjtbll", "fwgjtbllygebpeniyvhyyjhybaxmveky", "fwgjtbllygebpeniyvhyyjhybaul", "fwgjwzvveeftxbi", "fwgjtbllygebiqwpirhg", "fwgjtbllygebpeniyvhyyjhybaulo", "fwgjtbllygebpen", "fwgjtbllygebpeniyvhyyjhyb", "fwgjtbllygebpeniyvh", "fwgjtbllygebpenhzi", "fwgjtbllygebpeniyvhyyjhybbskhxd", "fwgjtbllygebpeniyvhyyjhy", "fwgjtbllygebpeniyvhyyjhybau", "fwgjtsw", "fwgjtbllygebaofptsytaaikf", "fwgjtb", "fwgjt", "fwgjtbllbhxdspcm", "fwgjtbllsnqz", "fwgjtbllygebpeniy", "fwgjtbllyge", "fwgjtbl", "fwgjwzvve", "fwgjtbllygebpeni", "fwgjtblliu", "fwgjtbllygebiqwpirhgvpber", "fwgjtbllygebpe", "fwgjtbllygebpeniyv", "fwgjtbllygebckfss", "fwgjtbllyg", "fwgjtbllsnqzpnc", "fwgj", "fwgjtbllygebpeniyvhyyjh", "fwgjtbllygebiqwpirhglls", "fw", "fwgjtblly", "fwgjtbllygebpeniyvhyyj", "draeo")
p1 = 30
p2 = 146326063
all_right = (disabled or RunTest(51, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = ("zoydaontqynmqascxsm", "zoydaontqynmqas", "zoydaontqynm", "zoydaontq", "g", "zoydaontqynmqascxfjm", "zoydaontqnl", "zoydaonmgv", "zoydaontqynmqascxfjbeud", "zoydaontqynmqascxfjbeuds", "zoydaontqynmqax", "zoydaontqynmqascxfjbxr", "zoydaont", "zoydaontqynmq", "zoydaontqynmqascxfjbeudj", "zoydaontqynmqascyv", "zoydaontqynmqascxf", "zoydaontpu", "zoydaontqynmqascxfjbeu", "zoydaonm", "zoydaontqynmqascyvtt", "zoydaontqynmqjk", "zoydaontqyn", "zoydaontqynmqascxfjbeui", "zoy", "zoydaontqynmqa", "zoydaonttk", "zoydaontqynmqascxfjdu", "zoydaontqynmqascxfjb", "zoydaonla", "zoydaym", "zoydaontqy", "zoydaon", "zoydaontqynmqaszu", "zoydaontqynmqascxfjmdo", "zo", "zoydaonmg", "zoydao", "zoydaontqynmqasc", "zoydaontqynmqascxfjbew", "zoyd", "zoydaontqynmqascxfjbeudjm", "zoydaontqynmqascxfsy", "zoydaontqynmqascxfj", "zoydaontqynmqascxfjbeudjmo", "zoydaontqynmqascxfd", "zoydaontqynmqascxfjbe", "zoyda", "zoydaontqynmqascx", "z")
p1 = 32
p2 = 0
all_right = (disabled or RunTest(52, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = ("shauwykcdi", "tkvlb", "sha", "shauwykcdiqbzyrhgs", "s", "shauwykcdiq", "shauwykcdiqbzyrjmzzhizx", "shauwykcdfnllp", "shauwykcdiqbzyrjmzzh", "shauwykcdiqbzyrj", "shauwyk", "shauwykcdiqbzyrjmlad", "shauwykcdiqbybgkunefvj", "shaqcclcplzobrli", "shauwykcp", "shauwykcdiqbzyrjm", "shaqcclc", "shauwy", "shauwykcdiqbzyr", "shauwykcdiqbzyrjmzzhyzux", "shahm", "shau", "shauwykcdiqb", "shauwykcdiqmz", "shauwykcdiqbzyrjmzzqpxew", "shauwykcdiqbzyrjmlada", "shauwykcdiqbzyrjmzzhi", "shauwhr", "shauwykcdiqbzyrjmzzhiz", "shauwykcdiqbzyrjmz", "shauwykca", "shauwykcdiqbybg", "snjo", "shauw", "shauwykcdiqbz", "shao", "shauwykcdiqbfhx", "shauwykc", "shauwykcdiqbzyrjnsqlqa", "shauwykcdiqbzyrjmzz", "shbwymewx", "shauwykctog", "shauwykcdiqbzy", "shauwykcdiqbzyrjmzzhizxf", "shauwykcdiqbzyrjmzzqpxewmo", "shauwykcd", "sh", "shauwykcdiqbzyrjmzzhizkgwjepsr", "shauwykx", "shahmeckgut")
p1 = 30
p2 = 0
all_right = (disabled or RunTest(53, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 54 -----
disabled = False
p0 = ("qgwxnbzxteq", "qgwxnbzxtekpgivz", "qgwxnbzxfj", "qgwxnbzxtekpw", "qgwxnbzxtexyg", "qgvy", "qgwxnbzxfjn", "qgwxnbzxtekpgivuz", "qgwxnbzx", "qgwxnbzxtekpgivuncxozs", "qgwxnbzxtekpg", "qgwxnbzxtexyk", "qgwxnbzxtekpgivuncxozsc", "qgwxnbzxtekpgivuncxo", "qgwxnbzxtekpgu", "qgwxnbu", "qgwxnbd", "qgwxnbzxtes", "qg", "qgwxnbzxtekpgivun", "qgv", "qgwx", "qgwxnbzxtekpgivuncxozsbi", "qgwxnbz", "qgwxnbzxtekpgi", "qgwxnbzxte", "qgwxnbzxtekpgiv", "qgwxnbzxtek", "qgwxnbzxtekpgivunc", "qgwxnbzxtekpgivuncxoz", "qgwxnbzxtex", "qgwxnbzxtekpgivuncxozsbir", "qgwxn", "qgwxnbzxtexw", "qgwxnbzxtekp", "qgwxnbzxtekpgivuncxozsb", "qgwxnbzxfjd", "qgwxnbzxtekpgib", "qgwxnbzxteqm", "qgwxnbzxtekpgivu", "qgwb", "qgwxnbzxtekpgivuncx", "qgw", "qgwxnbzxt", "q", "qgwxnbzxfjdv", "qgwxnbzxtekpwz", "qgwxnbzxf", "qgwxnbzxtexy", "qgwxnb")
p1 = 4
p2 = 592028584
all_right = (disabled or RunTest(54, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 55 -----
disabled = False
p0 = ("auxaaspzpvbfnlhlckwt", "auxaaspzpvbfnlhlckwimxbosgnvwnuoixt", "auxaaspzpvbfnlhlckwimxbosgsjjxojsllu", "auxaaspzpvbfnlhlckwimxbosgsjj", "auxaaspzpvbfnlhlckwimx", "auxaaspzpvbfnlhlckwimxbosgsjjxojsl", "aunddqy", "auxaaspzpv", "auxaaspzpvbfnlhlckwimxbosgsjjxojsll", "auxaaspzpvbfnlhlckwi", "auxaaspzpvbfnlhlckwimxbosgsjjxojs", "auxaaspzpvbfnlhlckwim", "auxaaspzpvbfnlhlckwimxbosgsjjxo", "auxaaspzpvbfnlhlc", "auxaaspzpvbfnlhlckwimxbosgsjjxoj", "auxaaspzpvbfnlhlckwimxb", "auxaaspzp", "auxaaspzpvbfnlhlckwimxbos", "auxohecdyvnob", "auxaaspzpvbfnlhlckwimxbosgsjjtzyngsw", "auxaaspzpvbfnl", "auxaaspzpvbfnlhlck", "au", "auxa", "auxaaspzpvbf", "a", "auxaaspzpvbfnlhlckwizng", "auxaaspzpvbfnlhlckwimxbosgsjjxojslluda", "auxaaspzpvbfnlhlckwimxbosgsj", "auxaaspzpvbfnlhlckwimxbo", "auxaaspzpvhjylwu", "auxaaspzpvbfnlhlckwimxbosgsjjx", "auxaaspz", "auxaaspzpvbfnlhl", "auxaaspzpvbfnlhlckwimxbwjswziqo", "auxaaspzpvbfnlhlckwimxbosg", "auxaaspzpvbfnlhlckwimxbosgsjjxojsllud", "auxaaspzpvbfnlh", "auxaas", "auxaaspzpvbfn", "aux", "auxaaspzpvbfnlhlckwimxbosgsjjma", "auxaasp", "auxaaspzpvbfnhxgfowsqh", "auxaaspzpvb", "auxaaspzw", "auxaaspzpvbfnlhlckwimxbosgs", "auxaaspzpvbfnlhlckwimxbosgsjjxojvbdekdsia", "auxaaspzpvbfnlhlckw", "auxaa")
p1 = 15
p2 = 315349501
all_right = (disabled or RunTest(55, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 56 -----
disabled = False
p0 = ("yxbhza", "yxbhzauyshgjob", "yxbhzauyshgjobzwqkkpn", "yxbhzauyshgjobzwqkkpnbxpqhtaz", "yxbhzauyshgjobzwqkkpnbzpolvofnmgk", "yxbhzauysh", "yxbhzauyshgjobzwqkkpnb", "yxbhzauyshgjobzwqkkpnbzpolvofsu", "yxbhzau", "yxbhzauyshgjobzwqk", "yxbhzauys", "yro", "yxbhzauyshgjobzwqkkpnbzp", "yxbhzauyshgjobzwqkkpnbzpo", "yxbhzauyshgjobz", "yxbhzauyshgjo", "yx", "yxbhzauyshg", "yxb", "yxbh", "yxbhzauyshgjobzw", "yxbhzauyshgjobzwqkkpnbzpolvofnmg", "yxbhzauyshgjobzwqkkgoytrziggg", "yxbhzauyshgjobzwqkkpnbzpolvofnmgkn", "yxbhz", "yxbhzauyshgjobzwqkkgoytrzi", "yxbhzauyshgj", "yxbhzauyshgjobzwqkgwuvia", "yxbhzauyshgjobzwq", "yxbhzauy", "ygiowbdv", "yxbhzauyshgjobzwqkkpnbzpolvofnmgknn", "yxbhzauyshgjobzwqkkpnbzpolvofn", "yxbkwvhil", "yxbhzauyshgjobzwqkkgoytrzirtukoy", "yxbhzauyshgjobzwqkkpnbz", "yxbhzauyshgjobzwqkkpnbxpq", "yxbhzauyshgjobzwqkkpnbai", "yxbhzauyshgjobzwqkkp", "yxbhzamvqdwa", "yxbhzauyshgjobzwqkkpnbzpolvof", "yxbhzauyshgjobzwqkkgoytrzirtukoyvw", "y", "yxbhzauyshgjobzwqkkpnbzpolv", "yxbhzauyshgjobzwqkkpnbzpolvo", "yxbhzauyshgjobzwqkkpnbzpolvofnm", "yxbhzauyshgjobzwqkk", "yxbhzauyshgjobzwqkkpnbzpol", "yxbhzauyshgjobzwqjjq", "yxbhzauyshgjobzwqkgwuvi")
p1 = 39
p2 = 0
all_right = (disabled or RunTest(56, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 57 -----
disabled = False
p0 = ("stvvspyjxayijbnjkidqp", "st", "stvvspyjxay", "stvvspyjxayi", "stvvspyjxayijbnjkidqpjm", "stvvspyjxayij", "stvvspyjxayijbnjkidcirpzzqeg", "stvvspyjxayijb", "stvvspyjxalrgbffv", "stvvspyjxayijbnjkidqcylsrfwadevarmsmshpr", "stvvspyjxayijbnjkid", "smntnawmklik", "stvvspyjeblkizm", "stvvspyjxayijbnjkidqpjmxax", "stvvspyjxayijbnjkidq", "stvvspyjxayijbn", "stxssrasoxht", "stvvspyjxayijbnjkikz", "stv", "s", "stvvspyj", "stvvtdsmyqhposn", "stvvsbsuixvxpbtv", "stvvspyjxayijbnjkidqcylsdqafoozu", "stvvspyjxayijbnjk", "stvvvarkl", "stvvspyjxayijbnjkiptjaiiahoih", "stvvspyjxayijbwfh", "stvvspyjxwpcprufpdxjff", "stvvspyjxayijbnjkidqcylsrfwadecqo", "stvvspyjx", "wvtcweog", "stvvspyjxayijbnjki", "stvvspyjxayijbnjkidqpjmx", "stvvspyfbppdw", "stvvspyjxayijbnjkidqcylsrfwade", "stvvspyjxayijbnjkidqpjmzgzkjv", "stxssrasoxh", "stvvspyjxayijbnjkidqcyls", "stvvspyjxayijbnjkidx", "stvv", "stvvspyjxa", "stvvspyjxayijbnjkthhjwgp", "stvvspyjxayijbnjkidqpj", "stvvspy", "stvvspyjxayijbnjkidqpjmxa", "stvvsp", "stvvs", "stvvspyjxayijbnj", "stvvvarklixqx")
p1 = 27
p2 = 0
all_right = (disabled or RunTest(57, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 58 -----
disabled = False
p0 = ("mpvlermltmsylshegfmbpuzbcliwmlsycpm", "mpvlermltmsylshegfmbpuzbcliwmlsycpmhipvln", "mpvlermltmsylshegf", "mpvlermltmsylshegfmbpuzbcliwml", "mogkireezsutpufo", "mphmqsxx", "mpvlermltmsylshegfmbpu", "mpvlermltmsylsh", "mpvlermltmsylshegfmbpuzbcli", "mpvlermltm", "mpvlermltmsylshegfmbpuzbcliwmlsyc", "mpvlermltmsylshegfmbpuzbclimayhjcporqfnp", "mpvlecrnpdf", "mpvlermltmsylshegfmbpuzbc", "mpvlermltmsylshegfmbpuzbcliwmlsycpmhi", "mp", "m", "mpvlermltmsylshegfmbpuzbcliwmlsy", "mpvlermltmsrklhqyxe", "mpvl", "mpvlermltmsylsheg", "mpvle", "mpvlermltmsrklhqy", "mpvlermltmsylshe", "mpvlermltmsylshegfm", "mpvlermltmsylshegfmbpuzylnab", "mpvlermltmsylshegfmbpuzbcliwmls", "mpvlermltmsylshegfmbpuzbcliwmlsycqbqdsvlibilp", "mpvlermltmsylshegfmbpuz", "mpvlermltmsylshegfmbp", "mpv", "mpvler", "mpvlerm", "mpvlermltmsyls", "mpvlermltmsylshegfmbpuzbcliwmlsycp", "mpvlermltms", "mpvlerml", "mpvlermltmsylshegfmbpuzb", "mpvlermltmsylshegfmbpuzbcliw", "mpvlermlt", "mpvlermltmsylshegfmbpuzbcliwmlsycpmhiy", "mpvlermltmsylshegfmbpuzbcliwmlsycpxbmfc", "mpvlermltmsy", "mpvlermltmsylshegfmbwyesl", "mpvlermltmsylshegfmb", "mpvlermltmsyl", "mpvlermltmsylshegfmbpuzbcliwm", "mpvlermltmsylshegfmbpuzbcliwoqp", "mpvlermltmsylshegfmbpuzbcl", "mpvlermltmsylshegfmbpuzbcliwmlsycpmh")
p1 = 27
p2 = 532559953
all_right = (disabled or RunTest(58, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 59 -----
disabled = False
p0 = ("znfufsvwkgumbnjmr", "znfufsvoje", "znfufsvvpcnbgneins", "znfufsvojehljletivwxxbmywrmduqlm", "znfufsvojeh", "znfufsvojehljcfkc", "znfufsvo", "okvqkughio", "znfufsvojehljcfkcr", "znfufsurxdnqxojjtss", "znfufsvoj", "znf", "znfufsvojehljcfkcruvujznhwgqzxjs", "znfuf", "znfufsvojehljletivwxx", "znfufsahlrc", "znfufsu", "znfufsvojehljc", "zbmjthcwtuzrke", "znfufsvojehlbkrp", "znfufsvojehlvmwfshgcxv", "lwpsjaxpmbi", "znfufsvojehl", "znfufsvojehlbkrpihbcgsblhtkwct", "znfufsvojehljcfkcru", "znfufsvojehljyvthd", "znfufsvojehljcf", "znfufsvojehljsedbfqkb", "zn", "znfufs", "znfufsvojehlj", "znfufsvojehljyvthdrbojli", "znfufsvojehljcfkcruo", "znfufsvojehlbkrpqobsdpajgkspfjctazpnhjyixqlufnnrsr", "znfufsv", "znfufsvojehlbkrpinatmeenr", "znfu", "znfufsvojehlbkrpqobsdpajgkspfjctazpnh", "z", "znfufsvojehljcfkcrutdjpawofq", "znfufsvojehcyou", "znfw", "znfufsvojehljcfk", "zubw", "znfufsvojehljletivwxxxsvqjazlwbml", "znfufsvojehljcfkcruos", "znfufsuxnvoihohwaigi", "znfutxgnm", "znfufsvojehlbkrpqobsdpajg", "znfufsvojehlbkrpi")
p1 = 17
p2 = 839600600
all_right = (disabled or RunTest(59, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 60 -----
disabled = False
p0 = ("cso", "csoskimpsmnohhtyipkhgrnrfekag", "csoskimpsmnohh", "csoskimp", "csoskimpsmnohhtyip", "csoskimpsmnohhtyipkhgrnrfekagzxkjqgqn", "csoskimpsmnohhtyipkhgrnrfekagzxksld", "csoski", "csoskimpsmnohhtyipkhgrnrf", "csoskimpsmnohhtyipkhgrnrfekagz", "csoskimpsmnohhtyipkhgrnrfe", "csoskimps", "csos", "csoskimpsmnohhtyipkhgrnrfekagzxksnsyyvgz", "csoskimpsmnohhtyipk", "csoskimpsmnohhtyi", "csoskimpsm", "csoskimpsmnohhtyipkhgrnrfekagzxks", "csoskimpsmnohhtyipkhgrnrfbagylvh", "csoskimpsmnohhtyipkhgrnrfekagzxksldc", "csoskimpsmnohhtyipkhgrnrfeka", "csoskimpsmno", "csoskimpsmnohhtykaouhu", "csosk", "csoskimpsmnohhtyipkhgrnrfvuqdetid", "cs", "csoskimpsmnohhtyipkh", "csoskimpsmnohhtyipkhgrnrfek", "csoskimpsmnohbhacc", "csoskimpsmnohhtyipkhgrnrfekagzxksldcv", "csoskimpsmnohhtyipkhgrnvtujb", "csoskimpssrasmg", "csoskimpsmnohhtyipkhgrnr", "csoskimpsmnohhtyiikdc", "csoskimpsmn", "csoskimpsmnohht", "csoskimpsmnohhtykaouhutfwxbnqq", "csoskimpsmnohhtyipkhgrnrfekagzxksnsyyvgzznovk", "csoskimpsmnohhtyipkhgrnrfekagzxk", "c", "csoskimpsmnoh", "csoskimpsmnohhtyipkhgr", "csoskimpsmnohhtyipkhgrnrucrr", "csoskimpsmnohhtyipkhgrnrfekagzx", "csoskimpsmnohhtyipkhg", "csoskim", "csoskimpsmnohhtyipkhgrnrfekagzxksl", "csoskimpsmnohhty", "cdiem", "csoskimpsmnohhtyipkhgrn")
p1 = 27
p2 = 494552978
all_right = (disabled or RunTest(60, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 61 -----
disabled = False
p0 = ("ygqyotcxtvqcsyr", "ygqyotcxtmo", "ygqyotcxtmoidxut", "ygqyotcxtmoidoyieceufesti", "ygqyotcxtvqcsyjactrbqws", "ygqyotcxtvqcsyj", "ygqyotsxmpdvtgl", "ygqyotcxtvqcs", "ygqyotcxtmoid", "ygqyotcx", "ygqyotcxtmoidxutveu", "ygqyo", "ygqyotcxtmoidxutveuyp", "ygqy", "yg", "ygqyotcxtvqcsyrccmwcqnnavksg", "ygqyotcxtmoidxhktl", "ygqyotcxtmoidxutveuypu", "ygqyotcxtmoidxu", "ygqyotcxtvqcsyjac", "ygqyotcxt", "ygqyotcxtm", "ygq", "ygqyotcxtvqcsyrcvq", "ygqyotcxtmesiqqmifzibm", "ygqyotcxtmoidxutveuy", "ygqyotcxtmoidxujiyby", "ygqyotcxtvqcsyrcc", "ygqyotc", "ygqyotcxtvqcsyrc", "ygqyotcxtvqcsyrcclaznuj", "ygqyotcxtmoidxutveuypuaferjig", "ygqyotcsowjpskbvuwd", "ygqyotcsow", "ygqyotcxtmoidxutve", "ygqyotcxtvq", "ygqyotcxtvqcsyrlunerr", "ygqyotcxtmoidxutv", "y", "ygqyotcxtv", "ygqyotcxtmoidivkax", "ygqyotcgt", "ygqyotcxtvqcsyviuvhkpq", "ygqyotcxtvqc", "ygqyotcxtvqcsy", "ygqyotcxtmoidoyie", "ygqyotcxtmoi", "ygqyotcxtmoidx", "ygqyot", "ygqyotcxtmoidxutveuypumajevfib")
p1 = 13
p2 = 781006024
all_right = (disabled or RunTest(61, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 62 -----
disabled = False
p0 = ("kcwilbdoqanfxkczkpwkh", "kcwi", "kcwilb", "kcwilbdoqanfdkirlujtkxdmhrzswvx", "kcwilbdoqanfxkczmbtnkhzodmyoevip", "kcwilbdoqanfxkczmbtn", "kcwilbdoqanfxkczmbtnk", "kcwilbdoqanfdkirlu", "kcwilbdo", "kcwil", "kcwilbdoqankpmzfhbt", "kcwilbdoqanfdkirlex", "k", "kcwilbdoqanfxkc", "kcwilbdoqanfdkirluj", "kcwilbdoqanfxkczmbt", "kcw", "kcwilbdoq", "kcwilbdoqanfdkirluji", "kcwilbdoqanfxkczm", "kcwilbdoqanfdkir", "kcwilbdoqanfxen", "kcwilbdoqanfdkirlujtkxdmhrzswvxlvztqleueqrid", "kcwilbdoqanfdkirlwwhmnibuhlw", "kcwilbdoqanfdkirlexhpe", "kcwilbdoqanfxkcz", "kcwilbdoqanfxkczmbtnkklkgwerzai", "kcwilbdoqanfd", "kcwilbdoqanfdkirl", "kcwilbdoqanfxkczmbtnkhzodmyoevipxmlfszuukr", "kcwilbdoqanfdkirlujtkxdmhrzswvxhbfthxudrg", "kcwilbdoqa", "kcwilbdoqanfxk", "kcwilbdoqanfxkczmbtnkerxzqg", "kcwilbd", "kcwilbdoqanfdkirlujaankjsurjfouplkonic", "kc", "kcwilbdoqanfdkirlujix", "kjhkdnbxxe", "kcwilbdoqanfx", "kcwilbdoqanfxkczmbtnkh", "kcwilbdoqanfdkirlujaankjsurjfoupl", "kcwilbdoqanfdkirlujixt", "kcwilbdoqanfdklsjbwpww", "kcwilbdoqanfdk", "kcwilbdoqanf", "kcwilbdoqan", "kcwilbdoqanfdki", "kcwilbdoqanfxkczmbtngtaedotlpqsa", "kcwilbdoqanfxkczmb")
p1 = 10
p2 = 165853970
all_right = (disabled or RunTest(62, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 63 -----
disabled = False
p0 = ("mlpk", "mlpkikeoqnhh", "mlpkikeoqnhclqhrezlhn", "mlpkikeoqnhclqmfzyystmcjfcnwz", "mlpkikeoqnhhrgwquhnim", "mlpkikeoqnhclqmfz", "mlpkikeoqn", "mlpkikeoqnhclq", "mlpkikeoqnhclqmf", "mlpkikeoqnhclqmfzyystme", "mlpkikeoqnhma", "mlpkikeoq", "jvuwvqeymc", "mlpkikeo", "mlpkikeoqnhhrgwqu", "mlpkikeoqnhclqmfzyy", "mlpkiyticw", "mlpkikeoqnhclqmfzywpmywdi", "mlpkikeoqnhclqmfzyystmej", "ml", "mlpkiccoqjvjr", "mlpkikeoqnh", "mlpkikeoqnhclqmfzyfg", "mlpkikeovyuigjye", "mlpkikeoqnhc", "mlpkikeoqnhhrgwquh", "mlpkikeoqnhclqmfzywpmywdiovalggue", "mlpkikeoqnhhrgwquhn", "mlpkiccoqjvjrfvfjjwquej", "mlpkikeoqnhclqmfzyystm", "m", "mlpkikeoqnhclqelgrjewuyo", "mlpkikeoqnhcl", "mlpkik", "mlpkikeoqnhclqmfzyys", "mlpkikeoqnhclqmfzy", "mlpki", "mlpkikeoqnhhrgwquhni", "mlpkikeoqnhhrggnzbz", "mlpkikeoqnhhrg", "mlpkikeoqnhclqmfzyyst", "mlpkikeoqnhcluppqlfwjt", "mlpkikeoqnhhrgwqlcsskahqi", "mlp", "mlpkikeoqnhhrgw", "mlpkikeoqnhhr", "mlpkike", "mlpkikeoqnhhrgwq", "mlpkikeoqnhclqmfzypthfi", "mlpkikeoqnhclqm")
p1 = 23
p2 = 853355262
all_right = (disabled or RunTest(63, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 64 -----
disabled = False
p0 = ("gscrugbbxetpl", "gscrugbbfjwxsjcnaihia", "gscrugbbxjxpjjqblequph", "gscrugbbfj", "gscrugbbfjwxsjcqdzpht", "gscrugbthsdczxjkjjb", "gscrugb", "gscrugbbfjwxsjcnaihiwfngfqmh", "gscrugbbxetplmbrhp", "g", "gscrugbbxettzjjybgajil", "gs", "gscrugbbxetplm", "gscrugbbxetplmbqfi", "gscrug", "gscrugbbxjxpjjq", "gsc", "gsw", "gscrugbbfjwxs", "gscru", "gscrugbbxet", "gscr", "gscrugbbfjwxsj", "gscrugbbfjw", "gscrugbbfjwxsjc", "gscrugbbfjwxsjcnai", "gscrugbbfjwxsjcqdzphtcfvapqv", "gscrugbbx", "gscrugbbfjwxsjcqdzphtcfvapqvupvducorolw", "gscrugbbfjwxsjcqdzphtcfvapq", "gscrugbbxetplmbqfimg", "gscrugbbxetplmbqfihfhkvk", "gsh", "gscrugbbxetplmbqfim", "gscrugbbfjwxsjcna", "gscrugbbxetplmb", "gscrugbbfjwxsjcn", "gscrugbbf", "gscrugbbfjwx", "gscrugbthsdczxjk", "gscrugbb", "gscrugbbfjwxsjcnaihi", "gscrugbbxetplmbq", "gscrugbbxe", "gscrugbbfjwxsjcnaih", "gscrugbbxetp", "gscrugoqxvxitxacb", "gscrugoqxvxitxacbngywsb", "gscrugbbxetplmbqf", "gscrugbbfjwxsjcqdzphtcfvapqcijfmidw")
p1 = 15
p2 = 827302343
all_right = (disabled or RunTest(64, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 65 -----
disabled = False
p0 = ("sxixusckjuukcc", "sxixusckjvwewoq", "sxixusckjyez", "sxixusckjuukccmihacgudwdaq", "sxix", "sxixusckjvwe", "sxixusckjvwewowcemroct", "sxixusckjuukccmiha", "sxixusckjvwewh", "sxixusckl", "sxixusckjvwewowcemro", "sxixusckjvwewowlhq", "sxixusckjuukccm", "sxixus", "sxixusckjuukccmihacgudw", "sxi", "sxixusckjvyjuq", "sxixusckjvyju", "sxixusckjvwewowcemr", "sxixusckjuukccmihac", "sxixusckjuuk", "sxixusckju", "sxixusckjuu", "sxixusckjvwewow", "sxixusckjuukccmi", "sxixusckjvw", "sxixusc", "s", "sxixusckjvwewowcem", "sxixusckjvwewo", "sxixusckj", "sxixu", "sxixusckjuukccmihacglo", "sxixusckjve", "sxixusckjuukccmihacglot", "sxixusckjv", "sxixusckjvyjuboj", "sxixusx", "sxixusckjvwewowcemroc", "sxixusckjuukc", "sxixusck", "sxixusj", "sxixusju", "sxixusckjvwew", "sxixusckjvwewowce", "sxixusckjvwewowc", "sxixusckjuukccmih", "sx", "sxixusckjvwewowcecb", "sxixusckjuukccmihacg")
p1 = 25
p2 = 0
all_right = (disabled or RunTest(65, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 66 -----
disabled = False
p0 = ("dqfawgdsyogdo", "dq", "dqf", "dqfawgdvpubbjcfxx", "dqfaw", "dqfawgdsyogdie", "dqfawgdvpu", "dqfawgdsyogdoegq", "dqfawgdsykx", "dqfawgdvpubbjcfxft", "dqfawgd", "dqfawgdvp", "dqfawgdvpub", "stayyw", "st", "dqfawgdvpubbjcfxf", "dqj", "dqfawgdsyog", "v", "dqfawgdvpubbm", "dqfawgdsyogd", "dqfawok", "dqfawgdvpufp", "dqfawgdsyoeb", "dqfawgdvpubmb", "dqfawgdsyo", "dqfa", "dqfawgdsyogdoegqdq", "dqjha", "dqfawgdvpubbjc", "dqfawgdsyoe", "dqfawgdvpubbjcfxxi", "dqfawgdvpubb", "stayo", "dqfawgdsyogdoegqd", "dqfawgdvpubbj", "dqfawgds", "dqfawgdvpubbjcfx", "dqfawgdvpubbjcfxj", "dqfawgdvpubk", "dqfawgdsyogdoe", "dqfawgdvpubbjcf", "dqfawg", "dqfawgms", "dqfawgdsy", "d", "dqfawgdsyogdoeg", "dqfawgdsyogdoegqdql", "dqfawgdv", "stay")
p1 = 8
p2 = 4201197
all_right = (disabled or RunTest(66, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 67 -----
disabled = False
p0 = ("vphfytdzufftyo", "vphfytdzufftfedwrxltscav", "vphfytdzufftyquff", "vphfytdzufftfedwrxltsc", "vphfytdz", "v", "vphfytdzu", "vphfytdzufftfedwrxl", "vphfytdzufftyquffs", "vphfytdzufftyquffsa", "vphfytdzufftyquffsadmc", "vphfytdzufftyquffsad", "vphfdc", "vphfytdzufftyquffm", "vphfytp", "vphfytdzufftfedwrxltsca", "vph", "vphfytdzufftyq", "vphfytdzjo", "vphfytdzufftyqu", "vphfytdzufftyqunk", "vphfytdzufftfedwr", "vphfy", "vphfytdzufftfed", "vphf", "vphfytdzufftyquffsadmch", "vphfytd", "vphfytdzufftfedw", "vphfytdzufftfedwrxlt", "vphfytdzufftfedwrxltscavvda", "vphfytdzufftfedwrx", "vphfytdzufftyquffsadm", "vphfytdzuf", "vphfytdzufftf", "vphfytdzufftfedwrxltscfz", "vphfytdzufftfe", "vphfytdzufftfedwrxltscavvh", "vtw", "vphfytdzuff", "vphfytdzufftct", "vphfytdzufftfedwrxh", "vphfytdzufftfedwrz", "vp", "vphfytdzufftfedwrxltscavv", "vphfytdzufft", "vphfytdzufftfedwrpy", "vphfytdzuffty", "vphfytdzufftyquf", "vphfytdzufftfedwrxlts", "vphfyt")
p1 = 6
p2 = 295761820
all_right = (disabled or RunTest(67, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 68 -----
disabled = False
p0 = ("tgstncqzpqmlxp", "tgs", "tgstncqzpqmlqtziuozic", "tgstncqzpqmlxpijwoo", "ngaxoerdkjpuc", "tg", "tgstncqzpqmlxpijw", "tgstncqzpq", "tgstncqzpqmlxpooqav", "tgstncqzp", "tgstgbnmimnlh", "tgstn", "tgstncqzpqmlxpijwo", "tgstncqzpqmlx", "tgstncqzpqmltzyblnovhns", "tgstncqzpqml", "tgstncqzpqmlxpij", "tgstnxafv", "tgstncqzpqmlxndcirxrgrm", "tgstncqzpqmlxpijwoodjtjmhaws", "tgstnxafvxlbtfzievpzoj", "tgstncqzpqmlxpijwoolgbydwrrmovcjy", "tgstncqzpqmlxpijwoolgb", "tgstncqzpqm", "tgstncqzpqmlxnm", "tgstncqzpqmlxpipuxlkvozjl", "tgstncqzpqmlmnbszq", "tgstncqzpvnzvqwbnoxnw", "tgstncqzpqmlxnmkphw", "tgstncqzpqmlxnmkphwo", "tgstncqzpqmlxnmkph", "tgstncq", "tgstncqzpqmlxpijwool", "tgstncqzpqmlxpijwoolg", "tgstncqzpqmlxn", "tgstncqzpqmlxpijwoolgby", "tgstncqz", "tgstncqzpqmlxpi", "tgstncpr", "tgstncqzpqmlxpijwoolgbyd", "tgstncqzpqmlxpipuxlkvozjlspeq", "t", "tgstncqzpqmlxpijwoodjtjmhawspzufvtshpigy", "tgstncqzpqmloilxgbmokk", "tgstncqzpqmlxpifsffxbd", "tgstnc", "tgstncqzpqmlxnmk", "tgstncqzpqmlxnmkp", "tgstnclapw", "tgst")
p1 = 31
p2 = 0
all_right = (disabled or RunTest(68, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 69 -----
disabled = False
p0 = ("xgehfqbmrpngcem", "xgehfqbmr", "xgehfqbmrpnjcwck", "xgehfqbmulbgfnh", "xgehfqbmrp", "xgehfqbmrpngce", "xgehfqbmul", "xgehfqbmjp", "xgehfqbmrpngcelw", "xgi", "xgehfqbmulbgf", "xgehfqbmrpnjcwwprt", "xgehfqbmulbgfnhaz", "x", "xgehfqbmulbgfnhazawnr", "xgehfqbmrpnjcw", "xgehfqbmulbgfnhazaw", "xgehfqb", "xgehfqbmulbgfnha", "xg", "xgehfqbmrpngcel", "xgehfqbmrpngcelkmin", "xgeh", "xgehfqbm", "xgehfqbmrpngcemozo", "xgehfqbmulgph", "xgehfqe", "xgehfqbmrpnjcww", "xgehfqbmrpngc", "xgehfqbmulbgfnhadmomv", "xgehfqbmulbgfnhadmhq", "xgehfqbmrpng", "xgehfqbmulb", "xgehfqbmu", "xgehfqbmrpngcelk", "xgehfqbmulqe", "xgehfqbmulbgfnhazawdtyc", "xgehfqbmrpngca", "xgehfqbmulbgfnhaza", "xgehfqbmulbgfnhadm", "xgehfqbmrpn", "xgehfqbmrpngcelkf", "xge", "xgehfqbmulbgfnhazawd", "xgehfqbmulbgfnhuz", "xgehfqbmulbgfn", "xgehfqbmrpngcelkfzrk", "xgehfq", "xgehfqbmulbg", "xgehf")
p1 = 5
p2 = 978958357
all_right = (disabled or RunTest(69, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 70 -----
disabled = False
p0 = ("srsy", "srkjcxeyx", "srssvnoujrmqdntuajtn", "s", "srssvnounl", "srssvno", "srssvnounlblc", "srssvnoujr", "srssvnounlblcv", "srssvnounlblcvyqf", "srssvnoun", "srssvnounlblcvyqfyfcceckn", "srssvnounlblcvyq", "sgidv", "sr", "srss", "srssv", "srssvnoujrm", "srssvnou", "srssvnounlblcvy", "srssvnounlblcvyqfyfc", "srssxffa", "sdzvpb", "sdzvpbdptwcg", "srs", "srssvnoujrmqdntuajypjzpo", "srssxffavxpumg", "srssvnoudord", "srssvnoujrmqdnt", "srssvnoujjusgeb", "srssvnounlblcvyqft", "srssvnounlblco", "srssvnoujrmqdn", "srssvnoujrmqdntuajyp", "srssvnounlb", "srssvnoujowfma", "srssvnounlblcvyqfyf", "srssvnoujrmqdntuaj", "srssvnounlbl", "sdzvpbdpt", "srssvnouj", "srssvnoujrmqd", "srssvn", "srsjsz", "srssvnoujrmqdntua", "srsyzoaw", "srssvnounlblcvyqglrz", "srssvnoujrmqdntuajy", "srssvnoujrmqdntu", "srssvnoujrmq")
p1 = 13
p2 = 198670219
all_right = (disabled or RunTest(70, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 71 -----
disabled = False
p0 = ("ddrgafnrx", "hihu", "ddrgafnrxpxqiln", "hihubfeturt", "hihubfeturvfusurldca", "hihub", "p", "h", "hihubfxgvdpcldp", "ddrgafncnjhcnwiuakskgukpjo", "hihubfe", "hihylehh", "ddrg", "hihbedjmcq", "hiwmjgnyfi", "he", "palyx", "ddrga", "d", "dd", "palyxmrwwab", "ddrgafnr", "pgntje", "hihubfeturto", "hihubfetur", "ddrgafnrxpxqililart", "hihuldiewwizp", "hihubf", "ddrgafnrxp", "hihubfet", "hih", "hihbedjmcqpjhckknpxx", "ddrgafnrxpxqi", "ddr", "hihubfetefwsf", "hiwmjgny", "hihvciqw", "hihbedj", "ddrgafnrxtnb", "ddrgafn", "ddrgafavhgigd", "hihuldiewwizpkdfwi", "hihbedjjydpem", "hihubfetu", "ddrgafnrxpx", "ddrgaf", "ddrgafnrxpxqil", "ddrgafncnjhcnwiua", "hi", "ddrgafnrxpxq")
p1 = 9
p2 = 258821703
all_right = (disabled or RunTest(71, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 72 -----
disabled = False
p0 = ("jmhsgapbkxwpjaa", "jmhsgapbkxwpja", "jmhsgapbkxwp", "fjjexeyq", "fjjexeyqxmupfmfeazhuusg", "fjjexeyqxmupfmfeazhuusgpku", "fjjexeyqxmupfmfeazhuusgoymg", "jmhsg", "jmhsgapbkx", "jmhsgapbk", "jm", "fjjexeyqyqjx", "j", "fjsrxchcfz", "jmhsgapbkxnqwr", "jmhsgapbkxwpjaaephy", "fjjexeyqx", "jmhsgapbkxwgftw", "jmhsgapbkxwpjczswejebperq", "fjj", "jmhsgapbkxwpjaae", "fjjexeymx", "fjjexeyqxmupfmfeazhuusgnvyk", "jmhsgapb", "fjjexeyqxmud", "jmhs", "fjjexeyqxmudus", "jmhsgapbkxwpjaaeph", "jmhsgapbkxwpjczswe", "fjjexe", "fjqdgbtn", "jmhsgodbrpypehqg", "fjjexeyqxm", "fjjex", "jmhsgap", "fjjexeyqxmu", "jmhsgapbkxwpj", "jmhsgapbkxwpjr", "jmhsgapbkxw", "f", "jmhsgapbkxwpjasrdvdccxdg", "fjjexey", "jmhsga", "fjjachqcyge", "fjjexeyqxmudu", "jmh", "fj", "jmhsgapbkxwpjaaep", "fjje", "jmhsgapbkxwpjtvv")
p1 = 2
p2 = 877179521
all_right = (disabled or RunTest(72, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 73 -----
disabled = False
p0 = ("txutwcpzpzbqpunynrmdmrvgkgu", "vewanyzncsew", "vewaphjciycigydmii", "txusa", "txusaxrpazoeiwclinaqmeprianb", "vewapvfxfj", "txuohklsmzaq", "t", "txusaxrpazoeiwclin", "txusaa", "txutwcpzpzmdjhepctx", "txusjc", "txutwcpzpz", "txusaaznaah", "txusaaznaahv", "vewapvf", "txusaazna", "vewapvfxhlwqoij", "vewapvfxhk", "txusaaznaahvyrgvgdgvgrqsxrafts", "vewapv", "vewa", "vew", "vewapvfx", "txu", "vewapvbsaaugimebtzoh", "txusaazn", "txusaxrpazoeiwclinaqmeprianbkidycqnwsfiwuz", "v", "trhlwrtbsyth", "vewapvfxh", "vewapwvcwerfyosl", "vewaptv", "txusaaznaxjncjumep", "txusaaznaahvyrgvgdgvgrqsx", "vewaphjciycigydmiiuhqcnqv", "vewxwydrhhzc", "ve", "vewap", "txusaaznaa", "vewapvfxfjoinsbkgid", "tx", "vewapvfxhkt", "vewaphjciycigydmiiuhqcnqvgljfrc", "txusaaz", "txus", "vewapvfkanidpezr", "vewapvbsaa", "txutwcpzpzbqpunynrmdmrvgk", "vewapvfxhv")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(73, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 74 -----
disabled = False
p0 = ("zjibwdnqxtt", "zjibwdnqxasyah", "ykkovsajym", "zjibwdnqx", "zjibwdn", "zjibwdnqxttfot", "ykkovsajymeumer", "zjibwdnqxsz", "zjibwv", "zjibwdnqxttfotw", "zjibwdnq", "ykkhqwzop", "y", "ykkovsajymekizfpwnbo", "ykkovsajymeumuklu", "zji", "ykkovsajymeumukluwu", "ykkovsajymekizfpwnboetccg", "ykkovkoovkk", "ykkovsajymeumuk", "ykkovsaj", "ykkovsajymeumukl", "zjv", "ykkovsa", "ykkovsajy", "zjibwdnqxt", "zjibwd", "zjibwdnqxttfo", "zjvjef", "zj", "zjvjeffy", "ykkovsajyme", "zjibwdnqxttf", "ykko", "ykkovsajymeumu", "ykkovsajymqy", "ykkovsajymeumukluw", "ykk", "ykkovsajymeu", "ykkov", "zjibw", "ykkovs", "zjibwvw", "ykkovsajymekizf", "zjibwdnqxttfotwrylbc", "yk", "zjib", "ykkovsajymeum", "zjibwdnb", "z")
p1 = 22
p2 = 0
all_right = (disabled or RunTest(74, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 75 -----
disabled = False
p0 = ("bprgijxtezs", "kdaywsobsmecphjzbfr", "kdaywsobsmecpowhr", "bprgiwgpgrs", "bprgxpeh", "bprgijx", "kdaywsobjkbmz", "bprgijxcgyasdc", "bprgijxcgyas", "kdaywsobsmecpkxdre", "b", "bprgijxcgyasdctmpgtp", "bprg", "k", "kdaywso", "bprgijxcgyasdct", "bprgijxcgya", "bpr", "kdaywsobsmec", "kdayw", "kdaywsobs", "bprgijxcgy", "bprgijxcg", "kdaywsobsmecpkxdreheex", "bprgijxcgyasd", "kdaywsobsmecpkxdr", "kdaywsob", "kdaywsoboqlui", "kdayws", "bprgi", "kdaywsobsm", "bprgijbcktnap", "kdaywsobsmess", "kdaywsobsme", "kd", "kdaywfddn", "kdaywsobsmecpkx", "kdaywsobsmejgdlzi", "kdaywsobsmecpkxdrep", "kdaywsobsmecpk", "bprgij", "bp", "kday", "bprgijxcgyasdctz", "kdaywsobsmecpowhrkqlnvyq", "kdaywsobsmecpkxd", "kdaywsobsmecpwo", "bprgijxc", "kdaywsobsmecp", "kda")
p1 = 3
p2 = 569604960
all_right = (disabled or RunTest(75, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 76 -----
disabled = False
p0 = ("xxwtezegnfoyflghobw", "wizbtnysyms", "wizbf", "xjwqyo", "x", "xxwtez", "xxwtezegnuvsrsmomqg", "xxw", "xxwtezegnf", "wizbtkujflbtjuhqztqvxaj", "xxwte", "xxwt", "wizb", "xxwtezegnuvsrsm", "xitr", "xxwtezegnuvsrsmrzuvsgpgumcjoup", "xxwtezegnuvsrsmrzuvsgpg", "wizbtnysy", "wizbtnysirplsglg", "wizhyrmg", "wizbtkujflbtju", "xxwtezegnsyo", "xkrbk", "mkauchoe", "wizbtnyzxdf", "xxwtezeg", "xxwtezegnfoyflghobwt", "wizbt", "xxwtezegnfo", "wizbtnysyprfxlrblcu", "xxwteze", "wi", "xxwtezegn", "xxwtezrciwwuah", "wizbtnysyg", "wizbtnyz", "xxwtezwbg", "bnjou", "wizbtn", "xxwtfsmwiyegtynap", "wizbtny", "w", "wizbtnys", "mkauchoejtyow", "wizbtnysydxxqwnepvo", "kndzr", "wiz", "xxwtfsm", "wizbtnysygsegatlgzjj", "xx")
p1 = 17
p2 = 0
all_right = (disabled or RunTest(76, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 77 -----
disabled = False
p0 = ("w", "whwrvoc", "k", "whwrvochnk", "wh", "kddisfkgdutyhu", "kdd", "kddisfvb", "kddisfvbr", "kdc", "kddisfkgduto", "kddisfkgdutyg", "t", "whwrvochn", "kddp", "kddisfkgdutyhan", "whw", "kddisfkgdutyha", "whwb", "whwrvochnnai", "whwrvochnn", "kddisf", "kddisfkgdutyhaw", "kddis", "kddisfr", "whwr", "whwrvo", "kd", "kdl", "whwrv", "kddisfkgdutq", "kddisfkgdu", "kddisfkgd", "whwrzs", "kddisfkgdut", "kddisfk", "kddisfkgdutyh", "kddisfke", "whwrvoch", "whwrz", "kddisfkgdutyhv", "kddisfkgduty", "kddi", "kddx", "whwrvochnnaip", "whwri", "kddisfkg", "kddisfv", "whwrir", "whwrvochnna")
p1 = 3
p2 = 711529687
all_right = (disabled or RunTest(77, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 78 -----
disabled = False
p0 = ("qtefbnxopafkqcqrln", "qtefbnx", "qtefbnxopafkqcqpjlplmkoe", "qtefbnxopaa", "qtefbnxopafkqcqputoslb", "qtefbnxg", "qtefbnxo", "qtefbnxopafkqcqqbjvsl", "usnmwomgbc", "u", "usnmwomg", "qte", "usnmwomgb", "qtefbn", "usnmwomgbcn", "us", "usgmt", "qtefbnxopafkqcqqbjvvvmy", "qtefbnxgphy", "qtef", "qtefbnxnvoxn", "usnmwom", "usnmwvzpj", "qtefbnxopa", "qtefb", "ubxykfr", "qtefbnxopafkqcqrlnkfgj", "qtefwehrg", "qtefbnxopafk", "qtefbnxopafkqcqqbjv", "qtefbnxopafkqcq", "qtb", "umwexiqno", "uvbqgsj", "qtefbnxop", "qt", "qtefbnxopafkqcqp", "usnmw", "qtefbnxopafkqcisxog", "usnm", "usnmwo", "q", "qtefbnxopafkqchitbvu", "qtelileoiku", "usnmwomgbco", "qtefbnxopafe", "qtefbnxopaf", "qtefbnxopafkq", "qtefbnxopafkqc", "usn")
p1 = 8
p2 = 133744723
all_right = (disabled or RunTest(78, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 79 -----
disabled = False
p0 = ("vbotfgss", "vbotfgssnytypseu", "vbo", "vbotfglyvin", "oqpxrinikstifgwevr", "oqpxrinikstifgw", "oqpxrinikst", "vbotfgssnyicq", "oqpx", "oqpxr", "oqpxrinik", "vbotfgssnyicqxbh", "o", "vbotfgssnyicqxb", "oqpxrin", "vbotzmu", "a", "vbotfmqfxjf", "vbot", "oqpxrinikstifgwex", "v", "oqpxrinikstifgwexgd", "vbotfg", "oqpxrinikstifgwexg", "oqpxrinikstifg", "oqpxrinikstif", "vbotfgssnyi", "vbotfgs", "oqpxrinikstifgwexgdl", "vcpdcqlje", "vbotfgssny", "oqpxriniks", "oqpxricnq", "oqpxriniksti", "vbotfgssnyicqxbdmxlmi", "oqpxrinikstifggejl", "oqpxrinikstifgwe", "oqpxrsxnr", "vbotfgssn", "oqpxrini", "oqpxrinikstifgsgl", "vbotfgssnyic", "oq", "vbotfgjlgm", "oqp", "vbotfgssnyicqx", "oqpxri", "oqpxlcor", "vb", "vbotf")
p1 = 4
p2 = 11890492
all_right = (disabled or RunTest(79, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 80 -----
disabled = False
p0 = ("pahvdiwqldcqaiww", "pahvzmo", "ppoxd", "pahvdiwqi", "kbjiqdxyl", "pahvdgmwez", "kbjiqdxylbqpvnqwffxa", "pa", "kbjikbqf", "kb", "pah", "pahvdiwql", "k", "kbjiqdxylbq", "pahvdiwqdy", "kbjmkzkrrugjj", "pahvdiwqlddifhni", "pahvdiwqldc", "kbjiqdxylbqpv", "kbjiqdxylb", "kbjiqdxy", "ppoxdso", "kbjiqdxylbqpvnqwffxxj", "pahvdiwq", "kbjiqdxylbqp", "kbjiqdxylbqpvnq", "kbjiqdyebw", "kbjiqdxylbqpvnqwgv", "pahv", "kbjiqdx", "kbjiq", "kbjiqdxylbqpvnqwff", "p", "pahvdiwqld", "kbjiqdxylbqpvnqwffeu", "kbjiqdxylbqpvnqw", "pgxtf", "kbjiqdxylbqpvnqwf", "kbjiqd", "pahvd", "kbjiqdxylbqpvnqwffj", "kbjiqdy", "kbj", "kbji", "pahvdiw", "pahvdiwqlddi", "pahvdi", "kbjiqdxylbqpvnqwffx", "kbjmkzkr", "kbjiqdxylbqpvn")
p1 = 17
p2 = 86643322
all_right = (disabled or RunTest(80, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 81 -----
disabled = False
p0 = ("xido", "xcovnakhb", "b", "glpyitxhy", "vpnlvwuc", "blmdyzs", "inj", "jxh", "aiq", "vpnl", "xco", "q", "xcovna", "jxg", "lkcudyd", "rdtdjleutlbt", "rdtdjle", "injtihvrm", "xcol", "blnem", "lkc", "vfhwdr", "xe", "i", "glpyitxi", "injtihvrjrprn", "pfh", "blgc", "rdtdrnp", "bl", "xedppgb", "jx", "rdtd", "xedppg", "rdtdrn", "ih", "glpyi", "vfhw", "sgjxr", "injtihvr", "e", "xedppgbslxjm", "injtihvrmnxwz", "pkf", "igvv", "vpnlfbpu", "zqm", "qnhit", "qyg", "adbc")
p1 = 3
p2 = 467137146
all_right = (disabled or RunTest(81, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 82 -----
disabled = False
p0 = ("tdyd", "majh", "xtrjvgymhz", "zjnrmfrhc", "evtxbvg", "ncvfd", "chgzybjy", "go", "fnd", "m", "ohr", "sf", "bdgcxx", "gcadpv", "gc", "z", "oxwanfmcp", "gwxtbuqjgh", "xtrjv", "ma", "ncvfdnkkd", "zjn", "jaij", "oxw", "zch", "gcwtif", "ncvfdobft", "fl", "g", "yrxv", "hwvqzqmydh", "tmac", "tdydx", "gx", "c", "bdgcx", "chgzy", "hwvqz", "gxb", "xiddg", "bdgcxrr", "ev", "cs", "hwvqzqm", "argmp", "jaijisc", "jvl", "kyc", "epc", "gwx")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(82, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 83 -----
disabled = False
p0 = ("fpviellnckj", "fpv", "hvdgy", "tgorqjlk", "acfr", "hvdgyzx", "awz", "zr", "srcjjhpfwfv", "baav", "srcepjdex", "baa", "bfqpy", "x", "ebapexfpjyntqeqs", "abpejvgypbqfg", "ebapexfp", "hvdgybnmicxuj", "tgorqj", "abp", "lrsgw", "bfqpyna", "cjzv", "srcjjhpfw", "shwwvger", "eb", "rg", "gqc", "omfq", "otnmuzc", "tpxat", "ebapexfppdz", "tgor", "zybry", "c", "abpejv", "ebapexfpy", "cmc", "bfqpyqmsq", "otnm", "b", "src", "hvdgyb", "sz", "tgorqjlkt", "t", "snvvf", "hvdgybj", "bdz", "shw")
p1 = 5
p2 = 472639410
all_right = (disabled or RunTest(83, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 84 -----
disabled = False
p0 = ("agnt", "r", "fbw", "npvmo", "lfkl", "cob", "kzh", "aahg", "gjai", "aahgthz", "mkdpzlwmat", "znja", "q", "lfklputtuku", "pcq", "lfklputtukuqoa", "z", "hu", "jruc", "mkdpz", "uksh", "ry", "lfkldpqjke", "ryrnclndqq", "za", "lwwlzlbqeuw", "npvmotydpxfvf", "fb", "dyf", "k", "dyfaegck", "hupo", "pmpl", "hbenf", "xz", "lwb", "t", "lw", "oul", "ktkodtmsh", "hbenfek", "u", "kjxn", "xuao", "hbenftewpqqrqe", "w", "hujcjz", "rcie", "ptkuk", "ktkodtmshceald")
p1 = 2
p2 = 930858136
all_right = (disabled or RunTest(84, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 85 -----
disabled = False
p0 = ("wdmw", "uiczkru", "skm", "s", "ycmjhpurxckhmvadvj", "skmuerm", "uic", "rcqe", "vg", "skq", "vgdzzz", "nchqxlnpidghti", "lucxjo", "xmbt", "hniz", "g", "zwkt", "capl", "lucxjrrahwfet", "nchqxlnpidght", "r", "cl", "vgdzzzgxb", "fb", "vbmm", "ykcx", "xj", "dezg", "femj", "pdjbt", "ycmjhdxxc", "ttrx", "dapnv", "nchqx", "lucx", "ycmjh", "wt", "dap", "ycmjhdxxceyvhpmgskka", "xq", "woh", "xqbbn", "wdm", "a", "mcu", "wtppwd", "pe", "wtpxfgwhqdwo", "docr", "o")
p1 = 2
p2 = 422582854
all_right = (disabled or RunTest(85, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 86 -----
disabled = False
p0 = ("netmrdrgj", "netmjqory", "hcsis", "prlp", "lhgmtwyotpqyniyncyqttbsvvlvk", "eyalhfsclyjozmn", "dbqzlptzocmjxppz", "prlpcclonakpnphtpmarashyevuddatuu", "ykowkrrs", "rvilm", "fxtvygtureiibhbyff", "ourmvsgsiul", "edncxoelancaavldcyhtegh", "qi", "lhgmt", "n", "ykbd", "yk", "lhgmtowzpfqzaw", "ourm", "vp", "vqo", "dbqz", "dbqzlptz", "fxtv", "vqoqexfnxljsfnc", "fxtvhkxymzsuuewuvs", "eoosn", "vg", "edncxoelancaavldcy", "exqy", "vgh", "bg", "prlpcclonakpnphtpm", "prlpcclonakpnphtpmb", "netmjqoryuvi", "netmdfvstdervlwa", "netmrdrgjmluxigorsscgy", "edncxoelancaavldcyasgv", "nmelme", "netm", "netmjqoryyredfhsxmljpyntlbgnl", "ey", "netmjqoryyredfhsx", "lhgmtwyotpqyniync", "ednc", "ykbdp", "lhgmtez", "i", "eyrwyqvweoowmbek")
p1 = 2
p2 = 353440983
all_right = (disabled or RunTest(86, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 87 -----
disabled = False
p0 = ("chm", "dgos", "njgnj", "lt", "ehty", "jda", "rfl", "fz", "m", "kf", "zp", "bkh", "heab", "xis", "exgda", "sui", "wpgby", "njgnjz", "vfe", "kflo", "oyvay", "inpczy", "brnd", "inpcz", "bkq", "vbito", "vbi", "iv", "wfdg", "gt", "ehtyc", "kfl", "bkv", "bk", "pzij", "njgnjzz", "vbio", "njgnjzl", "vfep", "hdq", "vfeh", "vbit", "kflm", "uzuef", "ehtycl", "lyxdi", "hdqw", "kflmk", "vbib", "chms")
p1 = 3
p2 = 617575408
all_right = (disabled or RunTest(87, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 88 -----
disabled = False
p0 = ("ck", "lehnx", "tzzo", "hnp", "fguaq", "jmk", "oue", "n", "ppdr", "safuxwffanu", "p", "zjedqwhpeipkkt", "safux", "bhvl", "jodb", "mo", "g", "aiz", "vppl", "niqhi", "lsnzunlrdztwib", "nbqe", "c", "hf", "safuxycwchtb", "safuxycw", "th", "sxoc", "xcft", "ixj", "snrtk", "hnpebd", "zac", "zjed", "fvezqhiexpscxfwaycp", "nbqeh", "a", "d", "jgd", "ukysk", "hfpv", "ou", "fve", "jmkbxiuvqvx", "fvezqhiexpscxf", "lsnzu", "fezgz", "mb", "u", "wav")
p1 = 3
p2 = 539191805
all_right = (disabled or RunTest(88, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 89 -----
disabled = False
p0 = ("yhuxjpdaiekfqkyi", "cs", "tgqo", "tpowphazosmpc", "jvdap", "jqms", "dutzvqzuu", "odner", "ii", "wxf", "dch", "w", "jzd", "iezbt", "b", "t", "bq", "hczkc", "d", "ttujahbs", "tpo", "v", "menj", "sv", "tjz", "oy", "xzco", "lcd", "pu", "tjzggsjzkfhr", "oxh", "g", "mwffxjukp", "gyt", "mwfegrgzat", "dchg", "gythaj", "khnxp", "nw", "jzdyqrziwkarsel", "cvf", "khn", "fr", "bqnyzgxi", "fqfvn", "yhuxj", "hqph", "lcdticrjkqsnn", "yhuxjqvgdrafmse", "mwf")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(89, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 90 -----
disabled = False
p0 = ("xabulv", "qsfmwmke", "qsfmu", "pnjed", "gyc", "pnjedsadgl", "ffzgathu", "ffz", "qsfm", "pnjedigek", "xxtiyb", "w", "nusr", "crhcpfyus", "ynod", "ojlr", "wu", "wzsqra", "cfkcrf", "aaa", "xa", "ffzg", "cfk", "qsfmutmm", "iceow", "crhc", "theon", "nlbmuo", "nrdeu", "x", "iceowmbqif", "nbqjv", "pnjevnv", "uvv", "qsfmildt", "k", "xeu", "q", "uvvegj", "crh", "bcho", "pnjevn", "svn", "nrdeumadl", "cfkc", "t", "nlb", "qsfmyj", "crhcf", "pnje")
p1 = 4
p2 = 741412713
all_right = (disabled or RunTest(90, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 91 -----
disabled = False
p0 = ("b", "bbbab", "bbbba", "aabba", "aa", "babb", "bbbbb", "bbaab", "abab", "ab", "aab", "bbbb", "aaba", "aaaa", "aaa", "baaab", "abbbb", "aaabb", "aaab", "aabbb", "baaaa", "bbba", "bbaa", "bbb", "aaaaa", "bb", "abbab", "baaa", "baaba", "bbab", "abba", "a", "bba", "abbb", "baba", "bab", "ba", "abaab", "abb", "bbbaa", "aabab", "aba", "aabb", "bbaba", "abaa", "baabb", "abbaa", "abbba", "baab", "baa")
p1 = 4
p2 = 175619951
all_right = (disabled or RunTest(91, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 92 -----
disabled = False
p0 = ("aa", "ab", "abbaa", "aabbb", "ababa", "aaaab", "bbaba", "aaaa", "aab", "a", "abba", "bbbb", "aaa", "baba", "abb", "bbbab", "bbbbb", "bb", "abaab", "aabab", "abaa", "aaba", "baaaa", "baa", "bbbaa", "abbba", "aaabb", "abab", "abaaa", "baaba", "bbba", "b", "bba", "abbb", "bbbba", "aba", "baab", "babb", "bbab", "babab", "ba", "bab", "aabb", "baaa", "aaaba", "ababb", "baabb", "aaaaa", "abbbb", "bbb")
p1 = 2
p2 = 806185308
all_right = (disabled or RunTest(92, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 93 -----
disabled = False
p0 = ("abab", "baa", "aabba", "abbb", "baabb", "ab", "aaba", "aaa", "b", "bbbb", "abb", "aaaaa", "bab", "aabb", "ba", "bbba", "aaaab", "bbabb", "bbbba", "bbab", "abba", "bbaba", "aab", "baaab", "aaaa", "aaab", "babb", "aba", "aabaa", "bb", "bbb", "bbaa", "abbba", "baab", "babaa", "baba", "bba", "abbaa", "abaa", "babba", "aaaba", "bbbab", "abbab", "aabbb", "abaaa", "baaa", "aabab", "a", "aaabb", "aa")
p1 = 2
p2 = 806185308
all_right = (disabled or RunTest(93, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 94 -----
disabled = False
p0 = ("baaba", "abab", "bbbb", "aaa", "baaab", "ababa", "babab", "aaba", "aaab", "bb", "abbaa", "bbb", "b", "bbbaa", "babb", "bbba", "aab", "aabb", "abaa", "aabba", "aaabb", "aa", "bbbba", "aaaab", "abaaa", "abbab", "ababb", "bbbbb", "bbaba", "bab", "baab", "babba", "bbbab", "abb", "aabbb", "baaaa", "aabab", "abbbb", "bba", "ba", "aba", "abbba", "aabaa", "abba", "bbab", "baaa", "baa", "ab", "a", "bbaa")
p1 = 4
p2 = 951381833
all_right = (disabled or RunTest(94, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 95 -----
disabled = False
p0 = ("babbb", "bab", "aaba", "baaaa", "babaa", "bbbb", "baabb", "bbaaa", "baaab", "bb", "aaaa", "babab", "baa", "baab", "a", "bba", "aaa", "ab", "aaaaa", "abbbb", "bbab", "bbb", "aba", "aabaa", "aaaab", "babb", "baaa", "aabab", "aabba", "bbaa", "baaba", "baba", "aabbb", "aab", "ba", "abbba", "bbbab", "bbba", "bbaab", "aaabb", "abb", "bbabb", "b", "abba", "abbb", "aaab", "bbbba", "aabb", "aa", "abab")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(95, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 96 -----
disabled = False
p0 = ("baca", "acac", "cca", "acaa", "ccb", "bb", "abbc", "bbcab", "baaa", "acb", "a", "b", "bcb", "aacc", "c", "bbaa", "abb", "abbbc", "bcccc", "bbcaa", "ccabb", "ccab", "aa", "ba", "cbcaa", "abcbc", "aab", "bacbb", "cbbb", "aabab", "abaa", "cb", "cabba", "ab", "cbc", "baa", "aabc", "bc", "cac", "bcaa", "abcaa", "caa", "aabb", "abca", "cc", "accba", "baacb", "cbba", "acbcc", "bacb")
p1 = 5
p2 = 472639410
all_right = (disabled or RunTest(96, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 97 -----
disabled = False
p0 = ("acac", "aaab", "bcb", "acacb", "bacbc", "c", "bcc", "aabc", "bacab", "baab", "baca", "bba", "abc", "cac", "cca", "bbaa", "baccb", "ba", "cbca", "cb", "bb", "cc", "a", "bcbba", "ac", "bbbab", "aa", "ccacb", "ca", "b", "cbcab", "bca", "acb", "ccc", "aaa", "bbcb", "bc", "cbc", "cab", "abbcc", "ab", "cbbc", "acbb", "bccb", "bab", "caaa", "acbc", "abaca", "cbbbb", "acaba")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(97, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 98 -----
disabled = False
p0 = ("cca", "bcaa", "ab", "ccc", "acabb", "cbcac", "aaacc", "bbcab", "a", "babcb", "b", "aabca", "baaa", "abbc", "abbbc", "ccaa", "cbcb", "aabaa", "aacb", "baa", "aba", "ccb", "bbccc", "bb", "acc", "acaa", "ca", "abc", "aa", "cbca", "aaa", "c", "acca", "aacaa", "bcbba", "cc", "cac", "abca", "cbbc", "abb", "cbaa", "cb", "bacc", "cab", "bcb", "ba", "ccaab", "bccb", "ccbca", "ccca")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(98, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 99 -----
disabled = False
p0 = ("abacc", "ccb", "aaac", "aa", "c", "aabb", "bc", "cbbcc", "abbab", "bba", "b", "bccbb", "ccac", "cbcb", "ccccc", "bbaa", "ca", "cccb", "bb", "abaa", "acaaa", "aab", "caba", "bbab", "bca", "acc", "aaaa", "babb", "a", "caabb", "baacc", "bac", "bab", "ba", "aaaba", "acbbc", "aabaa", "ccba", "ac", "cac", "abcba", "aacb", "abac", "cccaa", "bcabc", "bbcac", "cbcca", "aaccc", "cbac", "cc")
p1 = 3
p2 = 934274292
all_right = (disabled or RunTest(99, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 100 -----
disabled = False
p0 = ("acb", "aacc", "cbb", "cb", "a", "bcca", "ca", "ba", "bbb", "abaaa", "cab", "aaac", "aaaa", "abcc", "babaa", "bbbc", "bb", "c", "aab", "b", "caac", "acc", "bba", "acabb", "acaac", "cbcba", "abbab", "ccca", "abc", "aa", "baba", "cca", "acbbb", "acbc", "baa", "ab", "cbbb", "bbcac", "cbbc", "ccaba", "cc", "bc", "acaca", "cabbb", "cbaa", "ababa", "bcbac", "abaa", "acaaa", "aaaba")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(100, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 101 -----
disabled = False
p0 = ("bb", "bcba", "c", "ccbc", "ccbca", "dd", "aabc", "a", "cc", "ba", "bccab", "bddb", "bbcd", "adabc", "dacc", "ddba", "dcb", "cab", "d", "baac", "adaad", "b", "dc", "cbdca", "cacac", "cdb", "db", "bccd", "cdbc", "dcaa", "dbadc", "dbbcd", "aa", "bca", "ad", "aac", "dcbb", "bddad", "cacb", "ddcad", "bcbb", "bcc", "da", "bbddc", "addbc", "acb", "accbc", "bcac", "bdd", "cbddd")
p1 = 3
p2 = 699123483
all_right = (disabled or RunTest(101, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 102 -----
disabled = False
p0 = ("acadb", "b", "bcac", "cdcb", "bdc", "aacc", "cbaa", "dba", "daab", "bc", "abbd", "cb", "adac", "cbbd", "aaa", "bac", "d", "a", "daa", "dca", "ad", "cdb", "cdaa", "cdac", "abdbd", "ccb", "abcc", "dbd", "cbcad", "da", "cdc", "ccbc", "aa", "bdb", "bbdd", "cbdcc", "cdd", "ca", "ccddb", "cbbb", "ddbb", "babdd", "c", "dada", "abac", "bcab", "ab", "aadb", "ccabd", "dcabb")
p1 = 5
p2 = 0
all_right = (disabled or RunTest(102, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 103 -----
disabled = False
p0 = ("dbadd", "acd", "ccdb", "ba", "caddb", "bb", "caad", "acacb", "bda", "a", "ab", "dc", "cc", "aabdb", "cbaca", "bba", "cbb", "cbca", "cdc", "bdbbb", "acdbd", "c", "cacc", "abada", "dbd", "dd", "ddb", "ad", "aaaab", "aa", "d", "db", "adb", "dab", "adabd", "bd", "daaad", "abdac", "bbb", "cbad", "bdaa", "abda", "cb", "da", "b", "bbc", "ddcd", "bbd", "bdb", "bbbda")
p1 = 6
p2 = 0
all_right = (disabled or RunTest(103, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 104 -----
disabled = False
p0 = ("dbd", "cdb", "ac", "a", "adcda", "bbbdc", "b", "bbaad", "bcca", "bada", "abad", "bdacb", "bbcb", "cdcba", "baab", "dccd", "cca", "aba", "bcccc", "ccac", "daacd", "aadc", "cbd", "dbdcd", "cc", "bcbcc", "bacdd", "d", "dac", "bcdcd", "ca", "dcddb", "bca", "dca", "bddcd", "bdbd", "cdcbc", "cd", "dbdb", "ddc", "aabd", "dcaa", "cccb", "ddd", "caacc", "bdac", "dda", "ddbc", "daab", "c")
p1 = 6
p2 = 0
all_right = (disabled or RunTest(104, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 105 -----
disabled = False
p0 = ("ca", "ddb", "c", "ad", "dca", "bbccd", "abd", "cbad", "babb", "bacad", "dd", "ccc", "ddbcc", "cda", "dbc", "ac", "bcdd", "cb", "a", "d", "babdd", "db", "add", "da", "ccaac", "ba", "aca", "cbcd", "ada", "bbdb", "cab", "aadbc", "aa", "bddcd", "dc", "daadc", "dddbd", "bcd", "cc", "bc", "bd", "bcc", "bdada", "cbb", "cad", "cadc", "b", "bbbb", "bab", "ccdc")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(105, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 106 -----
disabled = False
p0 = ("dbecc", "e", "eeada", "eba", "cee", "d", "aaaac", "ccd", "abe", "abbde", "ed", "addb", "ecbdd", "ecce", "bcc", "cd", "ebe", "dbd", "cba", "aabbd", "dc", "aaabb", "dea", "dabdb", "aed", "dbea", "dbee", "c", "bb", "bcbaa", "dbda", "cabe", "eac", "da", "ee", "acdb", "cac", "dad", "eaaee", "caab", "b", "ddc", "a", "eb", "aeedc", "cdbe", "bcbee", "be", "ddbce", "ccbc")
p1 = 1
p2 = 318608048
all_right = (disabled or RunTest(106, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 107 -----
disabled = False
p0 = ("eaa", "aaccd", "cbab", "cedca", "acda", "cb", "dad", "ca", "ae", "eeeb", "cddde", "ebecd", "cece", "dcdce", "bdad", "add", "ecebb", "ebd", "eb", "abd", "deab", "bde", "aecce", "bedaa", "a", "eac", "aebab", "c", "bbe", "eed", "e", "aeded", "bbeba", "baea", "acba", "eea", "cc", "bbbe", "deeb", "ebb", "aea", "caed", "eeabd", "ccdc", "ceca", "baac", "b", "cbb", "edec", "daab")
p1 = 4
p2 = 0
all_right = (disabled or RunTest(107, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 108 -----
disabled = False
p0 = ("ca", "cdacd", "bdac", "bcec", "bebdd", "edd", "adb", "cdab", "bae", "aaeca", "edbbe", "bab", "eacbd", "cceb", "baaa", "d", "c", "cd", "dd", "bcae", "ebd", "ebc", "dadb", "bbb", "ceacb", "adbcd", "dce", "dab", "bbe", "ccece", "bda", "ccdea", "cecea", "eccb", "e", "be", "a", "cbb", "cde", "ab", "b", "cbc", "ad", "eaa", "dc", "daac", "bbda", "ababc", "da", "ba")
p1 = 6
p2 = 0
all_right = (disabled or RunTest(108, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 109 -----
disabled = False
p0 = ("ebac", "daeac", "bacc", "bbca", "ddabb", "a", "bdbbd", "bccea", "c", "ec", "dc", "dcb", "aaca", "ddbdb", "bddb", "bbbc", "dcc", "dbbbd", "abe", "cccdd", "acc", "bd", "ee", "adbc", "ebea", "bedba", "cdade", "acad", "bedbd", "aeadc", "decdd", "eaab", "e", "acd", "debd", "cbcd", "d", "de", "eb", "cd", "dbed", "dddca", "dbb", "bdeaa", "bba", "adee", "dcae", "eeea", "abdad", "abb")
p1 = 3
p2 = 463972674
all_right = (disabled or RunTest(109, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 110 -----
disabled = False
p0 = ("ca", "aaace", "dae", "aaa", "bbbb", "dc", "abc", "bae", "debc", "eeddb", "c", "dcac", "bcdd", "ebbcc", "ac", "beaaa", "e", "edcd", "bee", "abddb", "adbdb", "cdcd", "eae", "aaec", "aed", "eaeac", "ccee", "cbb", "dec", "bddaa", "b", "ba", "ada", "ad", "caba", "cae", "bdc", "cc", "aa", "bbcaa", "adbdd", "bbc", "ddaac", "a", "d", "eabcc", "beae", "acac", "beeb", "ccdee")
p1 = 3
p2 = 235150809
all_right = (disabled or RunTest(110, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 111 -----
disabled = False
p0 = ("aecc", "d", "ced", "cfcdf", "aacdf", "dcb", "a", "ea", "f", "eaafc", "ffdd", "ec", "ddae", "fda", "afcfa", "aedbe", "e", "bfdd", "dbeea", "df", "edde", "cdaf", "afc", "cab", "db", "affb", "aec", "bff", "fc", "ecd", "ef", "ccbe", "b", "befc", "beab", "cbde", "ae", "c", "bc", "cbc", "daed", "faebb", "cdab", "dbca", "da", "afb", "eaee", "ad", "be", "cceed")
p1 = 6
p2 = 0
all_right = (disabled or RunTest(111, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 112 -----
disabled = False
p0 = ("f", "bead", "bae", "d", "aee", "eaacc", "cced", "ebfdc", "bdd", "fdc", "acfbc", "ecbaf", "be", "ef", "aa", "dbddd", "cacdf", "cfbf", "aaf", "ae", "e", "eacb", "bc", "cbd", "ffeca", "cbba", "ea", "ead", "bffdd", "dff", "fba", "dda", "edde", "dbe", "afdc", "fac", "dd", "ccf", "caade", "bcdd", "eebb", "a", "cbe", "c", "addba", "cbb", "afa", "deac", "bf", "b")
p1 = 3
p2 = 463972674
all_right = (disabled or RunTest(112, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 113 -----
disabled = False
p0 = ("d", "ceb", "aaefd", "b", "defa", "a", "ccfeb", "eabdc", "bceac", "c", "cadaa", "f", "fedb", "dfd", "daea", "cd", "dda", "dfbc", "babb", "fddf", "ce", "aed", "bcfd", "ac", "dc", "bce", "ae", "ee", "ebffa", "ea", "cea", "acdfc", "facce", "e", "bb", "cecfe", "dbcf", "eec", "cf", "fbeb", "bc", "af", "abbfd", "da", "feec", "bf", "daef", "fd", "aff", "ba")
p1 = 2
p2 = 624129181
all_right = (disabled or RunTest(113, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 114 -----
disabled = False
p0 = ("bcada", "d", "dfb", "dbee", "abafc", "acaff", "fb", "ec", "edb", "eebfd", "fffcc", "aa", "daa", "fa", "be", "ddcbb", "bea", "bca", "fef", "ce", "de", "ccf", "abbcf", "bcece", "dcbfb", "afece", "ca", "faaa", "aadfd", "ddde", "cebed", "ccb", "aae", "f", "ebeef", "fedbd", "b", "dced", "cf", "dbafd", "a", "fbb", "ab", "aade", "faafd", "fd", "eebd", "ccded", "deb", "e")
p1 = 3
p2 = 310369940
all_right = (disabled or RunTest(114, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 115 -----
disabled = False
p0 = ("debfd", "fdedc", "cdaff", "aefdb", "edb", "feec", "dc", "cddfa", "aa", "dece", "edd", "c", "acfff", "dcae", "eee", "ba", "dcd", "ccbc", "ddbf", "cf", "f", "dfafe", "adfe", "fdbce", "dcab", "cfbe", "fdcb", "dfca", "cc", "a", "aaad", "fcefc", "eca", "ccef", "ff", "ddbef", "aad", "eb", "baf", "dafec", "ebdb", "fae", "aefe", "cdf", "ad", "d", "eecde", "bcad", "dddbe", "eed")
p1 = 6
p2 = 0
all_right = (disabled or RunTest(115, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 116 -----
disabled = False
p0 = ("kenta", "kentaro", "ken")
p1 = 2
p2 = 3
all_right = (disabled or RunTest(116, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 117 -----
disabled = False
p0 = ("alice", "bob", "charlie")
p1 = 1
p2 = 6
all_right = (disabled or RunTest(117, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 118 -----
disabled = False
p0 = ("a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "b", "bc", "bcd", "bcde", "bcdef", "bcdefg", "bcdefgh", "bcdefghi", "bcdefghij", "bcdefghijk", "c", "cd", "cde", "cdef", "cdefg", "cdefgh", "cdefghi", "cdefghij", "cdefghijk", "cdefghijkl", "d", "de", "def", "defg", "defgh", "defghi", "defghij", "defghijk", "defghijkl", "defghijklm", "e", "ef", "efg", "efgh", "efghi", "efghij", "efghijk", "efghijkl", "efghijklm", "efghijklmn")
p1 = 8
p2 = 42475263
all_right = (disabled or RunTest(118, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 119 -----
disabled = False
p0 = ("ryota", "ryohei", "ryotaro", "ryo", "ryoga", "ryoma", "ryoko", "ryosuke", "ciel", "lun", "ryuta", "ryuji", "ryuma", "ryujiro", "ryusuke", "ryutaro", "ryu", "ryuhei", "ryuichi", "evima")
p1 = 3
p2 = 276818566
all_right = (disabled or RunTest(119, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 120 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 46
p2 = 5527200
all_right = (disabled or RunTest(120, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 121 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 40
p2 = 762363706
all_right = (disabled or RunTest(121, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 122 -----
disabled = False
p0 = ("aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "aaaaaaaaaaa", "aaaaaaaaaaaa", "aaaaaaaaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
p1 = 35
p2 = 793470785
all_right = (disabled or RunTest(122, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 123 -----
disabled = False
p0 = ("taro", "jiro", "hanako")
p1 = 2
p2 = 0
all_right = (disabled or RunTest(123, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 124 -----
disabled = False
p0 = ("hideo", "hideto", "hideki", "hide")
p1 = 2
p2 = 6
all_right = (disabled or RunTest(124, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 125 -----
disabled = False
p0 = ("k", "kk", "kkk", "kkkk", "kkkkk", "kkkkkk", "kkkkkkk", "kkkkkkkk", "kkkkkkkkk", "kkkkkkkkkk", "kkkkkkkkkkk", "kkkkkkkkkkkk", "kkkkkkkkkkkkk", "kkkkkkkkkkkkkk", "kkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
p1 = 13
p2 = 721549524
all_right = (disabled or RunTest(125, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 126 -----
disabled = False
p0 = ("aswexsexsdaswexsexsdaswexsexsdaswexsexsdaswexsexsd", "aswexsexsdaswexsexsdaswexsexsdaswexsexsdaswexsexs", "aswexsexsdaswexsexsdaswexsexsdaswexsexsdaswexsex", "aswexsexsdaswexsexsdaswexsexsdaswexsexsdaswexse", "aswexsexsdaswexsexsdaswexsexsdaswexsexsdaswexs", "aswexsexsdaswexsexsdaswexsexsdaswexsexsdaswex", "aswexsexsdaswexsexsdaswexsexsdaswexsexsdaswe", "aswexsexsdaswexsexsdaswexsexsdaswexsexsdasw", "aswexsexsdaswexsexsdaswexsexsdaswexsexsdas", "aswexsexsdaswexsexsdaswexsexsdaswexsexsda", "aswexsexsdaswexsexsdaswexsexsdaswexsexsd", "aswexsexsdaswexsexsdaswexsexsdaswexsexs", "aswexsexsdaswexsexsdaswexsexsdaswexsex", "aswexsexsdaswexsexsdaswexsexsdaswexse", "aswexsexsdaswexsexsdaswexsexsdaswexs", "aswexsexsdaswexsexsdaswexsexsdaswex", "aswexsexsdaswexsexsdaswexsexsdaswe", "aswexsexsdaswexsexsdaswexsexsdasw", "aswexsexsdaswexsexsdaswexsexsdas", "aswexsexsdaswexsexsdaswexsexsda", "aswexsexsdaswexsexsdaswexsexsd", "aswexsexsdaswexsexsdaswexsexs", "aswexsexsdaswexsexsdaswexsex", "aswexsexsdaswexsexsdaswexse", "aswexsexsdaswexsexsdaswexs", "aswexsexsdaswexsexsdaswex", "aswexsexsdaswexsexsdaswe", "aswexsexsdaswexsexsdasw", "aswexsexsdaswexsexsdas", "aswexsexsdaswexsexsda", "aswexsexsdaswexsexsd", "aswexsexsdaswexsexs", "aswexsexsdaswexsex", "aswexsexsdaswexse", "aswexsexsdaswexs", "aswexsexsdaswex", "aswexsexsdaswe", "aswexsexsdasw", "aswexsexsdas", "aswexsexsda", "aswexsexsd", "aswexsexs", "aswexsex", "aswexse", "aswexs", "aswex", "aswe", "asw", "as", "a")
p1 = 31
p2 = 14132508
all_right = (disabled or RunTest(126, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 127 -----
disabled = False
p0 = ("k", "km", "kmn", "kmnf", "kmnfq", "kmnfqq", "kmnfqqd", "kmnfqqda", "kmnfqqdad", "kmnfqqdads", "kmnfqqdadsd", "kmnfqqdadsdj", "kmnfqqdadsdjd", "kmnfqqdadsdjdv", "kmnfqqdadsdjdvn", "kmnfqqdadsdjdvna", "kmnfqqdadsdjdvnak", "kmnfqqdadsdjdvnakd", "kmnfqqdadsdjdvnakdf", "kmnfqqdadsdjdvnakdfy", "kmnfqqdadsdjdvnakdfyb", "kmnfqqdadsdjdvnakdfybt", "kmnfqqdadsdjdvnakdfybtl", "kmnfqqdadsdjdvnakdfybtll", "kmnfqqdadsdjdvnakdfybtlle", "kmnfqqdadsdjdvnakdfybtllev", "kmnfqqdadsdjdvnakdfybtllevr", "kmnfqqdadsdjdvnakdfybtllevrx", "kmnfqqdadsdjdvnakdfybtllevrxj", "kmnfqqdadsdjdvnakdfybtllevrxjs", "kmnfqqdadsdjdvnakdfybtllevrxjsl", "kmnfqqdadsdjdvnakdfybtllevrxjsll", "kmnfqqdadsdjdvnakdfybtllevrxjsllt", "kmnfqqdadsdjdvnakdfybtllevrxjsllti", "kmnfqqdadsdjdvnakdfybtllevrxjslltij", "kmnfqqdadsdjdvnakdfybtllevrxjslltijk", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkz", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzi", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzin", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinn", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinno", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinnof", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinnofm", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinnofmk", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinnofmke", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinnofmkew", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinnofmkewr", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinnofmkewrc", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinnofmkewrcj", "kmnfqqdadsdjdvnakdfybtllevrxjslltijkzinnofmkewrcjg")
p1 = 45
p2 = 254251200
all_right = (disabled or RunTest(127, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 128 -----
disabled = False
p0 = ("a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn", "abcdefghijklmno", "abcdefghijklmnop", "abcdefghijklmnopq", "abcdefghijklmnopqr", "abcdefghijklmnopqrs", "abcdefghijklmnopqrst", "abcdefghijklmnopqrsta", "abcdefghijklmnopqrstaa", "abcdefghijklmnopqrstaaa", "abcdefghijklmnopqrstaaaa", "abcdefghijklmnopqrstaaaaa", "abcdefghijklmnopqrstaaaaaa", "abcdefghijklmnopqrstaaaaaaa", "abcdefghijklmnopqrstaaaaaaaa")
p1 = 24
p2 = 491400
all_right = (disabled or RunTest(128, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 129 -----
disabled = False
p0 = ("a", "aa", "aaa", "aaaa")
p1 = 4
p2 = 1
all_right = (disabled or RunTest(129, p0, p1, True, p2) ) and all_right
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
