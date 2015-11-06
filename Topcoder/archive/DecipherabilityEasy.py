class DecipherabilityEasy:
    def check(self, s, t):
        for i in range(len(s)):
            if s[:i] + s[i + 1:] == t:
                return "Possible"
        return "Impossible"


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, p1, hasAnswer, p2):
    obj = DecipherabilityEasy()
    startTime = time.clock()
    answer = obj.check(p0, p1)
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
p0 = "sunuke"
p1 = "snuke"
p2 = "Possible"
all_right = (disabled or RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = "snuke"
p1 = "skue"
p2 = "Impossible"
all_right = (disabled or RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = "snuke"
p1 = "snuke"
p2 = "Impossible"
all_right = (disabled or RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = "snukent"
p1 = "snuke"
p2 = "Impossible"
all_right = (disabled or RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = "aaaaa"
p1 = "aaaa"
p2 = "Possible"
all_right = (disabled or RunTest(4, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = "aaaaa"
p1 = "aaa"
p2 = "Impossible"
all_right = (disabled or RunTest(5, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = "topcoder"
p1 = "tpcoder"
p2 = "Possible"
all_right = (disabled or RunTest(6, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = "singleroundmatch"
p1 = "singeroundmatc"
p2 = "Impossible"
all_right = (disabled or RunTest(7, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = "aa"
p1 = "a"
p2 = "Possible"
all_right = (disabled or RunTest(8, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = "ab"
p1 = "a"
p2 = "Possible"
all_right = (disabled or RunTest(9, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = "ab"
p1 = "b"
p2 = "Possible"
all_right = (disabled or RunTest(10, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = "abc"
p1 = "ab"
p2 = "Possible"
all_right = (disabled or RunTest(11, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = "ab"
p1 = "c"
p2 = "Impossible"
all_right = (disabled or RunTest(12, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = "abc"
p1 = "ac"
p2 = "Possible"
all_right = (disabled or RunTest(13, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = "abc"
p1 = "b"
p2 = "Impossible"
all_right = (disabled or RunTest(14, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = "abc"
p1 = "aac"
p2 = "Impossible"
all_right = (disabled or RunTest(15, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = "ildzzupqqopaizfrwzmebdkuhjjmagwitsbmmrzbgrifpxyk"
p1 = "ildzzupqqopaifrwzmebdkuhjjmagwitsbmmrzbgrifpxyk"
p2 = "Possible"
all_right = (disabled or RunTest(16, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = "ligjjcdifqrfdamwmlqyzfdxylcaeahgcfzdyexdhxbccalpg"
p1 = "ligjjcdifqrfdamwmlqyzfdxylcaeahgcfzdyexhxbccalpg"
p2 = "Possible"
all_right = (disabled or RunTest(17, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = "dvyqkcuowtszmmarlhzmgmnqqnxrqkn"
p1 = "dvqkcuowtszmmarlhzmgmnqqnxrqkn"
p2 = "Possible"
all_right = (disabled or RunTest(18, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = "feipwxwoghejqcmaxvavqtwfgejhohyuyvufvdnl"
p1 = "feipxwoghejqcmaxvavqtwfgejhohyuyvufvdnl"
p2 = "Possible"
all_right = (disabled or RunTest(19, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = "jjvmjfcqlklwycceifpolickmabpujypdddkiksgowhduvf"
p1 = "jjvmjcqlklwycceifpolickmabpujypdddkiksgowhduvf"
p2 = "Possible"
all_right = (disabled or RunTest(20, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = "gtlaozuyoasojsvtxijopwxaeyfchxszmg"
p1 = "gtlaozuyoaojsvtxijopwxaeyfchxszmg"
p2 = "Possible"
all_right = (disabled or RunTest(21, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = "tsxjarccqzjveufxeaydzlwimsygniooihykmcsbwbtdprj"
p1 = "tsxjarccqzjveufxeaydzlwimsygnioohykmcsbwbtdprj"
p2 = "Possible"
all_right = (disabled or RunTest(22, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = "oeomnyundnxvqnpjbsddvslharvdmltqpmkilki"
p1 = "oeomnyundnxvqnpjbsddvslhavdmltqpmkilki"
p2 = "Possible"
all_right = (disabled or RunTest(23, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = "rdqhdmvzfjzlojmakdijvobgqdjkuffthkuohffzcpurkso"
p1 = "rdqhdmvzfjzlojmakdijvobgqdjkuffthkohffzcpurkso"
p2 = "Possible"
all_right = (disabled or RunTest(24, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = "yqtikjgerlfninryzowihtjzrgofrgaggtymhrxcczzclsw"
p1 = "yqtikjgerlfninryzowihtjzrgofrgggtymhrxcczzclsw"
p2 = "Possible"
all_right = (disabled or RunTest(25, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = "ydxzlcnhnhpjatmkgnhqbeecsdctepnxsa"
p1 = "ydxzlcnhnhpjatmkgnhqbeecsdctenxsa"
p2 = "Possible"
all_right = (disabled or RunTest(26, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = "rqxvzargeewzkuupotpsmedcirebocvsb"
p1 = "rqxvzargeewzkuuotpsmedcirebocvsb"
p2 = "Possible"
all_right = (disabled or RunTest(27, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = "tzwvuvipfxggtufhhcyrtvbbogdeomdngdvvmkchct"
p1 = "tzwvuvipfxggtufhcyrtvbbogdeomdngdvvmkchct"
p2 = "Possible"
all_right = (disabled or RunTest(28, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = "iuxpfdqlerypakpmavlejtfecsmnyersikytwucoddu"
p1 = "iuxpfdqlerypakpmavlejtfecsmnyersikytwuoddu"
p2 = "Possible"
all_right = (disabled or RunTest(29, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = "gjwoodxzmgnwrzjrkuspvzqzqfekzmnfjzof"
p1 = "gjwoodxzmgnwrzjrkuspvzqzqekzmnfjzof"
p2 = "Possible"
all_right = (disabled or RunTest(30, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = "qfpmqegpfjjtbxyfpzwmnavxpinffpccyqlpvjqxikcjphlbg"
p1 = "qpmqegpfjjtbxyfpzwmnavxpinffpccyqlpvjqxikcjphlbg"
p2 = "Possible"
all_right = (disabled or RunTest(31, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = "exqbugsgoydmkeetjlpjppebocwtshmfhrwuyyofwraykeb"
p1 = "exqbugsgoydmkeetjlpjppebcwtshmfhrwuyyofwraykeb"
p2 = "Possible"
all_right = (disabled or RunTest(32, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = "kpfbcumoyohhphyxobjxszmvaqhnycgwdwlztljxi"
p1 = "kpfbcumoyohhphyxobjxszmvaqnycgwdwlztljxi"
p2 = "Possible"
all_right = (disabled or RunTest(33, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = "hunrnueavcgknzdnxynllqaceveymjarezosbdqrwl"
p1 = "hunrnueavcgnzdnxynllqaceveymjarezosbdqrwl"
p2 = "Possible"
all_right = (disabled or RunTest(34, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = "oebybdgxrnezovpokxygqaidnqnuqbqpqayjco"
p1 = "oebybdgxrnezovpokxygaidnqnuqbqpqayjco"
p2 = "Possible"
all_right = (disabled or RunTest(35, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = "xtbxwjvnsueklslwaqdwlaknavvohwszkqjmtubhu"
p1 = "xtbxwjvnsuekllwaqdwlaknavvohwszkqjmtubhu"
p2 = "Possible"
all_right = (disabled or RunTest(36, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = "bbxhfyfhvcohnikfidtmlsdvmhkkyfokaewxopdjjilgf"
p1 = "bbxhfyfhvcohnikfidtmlsdvmhkkyfkaewxopdjjilgf"
p2 = "Possible"
all_right = (disabled or RunTest(37, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = "subedzqbrlfffroikjvxebvbrdfheucxgbptmrccdmnpoxpd"
p1 = "subedzqbrlfffroikjvxebvbrdfheucgbptmrccdmnpoxpd"
p2 = "Possible"
all_right = (disabled or RunTest(38, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = "smtzzvvvyzvdsntpzciwwzgulsjnserwiycinchcyeyoqd"
p1 = "smtzzvvvyzvdsntpzciwwzguljnserwiycinchcyeyoqd"
p2 = "Possible"
all_right = (disabled or RunTest(39, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = "bjxpmdkexyjqdjsqvvdnhygzddmvmerzgum"
p1 = "bjxpmdkeyjqdjsqvvdnhygzddmvmerzgum"
p2 = "Possible"
all_right = (disabled or RunTest(40, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = "bjusjvvvmmqvrifxuslxcyfkpgzeagrhz"
p1 = "bjusjvvvmmqvrifxuslxcyfkpgzeaghz"
p2 = "Possible"
all_right = (disabled or RunTest(41, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = "scwdsfiifsgxooxhalbrpfhkkvcokpbwuvztbndfpw"
p1 = "scwdsiifsgxooxhalbrpfhkkvcokpbwuvztbndfpw"
p2 = "Possible"
all_right = (disabled or RunTest(42, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = "ijzuunzjsjbrclauzzfszranpvyaudcqdhmpntacbwsy"
p1 = "ijzuunzjsjbrclauzzfszranpvyadcqdhmpntacbwsy"
p2 = "Possible"
all_right = (disabled or RunTest(43, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = "svfgfqftrygfeklvutbntlpedjrvdhgsib"
p1 = "svfgfftrygfeklvutbntlpedjrvdhgsib"
p2 = "Possible"
all_right = (disabled or RunTest(44, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = "dbhevbgilatmzjvdmmvvahdcgzobwwhupvzsaygv"
p1 = "dbhevbglatmzjvdmmvvahdcgzobwwhupvzsaygv"
p2 = "Possible"
all_right = (disabled or RunTest(45, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = "iiyokoiyo"
p1 = "iyokoiyo"
p2 = "Possible"
all_right = (disabled or RunTest(46, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = "iiyokoiyo"
p1 = "iiyokoiy"
p2 = "Possible"
all_right = (disabled or RunTest(47, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = "ccacbacaaaacca"
p1 = "cccbacaaaacca"
p2 = "Possible"
all_right = (disabled or RunTest(48, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = "caaabbbacbaababaccccabacabacabbbbbab"
p1 = "caaabbbacbaababaccccbbacaaacabbbbab"
p2 = "Impossible"
all_right = (disabled or RunTest(49, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = "abaaabcaabccac"
p1 = "abaaaacaabccb"
p2 = "Impossible"
all_right = (disabled or RunTest(50, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = "cccccaacabaacaacbbcbaaabaacabaacbbbbbabcaaa"
p1 = "cccaaaccbaacaacbbcbaaabaacabaacbbbbbabcaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(51, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = "cacbababaaaccacbccbbcbacb"
p1 = "cacbababaaccbcbccbbcbaca"
p2 = "Impossible"
all_right = (disabled or RunTest(52, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = "aabcacbacbbbbbbcccbcccacbcaaababcbabcbbabbbbb"
p1 = "aabcacbacbbcbbbcccbcbcacbcaaababcbabbbabbbbb"
p2 = "Impossible"
all_right = (disabled or RunTest(53, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 54 -----
disabled = False
p0 = "cacbbaacaaccaacbacababbbbbabccccaaabba"
p1 = "cacbbaacaaccaacbacababbbbabcbccaaabca"
p2 = "Impossible"
all_right = (disabled or RunTest(54, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 55 -----
disabled = False
p0 = "bcccccbaabcccacbbaabcaccacacaaaabacccaa"
p1 = "accccbaabcccacbbaabcaccacacaababacccaa"
p2 = "Impossible"
all_right = (disabled or RunTest(55, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 56 -----
disabled = False
p0 = "aabccccbabaabacaab"
p1 = "aabccccbabaaacaab"
p2 = "Possible"
all_right = (disabled or RunTest(56, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 57 -----
disabled = False
p0 = "baabcbcab"
p1 = "aabcbcbb"
p2 = "Impossible"
all_right = (disabled or RunTest(57, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 58 -----
disabled = False
p0 = "cbacbccb"
p1 = "cbacccb"
p2 = "Possible"
all_right = (disabled or RunTest(58, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 59 -----
disabled = False
p0 = "cbaabccc"
p1 = "abcabcc"
p2 = "Impossible"
all_right = (disabled or RunTest(59, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 60 -----
disabled = False
p0 = "bcbacbcbccbbbabccabcbaab"
p1 = "bcbbbcbccbbcabccabcbaab"
p2 = "Impossible"
all_right = (disabled or RunTest(60, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 61 -----
disabled = False
p0 = "acaacbbccab"
p1 = "aaccbbccab"
p2 = "Impossible"
all_right = (disabled or RunTest(61, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 62 -----
disabled = False
p0 = "aabbbacbcacabbbbccbbabababc"
p1 = "baabbcbcacabbbbccbbabababc"
p2 = "Impossible"
all_right = (disabled or RunTest(62, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 63 -----
disabled = False
p0 = "cccaabcaccbbcccacaaaacbcabc"
p1 = "cacaabcaccbbcccacaaaccbcbc"
p2 = "Impossible"
all_right = (disabled or RunTest(63, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 64 -----
disabled = False
p0 = "bccbabbbbacacaabccbbbabacaabbc"
p1 = "bcbbabbbacacaabccbbcabacaabbc"
p2 = "Impossible"
all_right = (disabled or RunTest(64, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 65 -----
disabled = False
p0 = "bcccacccbabbaaaccacacbcbaaaacbcaccbaababbbcbcbcb"
p1 = "bcccacccbabbaaaccacacbcbaaaabcaccbaababbbcbcbcb"
p2 = "Possible"
all_right = (disabled or RunTest(65, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 66 -----
disabled = False
p0 = "babccaccbbbbacaacaabaccbacacbacbc"
p1 = "babccaccbbbbacaacaabacccaacbacbb"
p2 = "Impossible"
all_right = (disabled or RunTest(66, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 67 -----
disabled = False
p0 = "babbabbacbccbabaacacbbaccacbcbbaaccaccbcccbb"
p1 = "babbabbacbccbabaacacbbaccacbcbbaaccaccbccbb"
p2 = "Possible"
all_right = (disabled or RunTest(67, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 68 -----
disabled = False
p0 = "bcacbbacc"
p1 = "bcacbbac"
p2 = "Possible"
all_right = (disabled or RunTest(68, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 69 -----
disabled = False
p0 = "ccbabbaaacbbaaaaabaaaba"
p1 = "ccbabbaaacbbaaaaaaaaba"
p2 = "Possible"
all_right = (disabled or RunTest(69, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 70 -----
disabled = False
p0 = "caaaaaabcbcbcabcbabbabacaacbcbabcababbbabacbcbbba"
p1 = "caaaaaabcbcacabcbabbabacaacbcbbbcababbbababcbbba"
p2 = "Impossible"
all_right = (disabled or RunTest(70, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 71 -----
disabled = False
p0 = "ccbbbcaacaacbaaaaccccbabaccacccbacccc"
p1 = "ccbbbcaaccaabaaaaccccbabaccacccacccc"
p2 = "Impossible"
all_right = (disabled or RunTest(71, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 72 -----
disabled = False
p0 = "bbaaccbcaccbbbcababbcaaccaabcbbabacababab"
p1 = "bbaaccbcacbbbcababbcaaccaabcbbabacababab"
p2 = "Possible"
all_right = (disabled or RunTest(72, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 73 -----
disabled = False
p0 = "cacaabbaaacbbc"
p1 = "cacaabbaaabbc"
p2 = "Possible"
all_right = (disabled or RunTest(73, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 74 -----
disabled = False
p0 = "cabcbabacbcaabbcbbbaababaaabaabbbabbaabcbccacccb"
p1 = "ccbcabacbcaabbcbbbaababaaabaabbbabbaabcbcaacccb"
p2 = "Impossible"
all_right = (disabled or RunTest(74, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 75 -----
disabled = False
p0 = "cbcbbcaabcbcabbbccccacbcbaacccbbc"
p1 = "cbcbccaabcbabbbcbccacbcbaacccbbc"
p2 = "Impossible"
all_right = (disabled or RunTest(75, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 76 -----
disabled = False
p0 = "baabbacbcabcaacaaaba"
p1 = "baabbabcabcaacaacba"
p2 = "Impossible"
all_right = (disabled or RunTest(76, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 77 -----
disabled = False
p0 = "bcbbaccbcbccacbbbbbccccbbaa"
p1 = "bcbbaccbcbccbcbabbbccccbba"
p2 = "Impossible"
all_right = (disabled or RunTest(77, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 78 -----
disabled = False
p0 = "bbabaaabbbabbabbaaabaabbbaaabaabbb"
p1 = "abaaabaabbbbaaaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(78, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 79 -----
disabled = False
p0 = "bbbabbabbbabaabbaabaaabbbbba"
p1 = "ababaaabaaaaabbaabbabbbaa"
p2 = "Impossible"
all_right = (disabled or RunTest(79, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 80 -----
disabled = False
p0 = "bbbbbabaabaabbbabaaabbabbabbabbbbabaababaa"
p1 = "baaaabbabbaabbaabaaabbbbaab"
p2 = "Impossible"
all_right = (disabled or RunTest(80, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 81 -----
disabled = False
p0 = "bbbabaaaababaaaaaaaa"
p1 = "bababababbbaababbbbbabbaaaabbabbbbbaabbabbbabbaa"
p2 = "Impossible"
all_right = (disabled or RunTest(81, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 82 -----
disabled = False
p0 = "abaababbaaabaabaaaaaaabaabbbaababaaaabbaaaaab"
p1 = "bababbbaabbbababbbbbabbbababbbbaaaaabbbbababb"
p2 = "Impossible"
all_right = (disabled or RunTest(82, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 83 -----
disabled = False
p0 = "abaabaaaabbaabaabaaaaabbbbabbbaabbbbaaabbbaa"
p1 = "bbabbabaabaaaabaaabaabbabaabbaababaabababaabab"
p2 = "Impossible"
all_right = (disabled or RunTest(83, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 84 -----
disabled = False
p0 = "aabbaabbbbabbaaaabbaaaababbb"
p1 = "aaaaaaabbabbbabbbabbaabbbabbbababababbaaab"
p2 = "Impossible"
all_right = (disabled or RunTest(84, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 85 -----
disabled = False
p0 = "bbbbaabbababbbbbbbbbbbbabaaabbbb"
p1 = "bbbabbabababba"
p2 = "Impossible"
all_right = (disabled or RunTest(85, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 86 -----
disabled = False
p0 = "abbaababbbaabaaababbbaabbbaabbabbbbbbbbaba"
p1 = "aabbbaaaababbaabbbbab"
p2 = "Impossible"
all_right = (disabled or RunTest(86, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 87 -----
disabled = False
p0 = "bbabbbbabbaaaabbaaabaaabbaaababa"
p1 = "aaabaaababaabaaaaab"
p2 = "Impossible"
all_right = (disabled or RunTest(87, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 88 -----
disabled = False
p0 = "a"
p1 = "a"
p2 = "Impossible"
all_right = (disabled or RunTest(88, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 89 -----
disabled = False
p0 = "a"
p1 = "b"
p2 = "Impossible"
all_right = (disabled or RunTest(89, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 90 -----
disabled = False
p0 = "a"
p1 = "ac"
p2 = "Impossible"
all_right = (disabled or RunTest(90, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 91 -----
disabled = False
p0 = "a"
p1 = "ca"
p2 = "Impossible"
all_right = (disabled or RunTest(91, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 92 -----
disabled = False
p0 = "a"
p1 = "bc"
p2 = "Impossible"
all_right = (disabled or RunTest(92, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 93 -----
disabled = False
p0 = "sunuke"
p1 = "sunuke"
p2 = "Impossible"
all_right = (disabled or RunTest(93, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 94 -----
disabled = False
p0 = "ss"
p1 = "ss"
p2 = "Impossible"
all_right = (disabled or RunTest(94, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 95 -----
disabled = False
p0 = "abcd"
p1 = "adc"
p2 = "Impossible"
all_right = (disabled or RunTest(95, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 96 -----
disabled = False
p0 = "ab"
p1 = "aaba"
p2 = "Impossible"
all_right = (disabled or RunTest(96, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 97 -----
disabled = False
p0 = "nnnn"
p1 = "nnnn"
p2 = "Impossible"
all_right = (disabled or RunTest(97, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 98 -----
disabled = False
p0 = "abcddddd"
p1 = "abcd"
p2 = "Impossible"
all_right = (disabled or RunTest(98, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 99 -----
disabled = False
p0 = "aa"
p1 = "aaa"
p2 = "Impossible"
all_right = (disabled or RunTest(99, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 100 -----
disabled = False
p0 = "pera"
p1 = "pea"
p2 = "Possible"
all_right = (disabled or RunTest(100, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 101 -----
disabled = False
p0 = "abc"
p1 = "abcabcababcabcababcabcababcabcababcabcababcabcab"
p2 = "Impossible"
all_right = (disabled or RunTest(101, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 102 -----
disabled = False
p0 = "abcde"
p1 = "bcde"
p2 = "Possible"
all_right = (disabled or RunTest(102, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 103 -----
disabled = False
p0 = "abc"
p1 = "aabc"
p2 = "Impossible"
all_right = (disabled or RunTest(103, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 104 -----
disabled = False
p0 = "ab"
p1 = "d"
p2 = "Impossible"
all_right = (disabled or RunTest(104, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 105 -----
disabled = False
p0 = "abcr"
p1 = "abcde"
p2 = "Impossible"
all_right = (disabled or RunTest(105, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 106 -----
disabled = False
p0 = "abc"
p1 = "dcba"
p2 = "Impossible"
all_right = (disabled or RunTest(106, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 107 -----
disabled = False
p0 = "aabc"
p1 = "acb"
p2 = "Impossible"
all_right = (disabled or RunTest(107, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 108 -----
disabled = False
p0 = "qwerty"
p1 = "qwery"
p2 = "Possible"
all_right = (disabled or RunTest(108, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 109 -----
disabled = False
p0 = "asdfafghh"
p1 = "asdaafgh"
p2 = "Impossible"
all_right = (disabled or RunTest(109, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 110 -----
disabled = False
p0 = "aaa"
p1 = "aa"
p2 = "Possible"
all_right = (disabled or RunTest(110, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 111 -----
disabled = False
p0 = "aaab"
p1 = "aaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(111, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 112 -----
disabled = False
p0 = "abcdef"
p1 = "abc"
p2 = "Impossible"
all_right = (disabled or RunTest(112, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 113 -----
disabled = False
p0 = "abc"
p1 = "ae"
p2 = "Impossible"
all_right = (disabled or RunTest(113, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 114 -----
disabled = False
p0 = "abcd"
p1 = "gcd"
p2 = "Impossible"
all_right = (disabled or RunTest(114, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 115 -----
disabled = False
p0 = "cabc"
p1 = "acb"
p2 = "Impossible"
all_right = (disabled or RunTest(115, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 116 -----
disabled = False
p0 = "aaaaa"
p1 = "aaaab"
p2 = "Impossible"
all_right = (disabled or RunTest(116, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 117 -----
disabled = False
p0 = "aaa"
p1 = "aaaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(117, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 118 -----
disabled = False
p0 = "ac"
p1 = "b"
p2 = "Impossible"
all_right = (disabled or RunTest(118, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 119 -----
disabled = False
p0 = "abc"
p1 = "abcd"
p2 = "Impossible"
all_right = (disabled or RunTest(119, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 120 -----
disabled = False
p0 = "accb"
p1 = "adb"
p2 = "Impossible"
all_right = (disabled or RunTest(120, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 121 -----
disabled = False
p0 = "abcd"
p1 = "abd"
p2 = "Possible"
all_right = (disabled or RunTest(121, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 122 -----
disabled = False
p0 = "hello"
p1 = "heoo"
p2 = "Impossible"
all_right = (disabled or RunTest(122, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 123 -----
disabled = False
p0 = "abecd"
p1 = "bcde"
p2 = "Impossible"
all_right = (disabled or RunTest(123, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 124 -----
disabled = False
p0 = "abc"
p1 = "bc"
p2 = "Possible"
all_right = (disabled or RunTest(124, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 125 -----
disabled = False
p0 = "aaaaaaa"
p1 = "aaaaaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(125, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 126 -----
disabled = False
p0 = "adsfefef"
p1 = "asdfefef"
p2 = "Impossible"
all_right = (disabled or RunTest(126, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 127 -----
disabled = False
p0 = "abc"
p1 = "acdef"
p2 = "Impossible"
all_right = (disabled or RunTest(127, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 128 -----
disabled = False
p0 = "snuke"
p1 = "snuk"
p2 = "Possible"
all_right = (disabled or RunTest(128, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 129 -----
disabled = False
p0 = "abcd"
p1 = "abc"
p2 = "Possible"
all_right = (disabled or RunTest(129, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 130 -----
disabled = False
p0 = "snnke"
p1 = "suke"
p2 = "Impossible"
all_right = (disabled or RunTest(130, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 131 -----
disabled = False
p0 = "abaa"
p1 = "ab"
p2 = "Impossible"
all_right = (disabled or RunTest(131, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 132 -----
disabled = False
p0 = "aab"
p1 = "aaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(132, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 133 -----
disabled = False
p0 = "abc"
p1 = "abdck"
p2 = "Impossible"
all_right = (disabled or RunTest(133, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 134 -----
disabled = False
p0 = "abcd"
p1 = "cab"
p2 = "Impossible"
all_right = (disabled or RunTest(134, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 135 -----
disabled = False
p0 = "aaaabxaaaa"
p1 = "aaaacaaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(135, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 136 -----
disabled = False
p0 = "ahmad"
p1 = "amsd"
p2 = "Impossible"
all_right = (disabled or RunTest(136, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 137 -----
disabled = False
p0 = "bcato"
p1 = "bceo"
p2 = "Impossible"
all_right = (disabled or RunTest(137, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 138 -----
disabled = False
p0 = "aaa"
p1 = "aaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(138, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 139 -----
disabled = False
p0 = "aabaa"
p1 = "aaa"
p2 = "Impossible"
all_right = (disabled or RunTest(139, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 140 -----
disabled = False
p0 = "ababa"
p1 = "aaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(140, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 141 -----
disabled = False
p0 = "perap"
p1 = "peap"
p2 = "Possible"
all_right = (disabled or RunTest(141, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 142 -----
disabled = False
p0 = "ash"
p1 = "ashwin"
p2 = "Impossible"
all_right = (disabled or RunTest(142, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 143 -----
disabled = False
p0 = "hhh"
p1 = "h"
p2 = "Impossible"
all_right = (disabled or RunTest(143, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 144 -----
disabled = False
p0 = "aaa"
p1 = "ab"
p2 = "Impossible"
all_right = (disabled or RunTest(144, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 145 -----
disabled = False
p0 = "howa"
p1 = "howw"
p2 = "Impossible"
all_right = (disabled or RunTest(145, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 146 -----
disabled = False
p0 = "abcde"
p1 = "abc"
p2 = "Impossible"
all_right = (disabled or RunTest(146, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 147 -----
disabled = False
p0 = "aabaa"
p1 = "aaaaa"
p2 = "Impossible"
all_right = (disabled or RunTest(147, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 148 -----
disabled = False
p0 = "aaaa"
p1 = "aa"
p2 = "Impossible"
all_right = (disabled or RunTest(148, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 149 -----
disabled = False
p0 = "bab"
p1 = "aa"
p2 = "Impossible"
all_right = (disabled or RunTest(149, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 150 -----
disabled = False
p0 = "asua"
p1 = "usa"
p2 = "Impossible"
all_right = (disabled or RunTest(150, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 151 -----
disabled = False
p0 = "pqrs"
p1 = "prstt"
p2 = "Impossible"
all_right = (disabled or RunTest(151, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 152 -----
disabled = False
p0 = "abcde"
p1 = "abke"
p2 = "Impossible"
all_right = (disabled or RunTest(152, p0, p1, True, p2) ) and all_right
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
