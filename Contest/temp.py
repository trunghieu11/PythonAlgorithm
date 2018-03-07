# TESTING 69 KATALON 84
# DEVELOPMENT 120 INTEGRITY 85
# JAVASCRIPT 110 ARCHITECTURE 144
# INNOVATION 97 KMS TECHNOLOGY

answers = []

known_words = ["KATALON", "TESTING", "INTEGRITY", "INNOVATION", "DEVELOPMENT", "JAVASCRIPT", "ARCHITECTURE"]
known_values = [84, 69, 85, 97, 120, 110, 144]

value_from = 1
value_to = 19


def index_of(letter):
    return ord(letter) - ord('A')


def potential_answer(cur_values):
    for word, value in zip(known_words, known_values):
        cur_sum = 0
        unknown = 0
        for x in word:
            if cur_values[index_of(x)] == 0:
                unknown += 1
            elif cur_values[index_of(x)] > 0:
                cur_sum += cur_values[index_of(x)]
            else:
                cur_sum -= cur_values[index_of(x)]
        remain = value - cur_sum
        if remain < unknown * value_from or value_to * unknown < remain:
            return False
    return True


# def checkValues(idx, cur_values, word, sum_value):
#     if not potential_answer(cur_values):
#         return
#
#     if idx >= len(word):
#         cur_sum = 0
#         for x in word:
#             if cur_values[index_of(x)] == 0:
#                 return
#
#             if cur_values[index_of(x)] > 0:
#                 cur_sum += cur_values[index_of(x)]
#             else:
#                 cur_sum -= cur_values[index_of(x)]
#
#         if cur_sum == sum_value:
#             answers.append(cur_values[:])
#         return
#
#     cur_idx = index_of(word[idx])
#     if cur_values[cur_idx] == 0:
#         for i in range(1, 20):
#             cur_values[cur_idx] = i
#
#             for j in range(cur_idx + 1, 26):
#                 if cur_values[j] > 0:
#                     cur_values[j] = 0
#
#             checkValues(idx + 1, cur_values, word, sum_value)
#     else:
#         checkValues(idx + 1, cur_values, word, sum_value)
#
#
#
# def findWords():
#     temp_answers = [[0 for i in range(26)]]
#
#     for x, y in zip(known_words, known_values):
#         x = list(x)
#         x.sort()
#         for cur_values in temp_answers:
#             for i,_ in enumerate(cur_values):
#                 if cur_values[i] > 0:
#                     cur_values[i] = cur_values[i] * (-1)
#             checkValues(0, cur_values, x, y)
#         temp_answers = answers[:]
#
#         print("=" * 20)
#         print("Finish " + str(x))
#         print(len(answers))
#
#         answers.clear()
#
#     for value in temp_answers:
#         result = 0
#         print("=" * 20)
#         print(value)
#         for x in "KMSTECHNOLOGY":
#             result += value[index_of(x)]
#         print(result)
#
#
# def testing():
#     word = "TESTING"
#     word = list(word)
#     word.sort()
#     existed = set()
#     word_index = set([index_of(x) for x in word])
#
#     value = 69
#     answers.clear()
#     prev_answers = []
#
#     with open('katalon.txt', 'r') as reader:
#         for line in reader:
#             cur_answers = list(map(int, line.split()))
#             for i in range(len(cur_answers)):
#                 if i not in word_index:
#                     cur_answers[i] = 0
#                 elif cur_answers[i] > 0:
#                     cur_answers[i] = -cur_answers[i]
#
#             if tuple(cur_answers) not in existed:
#                 existed.add(tuple(cur_answers))
#                 prev_answers.append(cur_answers)
#
#     with open('testing.txt', 'w') as writer:
#         for pa in prev_answers:
#             checkValues(0, pa, word, value)
#         for a in answers:
#             writer.write(' '.join(str(x if x > 0 else -x) for x in a) + "\n")
#
#
#
# def katalon():
#     word = "KATALON"
#     word = list(word)
#     word.sort()
#
#     value = 84
#     answers.clear()
#
#     checkValues(0, [0 for i in range(26)], word, value)
#     f = open('katalon.txt', 'w')
#     for a in answers:
#         f.write(' '.join(str(x) for x in a) + "\n")
#     f.close()
#
#
# def joining():
#     writer = open('joining.txt', 'w')
#     katalon_answer = []
#     testing_answer = []
#
#     with open('katalon.txt', 'r') as katalon_reader:
#         for line in katalon_reader:
#             katalon_answer.append(list(map(int, line.split())))
#
#     with open('testing.txt', 'r') as testing_reader:
#         for line in testing_reader:
#             testing_answer.append(list(map(int, line.split())))
#
#     for x in katalon_answer:
#         for y in testing_answer:
#             ok = True
#             for i in range(26):
#                 if x[i] != 0 and y[i] != 0 and x[i] != y[i]:
#                     ok = False
#                     break
#                 x[i] = max(x[i], y[i])
#
#             if ok:
#                 writer.write(' '.join(str(value) for value in x) + "\n")
#
#     writer.close()


def in_range(x):
    return 1 <= x <= 19


def good_answer(cur_answer):
    a = cur_answer[:]
    for w, v in zip(known_words, known_values):

        missing = get_missing(w, "KMSTECHNOLOGY")
        remain = get_remain(w, v, a)
        # f.write(w + " " + str(v) + "\n")
        # f.write("missing: " + missing + "\n")
        # f.write("remain: " + str(remain) + "\n\n")

        if w == 'KATALON':
            a[index_of('A')] = remain / 2
            if not in_range(a[index_of('A')]):
                return False

        if w == 'TESTING':
            a[index_of('I')] = remain
            if not in_range(a[index_of('I')]):
                return False

        if w == 'INTEGRITY':
            a[index_of('R')] = remain
            if not in_range(a[index_of('R')]):
                return False

        if w == 'INNOVATION':
            a[index_of('V')] = remain
            if not in_range(a[index_of('V')]):
                return False

        if w == 'DEVELOPMENT':
            # f.write('DPM = ' + str(remain) + "\n")
            if not (3 <= remain <= 19 * 3):
                return False

        if w == 'JAVASCRIPT':
            if not (2 <= remain <= 19 * 2):
                return False

        if w == 'ARCHITECTURE':
            a[index_of('U')] = remain
            if not in_range(a[index_of('U')]):
                return False


def checkValues(idx, cur_values, word):
    if len(answers) > 0:
        return

    if not potential_answer(cur_values):
        return

    if idx >= len(word):
        if good_answer(cur_values):
            answers.append(cur_values[:])
        return

    cur_idx = index_of(word[idx])
    if cur_values[cur_idx] == 0:
        for i in range(1, 20):
            cur_values[cur_idx] = i
            checkValues(idx + 1, cur_values, word)
            cur_values[cur_idx] = 0
    else:
        checkValues(idx + 1, cur_values, word)


def get_missing(word, kms):
    result = ""
    for letter in word:
        if letter not in kms:
            result = result + letter
    return result


def get_remain(word, value, cur_answer):
    return value - sum(cur_answer[index_of(letter)] for letter in word)


def kmstechnology():
    word = "KNSTECHNOLOGY"
    word = list(word)
    word.sort()

    value = 84
    answers.clear()

    checkValues(0, [0 for i in range(26)], word)
    f = open('kmstechnology2.txt', 'w')
    for a in answers:
        f.write("=" * 40 + "\n")

        for w,v in zip(known_words, known_values):

            missing = get_missing(w, word)
            remain = get_remain(w, v, a)
            # f.write(w + " " + str(v) + "\n")
            # f.write("missing: " + missing + "\n")
            # f.write("remain: " + str(remain) + "\n\n")

            if w == 'KATALON':
                a[index_of('A')] = remain / 2
                f.write('A = ' + str(a[index_of('A')]) + "\n")

            if w == 'TESTING':
                a[index_of('I')] = remain
                f.write('I = ' + str(a[index_of('I')]) + "\n")

            if w == 'INTEGRITY':
                a[index_of('R')] = remain
                f.write('R = ' + str(a[index_of('R')]) + "\n")

            if w == 'INNOVATION':
                a[index_of('V')] = remain
                f.write('V = ' + str(a[index_of('V')]) + "\n")

            if w == 'DEVELOPMENT':
                f.write('DPM = ' + str(remain) + "\n")

            if w == 'JAVASCRIPT':
                f.write('JP = ' + str(remain) + "\n")

            if w == 'ARCHITECTURE':
                a[index_of('U')] = remain
                f.write('U = ' + str(a[index_of('U')]) + "\n")


        f.write(' '.join(str(x) for x in a) + "\n")

        f.write("\n")

    f.close()


if __name__ == '__main__':
    kmstechnology()