__author__ = 'trunghieu11'


def maxMultiLength(words):
    answer = 0
    size = len(words)
    splitted = []
    for i in range(size):
        splitted.append(set(words[i]))

    for i in range(size):
        for j in range(size):
            canMulti = True
            for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if c in splitted[i] and c in splitted[j]:
                    canMulti = False
            if canMulti:
                answer = max(answer, len(words[i]) * len(words[j]))
    return answer


if __name__ == '__main__':
    words = ["ABCW", "BAZ", "FOO", "BAR", "XTFN", "ABCDEF"]
    print maxMultiLength(words)