class ValueOfString:
    def findValue(self, strx):
        sumx=0
        for i in strx:
            t = 0
            for j in strx:
                if j <= i:
                    t += 1
            sumx += (ord(i)-96)*t
        return (sumx)


##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, hasAnswer, p1):
    obj = ValueOfString()
    startTime = time.clock()
    answer = obj.findValue(p0)
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
p0 = "babca"
p1 = 35
all_right = (disabled or RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = "zz"
p1 = 104
all_right = (disabled or RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = "zyxwvutsrqponmlkjihgfedcba"
p1 = 6201
all_right = (disabled or RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = "topcoder"
p1 = 558
all_right = (disabled or RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = "charlie"
p1 = 297
all_right = (disabled or RunTest(4, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = "valueofstring"
p1 = 1502
all_right = (disabled or RunTest(5, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = "abcdefghijklmnopqrstuvwxyz"
p1 = 6201
all_right = (disabled or RunTest(6, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = "thequickbrownfoxjumpsoverthelazydog"
p1 = 11187
all_right = (disabled or RunTest(7, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = "a"
p1 = 1
all_right = (disabled or RunTest(8, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = "b"
p1 = 2
all_right = (disabled or RunTest(9, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = "z"
p1 = 26
all_right = (disabled or RunTest(10, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = "itwasthebestoftimesitwastheworstoftimesitwastheage"
p1 = 23206
all_right = (disabled or RunTest(11, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = "ofwisdomitwastheageoffoolishnessitwastheepochofbel"
p1 = 20393
all_right = (disabled or RunTest(12, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = "iefitwastheepochofincredulityitwastheseasonoflight"
p1 = 20660
all_right = (disabled or RunTest(13, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = "itwastheseasonofdarknessitwasthespringofhopeitwast"
p1 = 22276
all_right = (disabled or RunTest(14, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = "hewinterofdespairwehadeverythingbeforeuswehadnothi"
p1 = 20124
all_right = (disabled or RunTest(15, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = "ngbeforeuswewereallgoingdirecttoheavenwewereallgoi"
p1 = 19714
all_right = (disabled or RunTest(16, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = "ngdirecttheotherwayinshorttheperiodwassofarlikethe"
p1 = 21097
all_right = (disabled or RunTest(17, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = "presentperiodthatsomeofitsnoisiestauthoritiesinsis"
p1 = 22556
all_right = (disabled or RunTest(18, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = "tedonitsbeingreceivedforgoodorforevilinthesuperlat"
p1 = 20182
all_right = (disabled or RunTest(19, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = "ivedegreeofcomparisononlytherewereakingwithalargej"
p1 = 19402
all_right = (disabled or RunTest(20, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = "awandaqueenwithaplainfaceonthethroneofenglandthere"
p1 = 18478
all_right = (disabled or RunTest(21, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = "wereakingwithalargejawandaqueenwithafairfaceonthet"
p1 = 18599
all_right = (disabled or RunTest(22, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = "hroneoffranceinbothcountriesitwasclearerthancrysta"
p1 = 20826
all_right = (disabled or RunTest(23, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = "ltothelordsofthestatepreservesofloavesandfishestha"
p1 = 21337
all_right = (disabled or RunTest(24, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = "tthingsingeneralweresettledforeveritwastheyearofou"
p1 = 21648
all_right = (disabled or RunTest(25, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = "rlordonethousandsevenhundredandseventyfivespiritua"
p1 = 21762
all_right = (disabled or RunTest(26, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 27 -----
disabled = False
p0 = "lrevelationswereconcededtoenglandatthatfavouredper"
p1 = 19759
all_right = (disabled or RunTest(27, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 28 -----
disabled = False
p0 = "iodasatthismrssouthcotthadrecentlyattainedherfivea"
p1 = 20915
all_right = (disabled or RunTest(28, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 29 -----
disabled = False
p0 = "ndtwentiethblessedbirthdayofwhomapropheticprivatei"
p1 = 20691
all_right = (disabled or RunTest(29, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 30 -----
disabled = False
p0 = "nthelifeguardshadheraldedthesublimeappearancebyann"
p1 = 17219
all_right = (disabled or RunTest(30, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 31 -----
disabled = False
p0 = "ouncingthatarrangementsweremadefortheswallowingupo"
p1 = 20876
all_right = (disabled or RunTest(31, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 32 -----
disabled = False
p0 = "flondonandwestminstereventhecocklaneghosthadbeenla"
p1 = 18832
all_right = (disabled or RunTest(32, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 33 -----
disabled = False
p0 = "idonlyarounddozenofyearsafterrappingoutitsmessages"
p1 = 21857
all_right = (disabled or RunTest(33, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 34 -----
disabled = False
p0 = "asthespiritsofthisveryyearlastpastsupernaturallyde"
p1 = 23665
all_right = (disabled or RunTest(34, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 35 -----
disabled = False
p0 = "ficientinoriginalityrappedouttheirsmeremessagesint"
p1 = 20608
all_right = (disabled or RunTest(35, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 36 -----
disabled = False
p0 = "heearthlyorderofeventshadlatelycometotheenglishcro"
p1 = 20200
all_right = (disabled or RunTest(36, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 37 -----
disabled = False
p0 = "wnandpeoplefromacongressofbritishsubjectsinamerica"
p1 = 19529
all_right = (disabled or RunTest(37, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 38 -----
disabled = False
p0 = "whichstrangetorelatehaveprovedmoreimportanttothehu"
p1 = 21637
all_right = (disabled or RunTest(38, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 39 -----
disabled = False
p0 = "manracethananycommunicationsyetreceivedthroughanyo"
p1 = 20784
all_right = (disabled or RunTest(39, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 40 -----
disabled = False
p0 = "fthechickensofthecocklanebroodfrancelessfavouredon"
p1 = 18065
all_right = (disabled or RunTest(40, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 41 -----
disabled = False
p0 = "thewholeastomattersspiritualthanhersisteroftheshie"
p1 = 22046
all_right = (disabled or RunTest(41, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 42 -----
disabled = False
p0 = "ldandtridentrolledwithexceedingsmoothnessdownhillm"
p1 = 20087
all_right = (disabled or RunTest(42, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 43 -----
disabled = False
p0 = "akingpapermoneyandspendingitundertheguidanceofherc"
p1 = 18436
all_right = (disabled or RunTest(43, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 44 -----
disabled = False
p0 = "hristianpastorssheentertainedherselfbesideswithsuc"
p1 = 21060
all_right = (disabled or RunTest(44, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 45 -----
disabled = False
p0 = "hhumaneachievementsassentencingayouthtohavehishand"
p1 = 19772
all_right = (disabled or RunTest(45, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 46 -----
disabled = False
p0 = "scutoffhistonguetornoutwithpincersandhisbodyburned"
p1 = 22042
all_right = (disabled or RunTest(46, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 47 -----
disabled = False
p0 = "alivebecausehehadnotkneeleddownintheraintodohonour"
p1 = 19050
all_right = (disabled or RunTest(47, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 48 -----
disabled = False
p0 = "toadirtyprocessionofmonkswhichpassedwithinhisviewa"
p1 = 21791
all_right = (disabled or RunTest(48, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 49 -----
disabled = False
p0 = "tadistanceofsomefiftyorsixtyyardsitislikelyenought"
p1 = 22741
all_right = (disabled or RunTest(49, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 50 -----
disabled = False
p0 = "hatrootedinthewoodsoffranceandnorwaythereweregrowi"
p1 = 21439
all_right = (disabled or RunTest(50, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 51 -----
disabled = False
p0 = "ngtreeswhenthatsuffererwasputtodeathalreadymarkedb"
p1 = 20890
all_right = (disabled or RunTest(51, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 52 -----
disabled = False
p0 = "ythewoodmanfatetocomedownandbesawnintoboardstomake"
p1 = 20584
all_right = (disabled or RunTest(52, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 53 -----
disabled = False
p0 = "acertainmovableframeworkwithasackandaknifeinitterr"
p1 = 18995
all_right = (disabled or RunTest(53, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 54 -----
disabled = False
p0 = "ibleinhistoryitislikelyenoughthatintheroughouthous"
p1 = 22263
all_right = (disabled or RunTest(54, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 55 -----
disabled = False
p0 = "esofsometillersoftheheavylandsadjacenttoparisthere"
p1 = 20162
all_right = (disabled or RunTest(55, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 56 -----
disabled = False
p0 = "wereshelteredfromtheweatherthatverydayrudecartsbes"
p1 = 21782
all_right = (disabled or RunTest(56, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 57 -----
disabled = False
p0 = "patteredwithrusticmiresnuffedaboutbypigsandroosted"
p1 = 21514
all_right = (disabled or RunTest(57, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 58 -----
disabled = False
p0 = "inbypoultrywhichthefarmerdeathhadalreadysetapartto"
p1 = 20901
all_right = (disabled or RunTest(58, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 59 -----
disabled = False
p0 = "behistumbrilsoftherevolutionbutthatwoodmanandthatf"
p1 = 21592
all_right = (disabled or RunTest(59, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 60 -----
disabled = False
p0 = "armerthoughtheyworkunceasinglyworksilentlyandnoone"
p1 = 22258
all_right = (disabled or RunTest(60, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 61 -----
disabled = False
p0 = "heardthemastheywentaboutwithmuffledtreadtheratherf"
p1 = 20679
all_right = (disabled or RunTest(61, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 62 -----
disabled = False
p0 = "orasmuchastoentertainanysuspicionthattheywereawake"
p1 = 22095
all_right = (disabled or RunTest(62, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 63 -----
disabled = False
p0 = "aaabbc"
p1 = 47
all_right = (disabled or RunTest(63, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 64 -----
disabled = False
p0 = "y"
p1 = 25
all_right = (disabled or RunTest(64, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 65 -----
disabled = False
p0 = "abcabc"
p1 = 56
all_right = (disabled or RunTest(65, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 66 -----
disabled = False
p0 = "mmm"
p1 = 117
all_right = (disabled or RunTest(66, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 67 -----
disabled = False
p0 = "mamzmmwijfqpoaiponqoerjq"
p1 = 5033
all_right = (disabled or RunTest(67, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 68 -----
disabled = False
p0 = "jfjjfjjjjfjjfjfjjfjjjfjfj"
p1 = 4634
all_right = (disabled or RunTest(68, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 69 -----
disabled = False
p0 = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
p1 = 57500
all_right = (disabled or RunTest(69, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 70 -----
disabled = False
p0 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
p1 = 1225
all_right = (disabled or RunTest(70, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 71 -----
disabled = False
p0 = "abc"
p1 = 14
all_right = (disabled or RunTest(71, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 72 -----
disabled = False
p0 = "bbbcccdddaaazzz"
p1 = 1440
all_right = (disabled or RunTest(72, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 73 -----
disabled = False
p0 = "acdgknz"
p1 = 368
all_right = (disabled or RunTest(73, p0, True, p1) ) and all_right
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
