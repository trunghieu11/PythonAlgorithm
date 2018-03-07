# TESTING 69 KATALON 84
# DEVELOPMENT 120 INTEGRITY 85
# JAVASCRIPT 110 ARCHITECTURE 144
# INNOVATION 97 KMS TECHNOLOGY

answers = []

known_words = ["KATALON", "TESTING", "INTEGRITY", "INNOVATION", "DEVELOPMENT", "JAVASCRIPT", "ARCHITECTURE"]
known_values = [84, 69, 85, 97, 120, 110, 144]

value_from = 1
value_to = 19

same_threshold = 1


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


def in_range(x):
    return value_from <= x <= value_to


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
            if not (3 * value_from <= remain <= value_to * 3):
                return False

        if w == 'JAVASCRIPT':
            if not (2 * value_from <= remain <= value_to * 2):
                return False

        if w == 'ARCHITECTURE':
            a[index_of('U')] = remain
            if not in_range(a[index_of('U')]):
                return False


def checkValues(idx, cur_values, word, visited):
    if not potential_answer(cur_values):
        return

    if idx >= len(word):
        if good_answer(cur_values):
            print(cur_values)
            answers.append(cur_values[:])
        # answers.append(cur_values[:])
        return

    cur_idx = index_of(word[idx])
    for i in range(1, 20):
        if visited[i] < same_threshold:
            visited[i] += 1
            cur_values[cur_idx] = i
            checkValues(idx + 1, cur_values, word, visited)
            cur_values[cur_idx] = 0
            visited[i] -= 1


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
    word = list(set(list(word)))
    word.sort()

    value = 84
    answers.clear()

    visited = [0 for i in range(20)]

    checkValues(0, [0 for i in range(26)], word, visited)
    f = open('kmstechnology3.txt', 'w')
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