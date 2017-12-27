class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.color = "r"
        self.value = value

class RedBlack:
    def numTwists(self, keys):
        answer = 0
        root = None
        for x in keys:
            if root is None:
                root = Node(x)
            else:
                self.add_node(root, x)
            illegal_node = self.need_twist(root)
            while illegal_node:
                update_root, new_root = self.twist(illegal_node)

                if update_root:
                    root = new_root

                answer += 1
                root.color = "b"
                illegal_node = self.need_twist(root)
            root.color = "b"

        return answer

    def add_node(self, root, x):
        new_node = Node(x)
        leaf_node = root
        while True:
            if new_node.value > leaf_node.value:
                if leaf_node.right is not None:
                    leaf_node = leaf_node.right
                else:
                    leaf_node.right = new_node
                    new_node.parent = leaf_node
                    break
            else:
                if leaf_node.left is not None:
                    leaf_node = leaf_node.left
                else:
                    leaf_node.left = new_node
                    new_node.parent = leaf_node
                    break

    def need_twist(self, root):
        queue = [root]
        while queue:
            cur = queue[0]
            queue = queue[1:]
            if cur.left is not None:
                if cur.color == cur.left.color == "r":
                    return cur
                else:
                    queue.append(cur.left)
            if cur.right is not None:
                if cur.color == cur.right.color == "r":
                    return cur
                else:
                    queue.append(cur.right)
        return None

    def twist(self, illegal_node):
        grandfather = illegal_node.parent
        left = illegal_node.left
        right = illegal_node.right

        x = y = z = t1 = t2 = t3 = t4 = None

        # type 1
        if left is not None and illegal_node.color == left.color == "r":
            if grandfather.left is not None and illegal_node.value == grandfather.left.value:
                z = grandfather
                y = illegal_node
                x = left
                t1 = x.left
                t2 = x.right
                t3 = y.right
                t4 = z.right
                if z.parent is not None:
                    if z.parent.left is not None and z.parent.left.value == z.value:
                        z.parent.left = y
                    else:
                        z.parent.right = y
                y.parent = z.parent

        # type 2
        if right is not None and illegal_node.color == right.color == "r":
            if grandfather.left is not None and illegal_node.value == grandfather.left.value:
                z = grandfather
                y = right
                x = illegal_node
                t1 = x.left
                t2 = y.left
                t3 = y.right
                t4 = z.right
                if z.parent is not None:
                    if z.parent.left is not None and z.parent.left.value == z.value:
                        z.parent.left = y
                    else:
                        z.parent.right = y
                y.parent = z.parent

        # type 3
        if left is not None and illegal_node.color == left.color == "r":
            if grandfather.right is not None and illegal_node.value == grandfather.right.value:
                z = illegal_node
                y = left
                x = grandfather
                t1 = x.left
                t2 = y.left
                t3 = y.right
                t4 = z.right
                if x.parent is not None:
                    if x.parent.left is not None and x.parent.left.value == x.value:
                        x.parent.left = y
                    else:
                        x.parent.right = y
                y.parent = x.parent

        # type 4
        if right is not None and illegal_node.color == right.color == "r":
            if grandfather.right is not None and illegal_node.value == grandfather.right.value:
                z = right
                y = illegal_node
                x = grandfather
                t1 = x.left
                t2 = y.left
                t3 = z.left
                t4 = z.right
                if x.parent is not None:
                    if x.parent.left is not None and x.parent.left.value == x.value:
                        x.parent.left = y
                    else:
                        x.parent.right = y
                y.parent = x.parent

        y.left = x
        y.right = z
        x.parent = y
        z.parent = y

        x.left = t1
        if t1 is not None:
            t1.parent = x

        x.right = t2
        if t2 is not None:
            t2.parent = x

        z.left = t3
        if t3 is not None:
            t3.parent = z

        z.right = t4
        if t4 is not None:
            t4.parent = z

        x.color = "b"
        y.color = "r"
        z.color = "b"

        if y.parent is None:
            return True, y

        return False, None

##########################
#        BEGIN TEST      #
##########################
import sys
import time
def RunTest(testNum, p0, hasAnswer, p1):
    obj = RedBlack()
    startTime = time.clock()
    answer = obj.numTwists(p0)
    endTime = time.clock()
    testTime.append(endTime - startTime)
    res = True
    if hasAnswer:
        res = compare_answer(answer, p1)
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

def compare_answer(my_answer, correct_answer):
    if isinstance(my_answer, float) and isinstance(correct_answer, float):
        return round(my_answer, 6) == round(correct_answer, 6)
    return my_answer == correct_answer
all_right = True
tests_disabled = False
testTime = []
# ----- test 0 -----
disabled = False
p0 = (1, 2, 3)
p1 = 1
all_right = (disabled or RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = (1, 2, 3, 4, 5, 6, 7)
p1 = 4
all_right = (disabled or RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = (7, 1, 4, 6, 3, 5, 2)
p1 = 3
all_right = (disabled or RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = (2, 1, 3, 4)
p1 = 1
all_right = (disabled or RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = (1,)
p1 = 0
all_right = (disabled or RunTest(4, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = (5, 10, 15, 14, 3, 4, 11, 2, 1, 12, 6, 9, 7, 13, 8)
p1 = 11
all_right = (disabled or RunTest(5, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50)
p1 = 42
all_right = (disabled or RunTest(6, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 7 -----
disabled = False
p0 = (7, 5, 6, 4, 13, 1, 3, 10, 15, 2, 8, 9, 11, 12, 14)
p1 = 11
all_right = (disabled or RunTest(7, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 8 -----
disabled = False
p0 = (31, 6, 20, 8, 21, 28, 15, 14, 5, 30, 25, 13, 19, 9, 12, 22, 18, 2, 27, 10, 3, 24, 26, 7, 11, 16, 17, 32, 29, 1, 33, 23, 4)
p1 = 25
all_right = (disabled or RunTest(8, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 9 -----
disabled = False
p0 = (1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11)
p1 = 14
all_right = (disabled or RunTest(9, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 10 -----
disabled = False
p0 = (10, 9, 11, 8, 12, 7, 13, 6, 14, 5, 15, 4, 16, 3, 17, 2, 18, 1, 19)
p1 = 11
all_right = (disabled or RunTest(10, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 11 -----
disabled = False
p0 = (8, 4, 12, 2, 10, 6, 14, 1, 9, 7, 15, 5, 11, 3, 13)
p1 = 5
all_right = (disabled or RunTest(11, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 12 -----
disabled = False
p0 = (2, 4, 9, 7, 10, 6, 8, 1, 5, 3)
p1 = 2
all_right = (disabled or RunTest(12, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 13 -----
disabled = False
p0 = (8, 7, 10, 5, 1, 3, 6, 12, 11, 13, 2, 9, 4)
p1 = 3
all_right = (disabled or RunTest(13, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 14 -----
disabled = False
p0 = (15, 2, 9, 5, 3, 13, 11, 7, 8, 14, 1, 16, 4, 6, 10, 12)
p1 = 5
all_right = (disabled or RunTest(14, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 15 -----
disabled = False
p0 = (6, 8, 10, 12, 4, 2, 18, 14, 16, 19, 7, 15, 9, 17, 13, 5, 11, 3, 1)
p1 = 5
all_right = (disabled or RunTest(15, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 16 -----
disabled = False
p0 = (7, 6, 13, 10, 17, 8, 5, 16, 18, 14, 3, 9, 4, 11, 1, 19, 12, 2, 15)
p1 = 14
all_right = (disabled or RunTest(16, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 17 -----
disabled = False
p0 = (3, 13, 6, 5, 9, 14, 12, 11, 8, 2, 4, 1, 17, 7, 15, 16, 10)
p1 = 12
all_right = (disabled or RunTest(17, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 18 -----
disabled = False
p0 = (5, 4, 6, 9, 3, 1, 8, 2, 7)
p1 = 5
all_right = (disabled or RunTest(18, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 19 -----
disabled = False
p0 = (29, 15, 18, 25, 16, 7, 12, 28, 34, 35, 3, 27, 33, 6, 21, 24, 30, 31, 26, 23, 11, 10, 14, 1, 17, 4, 5, 9, 32, 20, 13, 19, 8, 22, 2)
p1 = 29
all_right = (disabled or RunTest(19, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 20 -----
disabled = False
p0 = (25, 7, 16, 33, 1, 19, 30, 13, 12, 29, 28, 34, 39, 41, 38, 22, 11, 32, 26, 14, 31, 23, 37, 6, 40, 21, 24, 10, 5, 17, 36, 35, 15, 2, 4, 3, 9, 8, 18, 20, 27)
p1 = 32
all_right = (disabled or RunTest(20, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 21 -----
disabled = False
p0 = (3, 26, 38, 21, 39, 6, 16, 46, 15, 27, 20, 14, 50, 32, 24, 19, 33, 37, 17, 29, 18, 11, 36, 25, 48, 49, 5, 7, 13, 35, 28, 45, 10, 4, 31, 34, 44, 40, 22, 43, 41, 9, 1, 47, 12, 8, 2, 23, 30, 42)
p1 = 38
all_right = (disabled or RunTest(21, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 22 -----
disabled = False
p0 = (2, 16, 8, 40, 42, 33, 25, 15, 1, 4, 6, 17, 41, 31, 49, 19, 10, 50, 13, 12, 35, 23, 29, 37, 21, 18, 7, 38, 14, 24, 39, 46, 5, 28, 32, 47, 26, 11, 9, 20, 27, 3, 44, 45, 22, 48, 43, 34, 30, 36)
p1 = 20
all_right = (disabled or RunTest(22, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 23 -----
disabled = False
p0 = (19, 12, 17, 6, 2, 8, 23, 10, 14, 21, 3, 15, 25, 27, 1, 13, 4, 11, 16, 22, 9, 20, 24, 7, 26, 5, 18)
p1 = 9
all_right = (disabled or RunTest(23, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 24 -----
disabled = False
p0 = (6, 8, 20, 21, 4, 23, 18, 28, 36, 32, 26, 22, 16, 24, 34, 12, 10, 15, 25, 40, 2, 7, 19, 29, 1, 11, 9, 14, 31, 5, 38, 3, 27, 30, 17, 35, 13, 39, 33, 37)
p1 = 14
all_right = (disabled or RunTest(24, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 25 -----
disabled = False
p0 = (2, 1, 3)
p1 = 0
all_right = (disabled or RunTest(25, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 26 -----
disabled = False
p0 = (5, 10, 15, 14, 3, 4, 11, 2, 1, 12, 6, 9, 7, 13, 8, 19, 18, 17, 16, 20, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 21, 22, 23, 24, 25, 26, 27, 28, 29, 41, 43, 45, 47, 49, 50, 48, 46, 44, 42)
p1 = 37
all_right = (disabled or RunTest(26, p0, True, p1) ) and all_right
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
